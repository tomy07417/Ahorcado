import etapa_1
import etapa_2
import etapa_3
import Etapa7

from Texto import obtener_texto

def main():
    jugadores = Etapa7.obtener_jugadores()
    orden_jugadores = Etapa7.mezclar_jugadores(jugadores)

    jugar = "s"
    while jugar == "s" :
        texto = obtener_texto()
        diccionarios = etapa_2.crear_diccionario(texto)
        
        longitud_palabra = int(input("Ingrese la longitud de la palabra a adivinar, debe ser un valor entre 5 y " + str(etapa_3.longitud_palabra_mas_larga(diccionarios)) + ": "))
        palabra = etapa_3.seleccion_palabra(diccionarios, longitud_palabra)
        
main()

