
def ingreso_valido(letra):
    '''
    La función toma el ingreso del usuario y se fija si es una única letra.
    
    Autor: Franco Singh
    '''
    resp = False
    if len(letra) == 1 and letra.isalpha():
        resp = True

    return resp

def letra_en_cadena(letra, palabra):
    '''
    Comprueba si la letra está en la palabra.
    
    Autor: Franco Singh
    '''
    return letra in palabra

def letra_ya_ingresada_y_es_valida(datos, diccionario):
    '''
    La función determina si el ingreso es valido y si está en la palabra que contiene los signos de
    interrogación.

    Autor: Franco Singh
    '''
    resp = datos['ingreso valido']
    resp = resp and letra_en_cadena(datos['letra'], diccionario['palabra_signos'])
    return resp

def seguir(datos, diccionario):
    '''
    Devuelve un booleano, el cual es verdadero si el usuario que actualmente está jugando,
    tiene que seguir ingresando valoreso, o falso en caso de que se tenga que pasar al siguiente 
    jugador.

    Autor: Franco Singh
    '''
    resp = diccionario['desaciertos'] == datos['desaciertos']  

    resp = resp and  '?' in diccionario['palabra_signos'] 

    return resp

def perdieron_todos(jugadores):
    '''
    Esta función determina si todos los jugadores perdieron.
    
    Autor: Franco Singh
    '''
    resp = True
    for jugador in jugadores:
        resp = resp and jugadores[jugador]['perdio']
    
    return resp

def gano_alguien(jugadores):
    '''
    Esta función determina si al menos unos de los jugadores adivinó la palabra.
    
    Autor: Franco Singh
    '''

    resp = False
    for jugador in jugadores:
        resp = resp or jugadores[jugador]['gano']
    
    return resp



