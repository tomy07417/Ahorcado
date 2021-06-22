import re



def sacar_tildes(palabra):
    '''
    Toma la cadena de caracteres ingresada, transforma en mayusculas todas las letras
    y se reemplazan las vocales que tienen tilde por las mismas pero sin la tilde. 
    
    Autor: Renata Pastorini
    '''
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
    '''
    Esta función toma el texto ingresado por parámetro, y devuelve una lista de palabras en la cual se 
    encuentran todas las palabras "validas", osea aquellas que tienen longitud mayor o igual a cinco.
    
    Autor: Tomás Amundarain
    '''

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
    '''
    Esta función genera un diccionario que contiene como claves palabras con longitud igual 
    o mayor a cinco, y que tiene como valor asociado la cantidad de veces que la palabra aparece
    en el texto ingresado por parametro.
    Éste está ordenado alfabéticamente.
    
    Autor: Tomás Amundarain
    '''
    
    lista_palabras = palabras_validas(texto)

    diccionario_palabras = {}

    for palabra in lista_palabras:
        if (palabra in diccionario_palabras):
            diccionario_palabras[palabra] += 1

        else:
            diccionario_palabras[palabra] = 1

    return dict(sorted(diccionario_palabras.items(), key = lambda palabra: palabra[0]))



