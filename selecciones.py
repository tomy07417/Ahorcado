import random

def palabras_con_longitud(archivo_csv, longitud):
    """
    La función genera una lista que dice en que linea del archivo csv se encuentran las palabras con la longitud pasada 
    por parámetro.

    Autor: Franco Singh
    """
    lista_posiciones = []
    linea = archivo_csv.readline()
    linea_lista = linea.rstrip('\n').split(',')
    cont = 1
    while linea:
        palabra = linea_lista[0]
        if len(palabra) == longitud:
            lista_posiciones.append(cont)
        
        cont += 1
        linea = archivo_csv.readline()
        linea_lista = linea.rstrip('\n').split(',')

    return lista_posiciones

def seleccion_palabra(nombre_archivo_csv, longitud):
    """
    La función elige una palabra del archivo csv que cumpla con la longitud pasada por parámetro.

    Autor: Franco Singh
    """
    archivo_abierto = open(nombre_archivo_csv)

    posiciones_en_archivo = palabras_con_longitud(archivo_abierto, longitud)

    N = len(posiciones_en_archivo)
    random_num = random.randint(0, N)
    
    cont = 0
    
    archivo_abierto.seek(0)

    while cont < posiciones_en_archivo[random_num]:
        linea = archivo_abierto.readline()
        cont += 1
    
    archivo_abierto.close()

    linea_lista = linea.rstrip('\n').split(',')
    palabra = linea_lista[0]

    return palabra
    
def longitud_palabra_mas_larga(archivo_csv):
    """
    Se le pasa por parámetro el nombre del  archivo csv que contiene a todas las palabras cual y selecciona 
    de este cual es la palabra más larga, y lo que devuelve la función es la longitud de esta palabra.

    Autor: Franco Singh
    """
    archivo_abierto = open(archivo_csv)
    linea = archivo_abierto.readline()
    linea_lista = linea.rstrip('\n').split(',')
    long_mas_larga = 0
    while linea:
        palabra = linea_lista[0]
        if len(palabra) > long_mas_larga:
            long_mas_larga = len(palabra)
    
        linea = archivo_abierto.readline()
        linea_lista = linea.rstrip('\n').split(',')
    
    archivo_abierto.close()

    return long_mas_larga
