import validaciones, asignaciones


def mostrar_en_pantalla(datos, diccionario):
    '''
    Le muestra al usuario los datos por pantalla a lo largo de la jugada, 
    dependiendo el caso en el que se encuentre.
    
    Autor: Gonzalo Bacigalupo
    '''
    if datos['tipo de ingreso'] == 'primer ingreso' : 
        print('Palabra a adivinar:', end = ' ')
    
    elif datos['tipo de ingreso'] == True:

        print('Bien!! ->  ', end = ' ')
        
    elif datos['tipo de ingreso'] == False:

        print('Lo siento!!! -> ', end = ' ')


    print(diccionario['palabra_signos'], end = '  ') 
    print('Aciertos:', diccionario['aciertos'], '  -   Desaciertos:', diccionario['desaciertos'], end = '  ')
    print('Letras no acertadas:', diccionario['letras_no_acertadas'])

def resultados_parciales(jugadores, cant_partidas):
    """
    Al finalizar cada partida, se llama a esta función para que muestre los datos de la partida
    jugada.

    Autor: Gonzalo Bacigalupo
    """

    print('Cantidad de partidas jugadas: ', cant_partidas)
    for jugador in jugadores:
        print(jugador, 'tenía que adivinar la palabra:', jugadores[jugador]['palabra'], end = '')
        print('. En esta partida tuvo', jugadores[jugador]['aciertos'], 'aciertos y', jugadores[jugador]['desaciertos'], 'desaciertos.', end = ' ')
        print('Y el puntaje obtenido: ', jugadores[jugador]['puntos_parciales'])
        
        if cant_partidas > 1:
            
            print('El puntaje total obtenido: ', jugadores[jugador]['puntos_totales'])
            print('Los aciertos totales: ', jugadores[jugador]['aciertos_totales'])
            print('Los desaciertos totales: ', jugadores[jugador]['desaciertos_totales'])
            print('Adivinó: ', jugadores[jugador]['cant_palabras_adivinadas'] ,'palabra/s.')

def final_partida(jugadores, cant_partidas, PUNTOS_ADIVINA_PALABRA, PUNTOS_RESTA_GANA_PROGRAMA):
    """
    Dependiendo si alguno de los usuarios ganó, modifica de distinta manera los puntajes parciales, 
    y luego muestra todos los datos con la funcion anteriormente explicada.

    Autor: Gonzalo Bacigalupo
    """

    hubo_ganador = validaciones.gano_alguien(jugadores)     
    
    if hubo_ganador:
        ganador = asignaciones.el_ganador(jugadores)
        print('El ganador de esta partida es: ', ganador)
        jugadores[ganador]['puntos_parciales'] += PUNTOS_ADIVINA_PALABRA
        jugadores[ganador]['cant_palabras_adivinadas'] += 1
    
    else:
        print('Ganó la computadora')
        for jugador in jugadores:
            jugadores[jugador]['puntos_parciales'] -= PUNTOS_RESTA_GANA_PROGRAMA

    jugadores = asignaciones.puntajes_totales(jugadores)

    resultados_parciales(jugadores, cant_partidas)

    jugadores = asignaciones.reinicio_de_valores(jugadores)

    return jugadores

