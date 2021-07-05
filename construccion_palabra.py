import validaciones

def calcular_palabra(palabra):
    '''
    Toma la palabra que se tiene que adivinar y con la longitud de esa palabra
    se genera una cadena que tenga por caracteres únicamente signos de interrogación.
    
    Autor: Pablo Dominguez
    '''
    palabra_adivinando = '?'*len(palabra)

    return palabra_adivinando

def construir_palabra(datos, diccionario):
    '''
    Esta función reemplaza los signos de interrogación por la letra ingresada por el usuario.
    
    Autor: Pablo Dominguez
    '''
    palabra_a_adivinar = diccionario['palabra']
    palabra_con_signos_de_pregunta = diccionario['palabra_signos']
    letra = datos['letra']

    palabra_nueva = ''
    for i in range(len(palabra_con_signos_de_pregunta)):
        if palabra_a_adivinar[i] == letra:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra_con_signos_de_pregunta[i]

    return palabra_nueva

def procesar_letra_ingresada(datos, diccionario, PUNTOS_ACIERTOS, PUNTOS_DESACIERTOS):
    '''
    Modifica los datos de los diccionarios "datos" y "diccionario" según corresponda, ya sea que se ingresó una letra
    que está en la palabra a adivinar, si es una letra que no está en la palabra o si es una letra
    que ya fue ingresada y que no se encuentra en la palabra.
    
    Autor: Pablo Dominguez 
    '''

    if validaciones.letra_en_cadena(datos['letra'],diccionario['palabra']):
        diccionario['palabra_signos'] = construir_palabra(datos, diccionario)       
        diccionario['aciertos'] += 1
        diccionario['aciertos_totales'] += 1
        diccionario['puntos_parciales'] += PUNTOS_ACIERTOS
        diccionario['letras_acertadas'] += (datos['letra'])
        datos['tipo de ingreso'] = True

    elif not validaciones.letra_en_cadena(datos['letra'], diccionario['letras_no_acertadas']):
        diccionario['letras_no_acertadas'] += datos['letra']
        diccionario['desaciertos'] += 1
        diccionario['desaciertos_totales'] += 1
        diccionario['puntos_parciales'] -= PUNTOS_DESACIERTOS
    
    else: 
        diccionario['desaciertos'] += 1
        diccionario['desaciertos_totales'] += 1
        diccionario['puntos_parciales'] -= PUNTOS_DESACIERTOS
    
    resp = (datos, diccionario)
    
    return resp  