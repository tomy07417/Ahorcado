import etapa_1
import etapa_2
import etapa_3

from Texto import obtener_texto

def main():
    jugar = "s"
    puntos = 0
    while jugar == "s" :
        texto = obtener_texto()
        diccionarios = etapa_2.crear_diccionario(texto)
        palabra = etapa_3.seleccion_palabra(diccionarios)
        print(palabra)
        puntos += etapa_1.juego(palabra)
        jugar = input("¿Quiere seguir jugando? (s/n): ")
    
    if puntos > 0 :
        
        print("Bien!! -> Tu puntaje es: ", puntos)
    
    else:

        print("Dedicate a otra cosa, tu puntaje es: ", puntos)


main()

