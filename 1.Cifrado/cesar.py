import argparse

def cifrado_cesar(texto, corrimiento):
    resultado = ''
    for caracter in texto:
        if caracter.isalpha():
            if caracter.islower():
                nuevo_caracter = chr(((ord(caracter) - ord('a') + corrimiento) % 26) + ord('a'))
            else:
                nuevo_caracter = chr(((ord(caracter) - ord('A') + corrimiento) % 26) + ord('A'))
        else:
            nuevo_caracter = caracter
        resultado += nuevo_caracter
    return resultado

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Cifrado César en Python')
    parser.add_argument('texto', type=str, help='Texto a cifrar')
    parser.add_argument('corrimiento', type=int, help='Número de corrimiento')
    args = parser.parse_args()
    
    texto_cifrado = cifrado_cesar(args.texto, args.corrimiento)
    print('Texto cifrado:', texto_cifrado)
