import etapa_1
import etapa_2
import etapa_3
from Texto import obtener_texto

def main():
    '''
    Esta función es un complemento a la función juego de la etapa 1,
    se genera el diccionario, se elige la palabra a adivinar de éste y
    se suman los puntos de cada partida jugada, si es que se juega más de una vez.
    
    Autor: Joaquin Altable
    '''

    jugar = "s"
    puntos = 0
    while jugar == "s" :
        texto = obtener_texto()
        diccionarios = etapa_2.crear_diccionario(texto)
        palabra = etapa_3.seleccion_palabra(diccionarios)
        puntos += etapa_1.juego(palabra)
        jugar = input("¿Quiere seguir jugando? (s/n): ")
    
    if puntos > 0 :
        print("Bien!! -> Tu puntaje es: ", puntos)
    
    else:
        print("Dedicate a otra cosa, tu puntaje es: ", puntos)
    
main()
