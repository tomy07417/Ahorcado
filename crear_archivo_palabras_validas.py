import re, os

def leer_linea(archivo, LONG_PALABRA_MIN):
    """
    Esta función lee una linea del archivo pasado por parametro, y devuelve dos valores: una 
    lista que contiene las palabras validas para ser asignadas a los usuarios, osea que cumplen 
    con la longitud mínima y no tienen ningún caracter especial ni acentos; así tambien se devuelve
    un valor booleano, el cual indica se llegó al final del archivo txt (si se le asigna True, es 
    porque no llegó al final; si se le asigna False es porque se llegó al final del archivo)


    Autor: Joaquin Altable
    """
    linea = archivo.readline()
    
    if linea:
        renglon = linea.rstrip('\n')
        renglon = palabras_validas(renglon, LONG_PALABRA_MIN)
        seguir = True
   
    else:
        renglon = []
        seguir = False
      

    return seguir, renglon

def palabras_validas(renglon, LONG_PALABRA_MIN):
    '''
    Esta función toma el renglon ingresado por parámetro, y devuelve una lista de palabras en la cual se 
    encuentran todas las palabras 'validas', osea aquellas que tienen longitud mayor o igual a LONG_PALABRA_MIN.

    Autor: Joaquin Altable
    '''

    lista_palabra_valida = []

    for palabra in re.split(' |-|_', renglon):
        palabra_sin = ''
        for letra in palabra:
            if letra.isalpha():
                palabra_sin += letra
        if len(palabra_sin) >= LONG_PALABRA_MIN:
            lista_palabra_valida.append(sacar_tildes(palabra_sin))

    return lista_palabra_valida

def sacar_tildes(palabra):
    '''
    Toma la cadena de caracteres ingresada, transforma en mayusculas todas las letras
    y se reemplazan las vocales que tienen tilde por las mismas pero sin la tilde. 

    Autor: Joaquin Altable
    '''
    palabra = palabra.upper()
    palabra_sin = ''
    diccionario = {'Á': 'A' , 'É': 'E' , 'Í': 'I', 'Ó': 'O' , 'Ú': 'U', 'Ü': 'U'} 
    
    for letra in palabra:
        if letra in diccionario:
            palabra_sin += diccionario[letra]
        else:
            palabra_sin += letra
    
    return palabra_sin

def crear_diccionario(lista_palabras, diccionario_palabras):
    '''
    Esta función genera un diccionario que contiene como claves las palabras que se encuentran en la 
    lista de palabras pasada por parametro, y que tiene como valor asociado la cantidad de veces que la 
    palabra aparece en el archivo que se esté evaluando en el momento.
    Éste diccionario NO está ordenado alfabéticamente.
    
    Autor: Joaquin Altable
    '''

    for palabra in lista_palabras:
        if palabra in diccionario_palabras:
            diccionario_palabras[palabra] += 1

        else:
            diccionario_palabras[palabra] = 1

    return diccionario_palabras

def unir_diccionarios(diccionarios):
    """
    Esta funcion toma los diccionarios que se crearon para cada archivo de texto y los une en un único diccionario
    el cual tiene como claves las palabras y como valor asociad una lista; esta lista tiene N elementos por los N archivos 
    de texto evaluados: en la iesima posicion de la lista figura la cantidad de veces que la palabra clave aparece en el 
    i-esimo archivo de texto.
    Este diccionario SI está ordenado alfabéticamente.

    Autor: Joaquin Altable
    """

    diccionario_completo = {}
    N = len(diccionarios)
    
    for indice in range(N):
        diccionario = diccionarios[indice]

        for palabra in diccionario:    
            valor = diccionario[palabra]

            if palabra in diccionario_completo:
                
                diccionario_completo[palabra][indice] += valor
            else:
                lista = []
                for j in range(N):
                    lista.append(0)
                
                diccionario_completo[palabra] = lista
                diccionario_completo[palabra][indice] += valor

    return dict(sorted(diccionario_completo.items(), key = lambda palabra: palabra[0]))

def crear_archivo(diccionario, cant_archivos):
    """
    Esta función toma el diccionario que contiene todas las palabras y lo pasa a un archivo csv.
    Y se devuelve el nombre de este archivo.

    Autor: Joaquin Altable
    """

    archivo = open("palabras.csv", "w")
    
    for palabra in diccionario:
        archivo.write(palabra)
        
        for indice in range(cant_archivos):
            dato = str(diccionario[palabra][indice] )
            archivo.write("," + dato)

        archivo.write("\n")

    archivo.close()
    
    return "palabras.csv"

def crear_archivo_palabras_validas(lista_archivos, LONG_PALABRA_MIN):
    """
    A esta función se le pasa por parametro una lista que contienen los nombres de 
    los archivos a analizar para la extracción de las palabras. Desde esta función se llama 
    a todas las anteriormente descriptas, para así crear el archivo csv que contiene las 
    palabras aptas para el juego y se devuelve el nombre del archivo creado.

    Autor: Joaquin Altable
    
    """
    diccionarios = []

    for archivo in lista_archivos:
        
        diccionario_palabras = {}
        archivo_abierto = open(os.path.join("./Archivos", archivo), encoding = "utf-8")        
        seguir, linea = leer_linea(archivo_abierto, LONG_PALABRA_MIN)

        while seguir:
            diccionario_palabras = crear_diccionario(linea, diccionario_palabras)
            seguir, linea = leer_linea(archivo_abierto, LONG_PALABRA_MIN)

        
        archivo_abierto.close()
        diccionarios.append(diccionario_palabras)
    
    diccionario = unir_diccionarios(diccionarios)

    cant_archivos = len(lista_archivos)
    
    nombre_archivo_csv = crear_archivo(diccionario, cant_archivos)

    return nombre_archivo_csv
    
