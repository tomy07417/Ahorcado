import validaciones, mostrar_datos, construccion_palabra, asignaciones, Texto, validacion_texto

def juego(diccionario):
    '''
    Esta función es el juego en sí, pide el ingreso de letras y las
    evalua, para devolver el puntaje correspondiente a los ingresos que se hacen.
    
    Autor: Renata Pastorini
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
            dato = construccion_palabra.procesar_letra_ingresada(datos, diccionario)
            datos = dato[0]
            diccionario = dato[1]


        else:   
            datos['tipo de ingreso'] = 'ingreso invalido'
            print('Ingreso invalido, debe ingresar una única letra! -> ', end = ' ')

        mostrar_datos.mostrar_en_pantalla(datos, diccionario)
        print('') 
    
    if not '?' in diccionario['palabra_signos']:
        diccionario['gano'] = True
    
    if diccionario['desaciertos'] == 8 :
        diccionario['perdio'] = True
 
    return diccionario

def partida(jugadores, orden_jugadores):
    '''
    depende lo q andy responda:
    si todos tiene q tener la posibilidad d adivinar la palabra, cambiar:
    
        and gano_alguien(jugadores)
        
    '''

    turno = 0
    cant_jugadores = len(jugadores)
    while not (validaciones.perdieron_todos(jugadores) or validaciones.gano_alguien(jugadores)):
        jugador = orden_jugadores[turno]

        if jugadores[jugador]['desaciertos'] <= 7:
            print('Es el turno de jugar de: ', jugador)
            jugadores[jugador] = juego(jugadores[jugador])

        if turno == cant_jugadores-1 :
            turno = 0
        else:
            turno += 1

    return jugadores
        
def main():
    jugadores = asignaciones.obtener_jugadores()
    orden_jugadores = asignaciones.mezclar_jugadores(jugadores)
    cant_partidas = 0
    jugar = 's'
    
    while jugar == 's' :    
        texto = Texto.obtener_texto()
        diccionarios = validacion_texto.crear_diccionario(texto)
        mas_larga = asignaciones.longitud_palabra_mas_larga(diccionarios)    
        longitud_palabra = asignaciones.longitud(mas_larga)
        jugadores = asignaciones.asignar_palabras(jugadores, orden_jugadores, longitud_palabra, diccionarios)
        
        jugadores = partida(jugadores, orden_jugadores)
        cant_partidas += 1
        
        orden_jugadores = asignaciones.nuevo_orden(orden_jugadores, jugadores)

        jugadores = mostrar_datos.final_partida(jugadores, cant_partidas)

        

        jugar = input('¿Quiere seguir jugando? (s/n): ')

        
main()