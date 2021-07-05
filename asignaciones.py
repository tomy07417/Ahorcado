import random, construccion_palabra, selecciones, validaciones


def asignar_longitud(LONG_PALABRA_MIN,mas_larga):
    """
    A través de esta función se le pregunta a el/los usuario/s si desean elegir la longitud
    de la palabra a elegir; en caso afirmativo, se pregunta cual es la longitud deseada entre los
    valores establecidos como minimo y maximo. Y en caso negativo, se toma un numero al azar entre el
    minimo y maximo.

    Autor: Tomás Amundarain
    """
    ingresar_longitud = input('¿Desea ingresar la longitud de la palabra a adivinar? (s/n): ')
    if ingresar_longitud == 's' :
        longitud_palabra = input('Ingrese la longitud de la palabra a adivinar, debe ser un valor entre '+ str(LONG_PALABRA_MIN) + ' y ' + str(mas_larga) + ': ')
        
        while not longitud_palabra.isnumeric() or not LONG_PALABRA_MIN <= int(longitud_palabra) <= mas_larga:
            longitud_palabra = input('Se debe ingresar un número entre '+ str(LONG_PALABRA_MIN) + ' y ' + str(mas_larga) + ': ')
        
        longitud_palabra = int(longitud_palabra)

    else:
        longitud_palabra = random.randint(LONG_PALABRA_MIN, mas_larga)
    
    return longitud_palabra

def asignar_palabras(jugadores, orden_jugadores, longitud_palabra, nombre_archivo):
    """
    Esta función le asigna una palabra a cada jugador con la longitud asignada.

    Autor: Tomás Amundarain
    """
    palabras = []
    N = len(orden_jugadores)
    indice = 0
    while indice < N:
        jugador = orden_jugadores[indice]
        palabra = selecciones.seleccion_palabra(nombre_archivo, longitud_palabra)
        
        
        if palabra not in palabras:
            jugadores[jugador]['palabra'] = palabra
            jugadores[jugador]['palabra_signos'] = construccion_palabra.calcular_palabra(palabra)
            palabras.append(palabra)
            indice += 1
    
    return jugadores

def reinicio_de_valores(jugadores):
    """
    A través de esta función se reinician los valores parciales utilizados en cada partida; los cuales son necesarios reiniciar 
    para el correcto funcionamiento en cada partida.

    Autor: Tomás Amundarain
    """
    for jugador in jugadores:

        jugadores[jugador]['aciertos'] = 0
        jugadores[jugador]['desaciertos'] = 0
        jugadores[jugador]['puntos_parciales'] = 0
        jugadores[jugador]['letras_acertadas'] = ''
        jugadores[jugador]['letras_no_acertadas'] = ''
        jugadores[jugador]['palabra'] = ''
        jugadores[jugador]['palabra_signos'] = ''
        jugadores[jugador]['letras_acertadas'] = ''
        jugadores[jugador]['perdio'] = False
        jugadores[jugador]['gano'] = False
    
    return jugadores

def el_ganador(jugadores):
    '''
    Esta función se usa sabiendo de hubo un ganador. Se devuelve el nombre 
    del usuario que adivinó la palabra.

    Autor: Tomás Amundarain 
    '''
    for jugador in jugadores:
        if jugadores[jugador]['gano'] :
            ganador = jugador
    
    return ganador

def nuevo_orden(orden_jugadores, jugadores):
    """
    A través de esta función se genera el orden en el que van a jugar los usuarios en una nueva partida.

    Autor: Tomás Amundarain
    """
     
    orden_jugadores = mezclar_jugadores(orden_jugadores)
    hubo_ganador = validaciones.gano_alguien(jugadores) 
   
    if hubo_ganador:
        ganador = el_ganador(jugadores)
        orden_jugadores.remove(ganador)
        orden_jugadores.insert(0, ganador)

    
    return orden_jugadores

def puntajes_totales(jugadores):
    """
    Con esta función se le suman a cada usuario los puntajes parciales obtenidos en la ultima partida, para así llevar el recuento de
    los puntos totales de todas las partidas.

    Autor: Tomás Amundarain
    """
    for jugador in jugadores:
        jugadores[jugador]['puntos_totales'] += jugadores[jugador]['puntos_parciales']

    return jugadores

def obtener_jugadores(CANT_MAX_JUGADORES):
    """
    Se le pasa por parametro la cantidad máxima de jugadores admitidos, para que los usuarios ingresen todos los nombres 
    deseados, hasta completar los cupos.

    Autor: Tomás Amundarain 
    """                                                        
    diccionario_jugadores = {}                                                  
     
    cargar_jugador = 's'                                                   
    while len(diccionario_jugadores) < CANT_MAX_JUGADORES and cargar_jugador != '': 
        cargar_jugador = input('Nombre del jugador: ').upper()                        
        if cargar_jugador != '':
            if cargar_jugador not in diccionario_jugadores:
                diccionario_jugadores[cargar_jugador] = {                           
                                'aciertos': 0,                                              
                                'desaciertos': 0,
                                'aciertos_totales': 0,                                              
                                'desaciertos_totales': 0,                                          
                                'puntos_totales': 0,                                        
                                'puntos_parciales': 0,                                      
                                'letras_acertadas':'',
                                'letras_no_acertadas' : '',                                     
                                'palabra': '', 
                                'palabra_signos' :'',
                                'perdio' : False,
                                'gano' : False,
                                'cant_palabras_adivinadas': 0                                      
                                } 
            else:
                print('El nombre no puede repetirse, ingresar otro nombre.')                                                         
    return diccionario_jugadores                                                

def mezclar_jugadores(jugadores):   
    """
    Se le pasa por parametro el listado de jugadores y esta función lo que hace es devolver la misma lista con los elementos 
    desordenados.

    Autor: Tomás Amundarain
    """                                                                                                                                                                           
    random.shuffle(jugadores)    

    return jugadores 

