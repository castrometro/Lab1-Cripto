import sys

def cifrado_cesar(texto, rotacion):
    # Definimos el abecedario español
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    cifrado = ''
    
    # Convertimos el texto a minúsculas para tratar mayúsculas y minúsculas de la misma manera
    texto = texto.lower()
    
    for char in texto:
        if char in abecedario:
            # Obtenemos la posición del caracter en el abecedario
            pos_original = abecedario.index(char)
            
            # Calculamos la nueva posición con la rotación
            nueva_pos = (pos_original + rotacion) % len(abecedario)
            
            # Añadimos el nuevo caracter al texto cifrado
            cifrado += abecedario[nueva_pos]
        else:
            # Si el caracter no está en el abecedario, lo añadimos sin cambiarlo
            cifrado += char
    
    return cifrado

if __name__ == '__main__':
    # Obtener el texto y la rotación desde los argumentos de línea de comandos
    texto = sys.argv[1]
    rotacion = int(sys.argv[2])
    
    resultado = cifrado_cesar(texto, rotacion)
    print(resultado)
