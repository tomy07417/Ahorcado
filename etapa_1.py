

def Calcular_palabra(palabra):
    xd = "?"*len(palabra)
    return xd

def Construir_palabra(palabra_a_adivinar, palabra_con_signos_de_pregunta, letra):
    palabra_nueva = ''
    for i in range(len(palabra_con_signos_de_pregunta)):
        if palabra_a_adivinar[i] == letra:
            palabra_nueva += letra
        else:
            palabra_nueva += palabra_con_signos_de_pregunta[i]

    return palabra_nueva


def Es_repetida(letras_ingresadas, letra):
    return letra in letras_ingresadas



def Existe_letra(letra, palabra):
    return letra in palabra


def Ingreso_Valido(letra):
    resp = False
    if len(letra) == 1 and letra.isalpha():
        resp = True

    return resp


def agregar_letra_no_acertada(letras_no_acertadas, letra):
    if not letra in letras_no_acertadas :
        letras_no_acertadas += letra + " "
    
    return letras_no_acertadas


def juego(palabra_a_adivinar):
    acierto_desacierto = [0,0]
    palabra_con_signos_de_pregunta = Calcular_palabra(palabra_a_adivinar)
    letras_no_acertadas = " "
    seguir = "si"
    print("Palabra a adivinar:", palabra_con_signos_de_pregunta, end = "    ")
    print("Aciertos:", acierto_desacierto[0], "  -  Desaciertos:", acierto_desacierto[1]) 

    while acierto_desacierto[1] <= 7  and  "?" in palabra_con_signos_de_pregunta and seguir == "si":
        letra = input("Ingrese una letra (0 o FIN para terminar la partida): ").upper()
        
        if not Ingreso_Valido(letra):
            if letra == "FIN" or letra == "0":
                seguir = "no"
                print("Fin de la partida.")
            else:
               print("Debe ingresar una única letra.")
      
        else:
           if Existe_letra(letra, palabra_a_adivinar):

               if Es_repetida(palabra_con_signos_de_pregunta, letra):
                
                   print("La letra que queres ingresar ya fue ingresada, intenta con otra: ")

               else: 
                    palabra_con_signos_de_pregunta = Construir_palabra(palabra_a_adivinar, palabra_con_signos_de_pregunta, letra)
                    acierto_desacierto[0] += 1

                    print("Bien!! ->  ", palabra_con_signos_de_pregunta, end = "  ") 
                    print("Aciertos:", acierto_desacierto[0], "  -   Desaciertos:", acierto_desacierto[1], end = "  ")
                    print("Letras no acertadas:", letras_no_acertadas)

           else:
               acierto_desacierto[1] += 1
               letras_no_acertadas = agregar_letra_no_acertada(letras_no_acertadas, letra)
               print("Lo siento!!! ->  ", palabra_con_signos_de_pregunta, end = "     ") 
               print("Aciertos:", acierto_desacierto[0], " -  Desaciertos:", acierto_desacierto[1], end = " ;  ")
               print("Letras no acertadas:", letras_no_acertadas)
    
    if acierto_desacierto[1] == 8 :

        print("La palabra era:", palabra_a_adivinar)

    else:

        print("Bien!! Adivinaste la palabra!! <3 <3")


    puntos = acierto_desacierto[0] * 10 + acierto_desacierto[1] * (-5)

    return puntos

