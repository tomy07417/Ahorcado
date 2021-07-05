
def leer_linea(archivo):
    """
    Esta funcion lee la una linea del archivo csv, y devuelve una lista con
    los valores de esa linea.

    Autor: Renata Pastorini

    """
    linea = archivo.readline()
    lista_linea = linea.rstrip('\n').split(',')
    
    return lista_linea
    
def configuracion_usuario():
    """
    Se crea un archivo csv en el que se guardan los datos para la implementación de la
    partida.
    
    Autor: Renata Pastorini
    """


    archivo_abierto = open("configuracion.csv","w")
    conf = input('¿Desea configurar los valores? (s/n): ')
    diccionario = {'MAX_USUARIOS': '',
                    'LONG_PALABRA_MIN': '',
                    'MAX_DESACIERTOS': '',
                    'PUNTOS_ACIERTOS': '',
                    'PUNTOS_DESACIERTOS': '',
                    'PUNTOS_ADIVINA_PALABRA': '',
                    'PUNTOS_RESTA_GANA_PROGRAMA': ''}

    if conf == 's':
        diccionario['MAX_USUARIOS'] = input('Maximo jugadores: ')
        diccionario['LONG_PALABRA_MIN'] = input('Longitud minima palabra: ')
        diccionario['MAX_DESACIERTOS'] = input('Maxima cantidad de desaciertos: ')
        diccionario['PUNTOS_ACIERTOS'] = input('Puntos a sumar por aciertos: ')
        diccionario['PUNTOS_DESACIERTOS'] = input('Puntos a restar por desacierto: ')
        diccionario['PUNTOS_ADIVINA_PALABRA'] = input('Puntos por adivinar la palabra: ')
        diccionario['PUNTOS_RESTA_GANA_PROGRAMA'] = input('Puntos a restar si gana la computadora: ')
    
    for clave in diccionario:
        valor = diccionario[clave]
        archivo_abierto.write( clave + ',' + valor + '\n') 
    
    archivo_abierto.close()

    return "configuracion.csv"

def configuracion():
    """
    Se toman los datos del archivo csv y se devuelve una lista con los valores numéricos 
    que se encunetran en el mismos.

    Autor: Renata Pastorini
    """
    nombre_archivo = configuracion_usuario()
    archivo_abierto = open(nombre_archivo)
    lista_linea = leer_linea(archivo_abierto)
    valores = [5,5,7,2,1,10,5]
    indice = 0
    diccionario = {'MAX_USUARIOS': 5,
                'LONG_PALABRA_MIN': 5,
                'MAX_DESACIERTOS': 7,
                'PUNTOS_ACIERTOS': 2,
                'PUNTOS_DESACIERTOS': 1,
                'PUNTOS_ADIVINA_PALABRA': 10,
                'PUNTOS_RESTA_GANA_PROGRAMA': 5}


    for clave in diccionario:
        valor = lista_linea[1]

        if valor != '':
            diccionario[clave] = ':  ' + valor + '; Valor asignado por configuración.'
            valores[indice] = int(valor)
        else:
            diccionario[clave] = ':  ' + str(diccionario[clave]) + '; Valor asignado por omisión.'


        lista_linea = leer_linea(archivo_abierto)
        indice += 1
    
    leer_configuracion(diccionario)
    
    return valores

def leer_configuracion(diccionario):
    """
    Muestra por pantalla los datos de la configuración.

    Autor: Renata Pastorini
    """

    for clave in diccionario:
        print(clave + ' ' + diccionario[clave])
    



