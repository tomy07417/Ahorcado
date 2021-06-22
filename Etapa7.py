import random

def obtener_jugadores():
    diccionario_jugadores = {}
    CANT_MAX = 5
    cargar_jugador = 's' 

    while (len(diccionario_jugadores) < CANT_MAX and cargar_jugador != ''):
        cargar_jugador = input('Nombre del jugador: ')
        if cargar_jugador != '':
            diccionario_jugadores[cargar_jugador] = {
                    'aciertos': 0,
                    'desaciertos': 0,
                    'puntos_totales': 0,
                    'puntos_parciales': 0,
                    'letras_utilizadas':[],
                    'palabra':'',
                    'cant_adivinadas': 0
                    }
        
    return diccionario_jugadores

def mezclar_jugadores(diccionario):
    jugadores = list(diccionario.keys())
    random.shuffle(jugadores)
    return jugadores

