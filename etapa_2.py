import re
from unicodedata import normalize



def sacar_tildes(palabra):
    palabra = palabra.upper()
    palabra_sin = ''
    diccionario = {"Á": "A" , "É": "E" , "Í": "I", "Ó": "O" , "Ú": "U"} 
    for letra in palabra:
        if letra in diccionario:
            palabra_sin += diccionario[letra]
        else:
            palabra_sin += letra
    
    return palabra_sin


def palabras_validas(texto):
    lista_palabra_valida = []

    for palabra in re.split(' |-|_|\n', texto):
        palabra_sin = ''
        for letra in palabra:
            if (letra.isalpha()):
                palabra_sin += letra
        if (len(palabra_sin) >= 5):
            lista_palabra_valida.append(sacar_tildes(palabra_sin))

    return lista_palabra_valida


def crear_diccionario(texto):
    lista_palabras = palabras_validas(texto)

    diccionario_palabras = {}

    for palabra in lista_palabras:
        if (palabra in diccionario_palabras):
            diccionario_palabras[palabra] += 1

        else:
            diccionario_palabras[palabra] = 1

    return dict(sorted(diccionario_palabras.items(), key=lambda palabra: palabra[0]))
