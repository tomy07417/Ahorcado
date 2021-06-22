

def calcular_palabra(palabra):
    '''
    Toma la palabra que se tiene que adivinar y con la longitud de esa palabra
    se genera una cadena que tenga por caracteres únicamente signos de interrogación.
    
    Autor: Pablo Dominguez
    '''
    palabra_adivinando = "?"*len(palabra)

    return palabra_adivinando

def construir_palabra(datos):
    """
    Esta función reemplaza los signos de interrogación por la letra ingresada por el usuario.
    
    Autor: Pablo Dominguez
    """
    palabra_a_adivinar = datos["palabra"]
    palabra_con_signos_de_pregunta = datos["palabra adivinando"]
    letra = datos["letra"]

    palabra_nueva = ''
    for i in range(len(palabra_con_signos_de_pregunta)):
        if palabra_a_adivinar[i] == letra:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra_con_signos_de_pregunta[i]

    return palabra_nueva

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
    resp = datos["ingreso valido"]
    resp = resp and letra_en_cadena(datos["letra"], diccionario["palabra_signos"])
    return resp



def mostrar_en_pantalla(datos, diccionario):
    '''
    Le muestra al usuario los datos por pantalla, dependiendo el caso en el que se encuentre.
    
    Autor: Gonzalo Bacigalupo
    '''
    if datos["tipo de ingreso"] == 'primer ingreso' : 
        print("Palabra a adivinar:", end = " ")
    
    elif datos["tipo de ingreso"] == True:

        print("Bien!! ->  ", end = " ")
        
    elif datos["tipo de ingreso"] == False:

        print("Lo siento!!! -> ", end = " ")
    


    print(diccionario["palabra_signos"], end = "  ") 
    print("Aciertos:", diccionario["aciertos"], "  -   Desaciertos:", diccionario["desaciertos"], end = "  ")
    print("Letras no acertadas:", diccionario["letras_no_acertadas"])


def procesar_letra_ingresada(datos, diccionario):
    '''
    Modifica los datos del diccionario datos según corresponda, ya sea que se ingresó una letra
    que está en la palabra a adivinar, si es una letra que no está en la palabra o si es una letra
    que ya fue ingresada y que no se encuentra en la palabra.
    
    Autor: Gonzalo Bacigalupo   
    '''
    if letra_en_cadena(datos["letra"],diccionario["palabra"]):
        diccionario["palabra_signos"] = construir_palabra(datos)        
        diccionario["aciertos"] += 1
        diccionario["letras_acertadas"] += (datos["letra"])
        datos["tipo de ingreso"] = True

    elif not letra_en_cadena(datos["letra"], datos["letras no acertadas"]):
        diccionario["letras_no_acertadas"] += datos["letra"]
        diccionario["desaciertos"] += 1
    
    else: 
        diccionario["desaciertos"] += 1
    
    resp = (datos, diccionario)
    
    return resp



def seguir(datos, diccionario):
    '''
    Devuelve un booleano, que depende de los datos que se toman del diccionario 
    "datos".

    Autor: Franco Singh
    '''
    resp = diccionario["desaciertos"] != datos["desaciertos"]  
    resp = resp and  "?" in diccionario["palabra_signos"] 

    return resp


def juego(diccionario):
    '''
    Esta función es el juego en sí, pide el ingreso de letras y las
    evalua, para devolver el puntaje correspondiente a los ingresos que se hacen.
    
    Autor: Renata Pastorini
    '''

    datos = {"letra": '',
            "tipo de ingreso": 'primer ingreso',
            "ingreso valido": '',
            "desaciertos": diccionario["desaciertos"]
            }
        
    mostrar_en_pantalla(datos)

    while seguir(datos):

        datos["letra"] = input("Ingrese una letra: ").upper()
        datos["tipo de ingreso"] = False
        datos["ingreso valido"] = ingreso_valido(datos["letra"])

        if letra_ya_ingresada_y_es_valida(datos, diccionario): 
            datos["tipo de ingreso"] = 'letra ya ingresada'
            print("La letra que queres ingresar ya fue ingresada!! -> ", end = " ")
            
        elif datos["ingreso valido"]: 
            dato =  procesar_letra_ingresada(datos, diccionario)
            datos = dato[0]
            datos = dato[1]


        else:   
            datos["tipo de ingreso"] = 'ingreso invalido'
            print("Ingreso invalido, debe ingresar una única letra! -> ", end = " ")
        
        
        mostrar_en_pantalla(datos)
        print('') 


    
    return diccionario
    



