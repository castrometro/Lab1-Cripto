import scapy.all as scapy
from collections import Counter
import string

# Diccionario de frecuencias de letras en español, incluyendo la 'ñ'
freq_espanol = {
    'a': 12.53, 'b': 1.42, 'c': 4.68, 'd': 5.86, 'e': 13.68,
    'f': 0.69, 'g': 1.01, 'h': 0.70, 'i': 6.25, 'j': 0.44,
    'k': 0.02, 'l': 4.97, 'm': 3.15, 'n': 6.71, 'ñ': 0.31,
    'o': 8.68, 'p': 2.51, 'q': 0.88, 'r': 6.87, 's': 7.98,
    't': 4.63, 'u': 3.93, 'v': 0.90, 'w': 0.01, 'x': 0.22,
    'y': 0.90, 'z': 0.52
}

def cesar_cipher(text, shift):
    """Cifrar un texto usando el cifrado César con un corrimiento específico"""
    alphabet = "abcdefghijklmnñopqrstuvwxyz"
    table = str.maketrans(alphabet, alphabet[shift:] + alphabet[:shift])
    return text.translate(table)

def compute_score(text):
    """Calcular un score basado en las frecuencias de letras en español"""
    count = Counter(text)
    score = sum([freq_espanol[char] for char in text if char in freq_espanol])
    return score

def best_shift(text):
    """Determinar el mejor corrimiento para el cifrado César basado en las frecuencias de letras en español"""
    best_score = -1
    best_shift = -1
    for shift in range(27):  # Ahora 27 debido a la 'ñ'
        encoded = cesar_cipher(text, shift)
        score = compute_score(encoded)
        if score > best_score:
            best_score = score
            best_shift = shift
    return best_shift

def packet_handler(pkt):
    """Manejador de paquetes para extraer el último byte del payload de un paquete ICMP request"""
    global accumulated_string
    
    if pkt.haslayer(scapy.ICMP) and pkt[scapy.ICMP].type == 8:  # ICMP request
        payload = pkt[scapy.Raw].load
        last_byte = chr(payload[-1]).lower()  # Convertir a minúsculas
        accumulated_string += last_byte
        print_all_shifts(accumulated_string)

def original_shift(best_shift):
    """Calcular el corrimiento original que se le hizo al string para cifrarlo"""
    return 27 - best_shift

def print_all_shifts(text):
    """Imprimir todas las codificaciones posibles, destacando la más probable en verde"""
    probable_shift = best_shift(text)
    original_probable_shift = original_shift(probable_shift)
    for shift in range(27):  # Ahora 27 debido a la 'ñ'
        encoded = cesar_cipher(text, shift)
        original_encoded_shift = original_shift(shift)
        if shift == probable_shift:
            print(f"\033[92mShift {original_encoded_shift}: {encoded}\033[0m")  # verde
        else:
            print(f"Shift {original_encoded_shift}: {encoded}")


accumulated_string = ""

# Escuchar paquetes ICMP
scapy.sniff(filter="icmp", prn=packet_handler)

