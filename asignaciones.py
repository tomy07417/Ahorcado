import random, construccion_palabra, asignaciones, validaciones


def longitud(mas_larga):
    ingresar_longitud = input('¿Desea ingresar la longitud de la palabra a adivinar? (s/n): ')
    if ingresar_longitud == 's' :
        longitud_palabra = int(input('Ingrese la longitud de la palabra a adivinar, debe ser un valor entre 5 y ' + str(mas_larga) + ': '))
    else:
        longitud_palabra = random.randint(5, mas_larga)
    
    return longitud_palabra

def seleccion_palabra(diccionario, longitud):
    lista_palabras = list(diccionario.keys())
    lista_palabras_longitud = []
    resp = ''
    for i in range (len(lista_palabras)):
        if len(lista_palabras[i]) == longitud:
            lista_palabras_longitud.append(lista_palabras[i]) 
    
    random_num = random.randint(0, len(lista_palabras_longitud) - 1)

    resp += lista_palabras_longitud[random_num]

    return resp
    
def longitud_palabra_mas_larga(diccionario):
    lista = list(diccionario)
    mas_larga = lista[0]
    resp = 0
    for palabra in lista:
        if len(mas_larga) < len(palabra):
            mas_larga = palabra
    
    resp = len(mas_larga)

    return resp

def asignar_palabras(jugadores, orden_jugadores, longitud_palabra, diccionarios):
    palabras = []
    n = len(orden_jugadores)
    i = 0
    while i < n:
        jugador = orden_jugadores[i]
        palabra = seleccion_palabra(diccionarios, longitud_palabra)
        
        
        if palabra not in palabras:
            jugadores[jugador]['palabra'] = palabra
            jugadores[jugador]['palabra_signos'] = construccion_palabra.calcular_palabra(palabra)
            palabras.append(palabra)
            i += 1
    
    return jugadores

def reinicio_de_valores(jugadores):

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
    
def nuevo_orden(orden_jugadores, jugadores):
    print(orden_jugadores)

    orden_jugadores = asignaciones.mezclar_jugadores(jugadores)
    hubo_ganador = validaciones.gano_alguien(jugadores) 
   
    if hubo_ganador:
        ganador = validaciones.el_ganador(jugadores)
        orden_jugadores.remove(ganador)
        orden_jugadores.insert(0, ganador)

    print(orden_jugadores)    
    return orden_jugadores

def puntajes_totales(jugadores):
    
    for jugador in jugadores:
        jugadores[jugador]['puntos_totales'] += jugadores[jugador]['puntos_parciales']

    return jugadores

def obtener_jugadores():                                                        
    diccionario_jugadores = {}                                                  
    CANT_MAX = 5 
    cargar_jugador = 's'                                                   
    while (len(diccionario_jugadores) < CANT_MAX and cargar_jugador != ''): 
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

def mezclar_jugadores(diccionario):                                                                                         
    jugadores = list(diccionario.keys())                                                                                    
    random.shuffle(jugadores)                                                                                               
    return jugadores 
