import random


def seleccion_palabra(diccionario):
    lista_palabras = list(diccionario.keys())
    lista_palabras_longitud = []
    resp = ''
    if input("¿Quiere ingresar la longitud de la palabra a adivinar? (s/n): ").upper() == "S" :
        longitud = int(input("Ingrese la longitud de la palabra a adivinar, debe ser un valor entre 5 y " + str(longitud_palabra_mas_larga(diccionario)) + ": "))
        for i in range (len(lista_palabras)):
            if len(lista_palabras[i]) == longitud:
                lista_palabras_longitud.append(lista_palabras[i]) 
    
        random_num = random.randint(0, len(lista_palabras_longitud) - 1)

        resp += lista_palabras_longitud[random_num]

    else:    
        random_num = random.randint(0, len(lista_palabras) - 1)
        resp += lista_palabras[random_num]

    return resp
    

def longitud_palabra_mas_larga(diccionario):
    lista = list(diccionario)
    mas_larga = lista[0]
    resp = 0
    for palabra in lista:
        if len(mas_larga) < len(palabra):
            mas_larga = palabra
    
    resp = len(mas_larga)

    return resp



