import random   
import etapa_1
import etapa_2
import etapa_3
import etapa_7

from Texto import obtener_texto

def longitud(mas_larga):
    ingresar_longitud = input("¿Desea ingresar la longitud de la palabra a adivinar? (s/n): ")
    if ingresar_longitud == "s" :
        longitud_palabra = int(input("Ingrese la longitud de la palabra a adivinar, debe ser un valor entre 5 y " + str(mas_larga) + ": "))
    else:
        longitud_palabra = random.randint(5, mas_larga)
    
    return longitud_palabra

def asignar_palabras(jugadores, longitud_palabra, diccionarios):
    for jugador in jugadores:
            jugadores[jugador]['palabra'] = etapa_3.seleccion_palabra(diccionarios, longitud_palabra)
            jugadores[jugador]['palabra_signos'] = etapa_1.calcular_palabra(jugadores[jugador]['palabra'])
    
    return jugadores


def perdieron_todos(jugadores):
    resp = True
    for jugador in jugadores:
        resp = resp and jugadores[jugador]['perdio']
    
    return resp


def gano_alguien(jugadores):
    """
    depende lo q andy responda:
    si todos tiene q tener la posibilidad d adivinar la palabra, cambiar:
    resp = True

    y

    resp = resp and jugadores[jugador]['gano']

    ???
    """

    resp = False
    for jugador in jugadores:
        resp = resp or jugadores[jugador]['gano']
    
    return resp

def el_ganador(jugadores):
    """
    esta función se usa sabiendo de hay un gandor
    """
    for jugador in jugadores:
        if jugador['gano'] :
            ganador = jugador
    return ganador

def partida(jugadores, orden_jugadores):
    """
    depende lo q andy responda:
    si todos tiene q tener la posibilidad d adivinar la palabra, cambiar:
    
        and gano_alguien(jugadores)
        
    """

    turno = 0
    cant_jugadores = len(jugadores)
    while not (perdieron_todos(jugadores) or gano_alguien(jugadores)):
        jugador = orden_jugadores[turno]
        if jugadores[jugador]["desaciertos"] <= 7:
            print("Es el turno de jugar de: ", jugador)
            jugadores[jugador] = etapa_1.juego(jugadores[jugador])

        if turno == cant_jugadores-1 :
            turno = 0
        else:
            turno += 1

    pass



def final_partida(jugadores):
   
    hubo_ganador = gano_alguien(jugadores)
    if hubo_ganador:
        ganador = el_ganador(jugadores)


    for jugador in jugadores:
        print(jugador, "tenía que adivinar la palabra", jugador['palabra'], end = "")
        print(". Tuvo", jugador['aciertos'], "aciertos y", jugador['desaciertos'], "desaciertos.", end = "")
        print("El puntaje obtenido en la partida: ", jugador['puntos_parciales'])
    
    if jugador == ganador:
        print("El ganador es: ", ganador)
    
            

        









def main():
    jugadores = etapa_7.obtener_jugadores()
    orden_jugadores = etapa_7.mezclar_jugadores(jugadores)
    cant_partidas = 0
    jugar = "s"
    while jugar == "s" :
        texto = obtener_texto()
        diccionarios = etapa_2.crear_diccionario(texto)
        mas_larga = etapa_3.longitud_palabra_mas_larga(diccionarios)    
        longitud_palabra = longitud(mas_larga)
        jugadores = asignar_palabras(jugadores, longitud_palabra, diccionarios)
        
        partida(jugadores, orden_jugadores)

        final_partida(jugadores)


        cant_partidas += 1
        jugar = input("¿Quiere seguir jugando? (s/n): ")

        
 
        



print()