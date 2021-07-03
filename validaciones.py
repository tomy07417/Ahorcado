

def ingreso_valido(letra):
    '''
    La función toma el ingreso del usuario y se fija si es una única letra.
    
    Autor: Pablo Dominguez
    '''
    resp = False
    if len(letra) == 1 and letra.isalpha():
        resp = True

    return resp

def letra_en_cadena(letra, palabra):
    '''
    Comprueba si la letra está en la palabra.
    
    Autor: Pablo Dominguez
    '''
    return letra in palabra

def letra_ya_ingresada_y_es_valida(datos, diccionario):
    '''
    La función determina si el ingreso es valido y si está en la palabra que contiene los signos de
    interrogación.

    Autor: Gonzalo Bacigalupo
    '''
    resp = datos['ingreso valido']
    resp = resp and letra_en_cadena(datos['letra'], diccionario['palabra_signos'])
    return resp

def seguir(datos, diccionario):
    '''
    Devuelve un booleano, que depende de los datos que se toman del diccionario 
    'datos'.

    Autor: Franco Singh
    '''
    resp = diccionario['desaciertos'] == datos['desaciertos']  
            # si los desaciertos son iguales en ambos diccionarios, significa q no se equivocó 
            # en lo q va d su turno, por lo q puede seguir jugando
    resp = resp and  '?' in diccionario['palabra_signos'] 

    return resp

def perdieron_todos(jugadores):
    '''
    si todos los judaores perdieron: la función va a devolver True
    '''
    resp = True
    for jugador in jugadores:
        resp = resp and jugadores[jugador]['perdio']
    
    return resp

def gano_alguien(jugadores):
    '''
    La funcion devulve: True si alguien ganó
    '''

    resp = False
    for jugador in jugadores:
        resp = resp or jugadores[jugador]['gano']
    
    return resp

def el_ganador(jugadores):
    '''
    esta función se usa sabiendo de hay un gandor!
    '''
    for jugador in jugadores:
        if jugadores[jugador]['gano'] :
            ganador = jugador
    
    return ganador

