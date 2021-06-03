

def Calcular_palabra(palabra):
    xd = "?"*len(palabra)
    return xd

def Construir_palabra(datos):
    """
    Toma la palabra original, la palabra q tienen los "?" y letras que ya haya adivinado, y la letra q haya ingresado el usuario en la ultima carga; genera 
    una nueva palabra en la cual, se va a ir fijando en cada posicion de la palabra que tine q adivinar el 
    usuario, y si la letra de la palabra coincide con la letra que se ingresa por parametro, en la nueva palabra, se
    le va a asignar la letra, en cualquier otro caso, se le va a asignar la letra o en su defecto un "?", que 
    haya en la palabra con signos de pregunta
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

def letra_en_palabra(letra, palabra):
    return letra in palabra

def Ingreso_Valido(letra):
    """
    """
    resp = False
    if len(letra) == 1 and letra.isalpha():
        resp = True

    return resp

def agregar_letra_no_acertada(letras_no_acertadas, letra):
    
    if not letra in letras_no_acertadas :
        letras_no_acertadas += letra + " "
    
    return letras_no_acertadas


#NUEVO!!

def letra_ya_ingresada_y_es_valida(datos):
    resp = True
    resp = resp and datos["ingreso valido"]
    resp = resp and letra_en_palabra(datos["letra"], datos["palabra"])
    resp = resp and letra_en_palabra(datos["letra"], datos["palabra adivinando"])
    return resp

def procesar_letra_ingresada(datos):

    if datos["letra"] in datos["palabra"]:
        datos["palabra adivinando"] = Construir_palabra(datos)        
        datos["aciertos"] += 1
        datos["acertó"] = True
    elif not datos["letra"] in datos["letras no acertadas"]:
        #letra no ingresada y que no está en la palabra
        datos["letras no acertadas"] += datos["letra"] 
        datos["desaciertos"] +=1
    
    else: #para q no imprima mas de una vez una letra q no está en la palabra
        datos["desaciertos"] +=1


    return datos

def mostrar_en_pantalla(datos):
    if datos["acertó"]:
        print("Bien!! ->  ", end = " ")
        
    elif not datos["acertó"] and datos["ingreso valido"]:
        print("Lo siento!!! -> ", end = " ")
    
    else: # para la primera pasada: muestra los datos iniciales!
        print("Palabra a adivinar:", end = " ")

    print(datos["palabra adivinando"], end = "  ") 
    print("Aciertos:", datos["aciertos"], "  -   Desaciertos:", datos["desaciertos"], end = "  ")
    print("Letras no acertadas:", datos["letras no acertadas"])


    pass

def resultados(datos):
    if not "?" in datos["palabra adivinando"]:
        print("Bien!! Adivinaste la palabra!! <3 <3")

    else:
        print("La palabra era:", datos["palabra"])
    
    pass

def seguir(datos):
    resp = True
    resp = resp and   datos["desaciertos"] <= 7  
    resp = resp and    "?" in datos["palabra adivinando"] 
    resp = resp and   datos["seguir"] == "si"

    return resp



def juego(palabra):
    palabra_con_signos_de_pregunta = Calcular_palabra(palabra)
    datos = {"aciertos": 0, 
            "desaciertos": 0, 
            "palabra": palabra, 
            "palabra adivinando": palabra_con_signos_de_pregunta,
            "letras no acertadas": '',
            "seguir": "si",
            "letra": '',
            "acertó": '',
            "ingreso valido": ''
            }
        
    mostrar_en_pantalla(datos)

    while seguir(datos):

        datos["letra"] = input("Ingrese una letra (0 o FIN para terminar la partida): ").upper()
        datos["acertó"] = False
        datos["ingreso valido"] = Ingreso_Valido(datos["letra"])

        if letra_ya_ingresada_y_es_valida(datos):
        #el ingreso es valido, la letra está en la palabra a adivinar y ya la habías ingresado:
            print("La letra que queres ingresar ya fue ingresada, intenta con otra: ")
        
        elif datos["ingreso valido"]:
       #el ingreso es valido, la letra está en la palabra a adivinar y todavía no la habías ingresado:
           datos = procesar_letra_ingresada(datos)
        
        elif datos["letra"] == "FIN" or datos["letra"] == "0":
            datos["seguir"] = "no"
            print("Fin de la partida.")
        
        else:
            #el ingreso no es valido
            print("Debe ingresar una única letra.")
        
        mostrar_en_pantalla(datos)
        
    resultados(datos)
    
    puntos = datos["aciertos"] * 10 + datos["desaciertos"] * (-5)

    return puntos
    
