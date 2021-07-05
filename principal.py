import os, validaciones, mostrar_datos, construccion_palabra, asignaciones, selecciones, configuracion 

from crear_archivo_palabras_validas import crear_archivo_palabras_validas

lista_de_archivos = os.listdir("./Archivos")
CANT_MAX_JUGADORES, LONG_PALABRA_MIN, MAX_DESACIERTOS, PUNTOS_ACIERTOS, PUNTOS_DESACIERTOS, PUNTOS_ADIVINA_PALABRA, PUNTOS_RESTA_GANA_PROGRAMA = configuracion.configuracion()

def juego(diccionario):
    '''
    Esta función es el juego en sí, pide el ingreso de letras y las
    evalua, para devolver el diccionario que contiene los datos de cada jugador 
    modificado según correspondan.
    
    Autor: Gonzalo Bacigalupo
    '''

    datos = {'letra': '',
            'tipo de ingreso': 'primer ingreso',
            'ingreso valido': '',
            'desaciertos': diccionario['desaciertos']
            }

    mostrar_datos.mostrar_en_pantalla(datos, diccionario)

    while validaciones.seguir(datos, diccionario):

        datos['letra'] = input('Ingrese una letra: ').upper()
        datos['tipo de ingreso'] = False
        datos['ingreso valido'] = validaciones.ingreso_valido(datos['letra'])

        if validaciones.letra_ya_ingresada_y_es_valida(datos, diccionario): 
            datos['tipo de ingreso'] = 'letra ya ingresada'
            print('La letra que queres ingresar ya fue ingresada!! -> ', end = ' ')
            
        elif datos['ingreso valido']: 
            dato = construccion_palabra.procesar_letra_ingresada(datos, diccionario, PUNTOS_ACIERTOS, PUNTOS_DESACIERTOS)
            datos = dato[0]
            diccionario = dato[1]


        else:   
            datos['tipo de ingreso'] = 'ingreso invalido'
            print('Ingreso invalido, debe ingresar una única letra! -> ', end = ' ')

        mostrar_datos.mostrar_en_pantalla(datos, diccionario)
        print('') 
    
    if not '?' in diccionario['palabra_signos']:
        diccionario['gano'] = True
    
    if diccionario['desaciertos'] == MAX_DESACIERTOS :
        diccionario['perdio'] = True
 
    return diccionario

def partida(jugadores, orden_jugadores):
    '''
    Esta función utiliza la función juego para que cada jugador pueda ingresar valores por pantalla, llevando a cabo
    una partida, la cual va a ejecutarse hasta que algun usuario adivine la palabra o hasta que todos lleguen al máximo de
    desaciertos.

    Autor: Gonzalo Bacigalupo
    '''

    turno = 0
    cant_jugadores = len(jugadores)
    while not (validaciones.perdieron_todos(jugadores) or validaciones.gano_alguien(jugadores)):
        jugador = orden_jugadores[turno]
        
        if jugadores[jugador]['desaciertos'] < MAX_DESACIERTOS:
            print('Es el turno de jugar de: ', jugador)
            
            jugadores[jugador] = juego(jugadores[jugador])

        if turno == cant_jugadores-1 :
            turno = 0
        else:
            turno += 1

    return jugadores
        
def main():
    """
    Esta función genera todos los valores iniciales y le solicita al usuario los datos necesarios
    para que el juego empiece a ejecutarse, hasta que ya no se desee jugar más, terminando así el juego para
    todos los usuarios.

    Autor: Gonzalo Bacigalupo
    """

    print("El máximo de jugadores es:", CANT_MAX_JUGADORES)
    jugadores = asignaciones.obtener_jugadores(CANT_MAX_JUGADORES)
    lista_jugadores = list(jugadores.keys())
    orden_jugadores = asignaciones.mezclar_jugadores(lista_jugadores)

    nombre_archivo_palabras = crear_archivo_palabras_validas(lista_de_archivos, LONG_PALABRA_MIN)
    
    cant_partidas = 0
    jugar = 's'
    
    while jugar == 's' :
        
        mas_larga = selecciones.longitud_palabra_mas_larga(nombre_archivo_palabras) 
        longitud_palabra = asignaciones.asignar_longitud(LONG_PALABRA_MIN, mas_larga)
        jugadores = asignaciones.asignar_palabras(jugadores, orden_jugadores, longitud_palabra, nombre_archivo_palabras)
        
        jugadores = partida(jugadores, orden_jugadores)
        cant_partidas += 1
        
        jugadores = mostrar_datos.final_partida(jugadores, cant_partidas, PUNTOS_ADIVINA_PALABRA, PUNTOS_RESTA_GANA_PROGRAMA)

        orden_jugadores = asignaciones.nuevo_orden(orden_jugadores, jugadores)

        jugar = input('¿Quiere seguir jugando? (s/n): ')

        
main()
