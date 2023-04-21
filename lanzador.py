
import fumadores_completo as fumadores
import fumadores_simple as fumadores_simple
from introducir.numero import solicitar_introducir_numero_extremo


def ejecutar():
    eleccion = solicitar_introducir_numero_extremo(
        "\n¿Qué versión quieres ejecutar? \n1: Completa \n2: Simplicada \n3: Terminar\n", 1, 3)
    if eleccion == 1:
        fumadores.ejecutar()
        ejecutar()
    elif eleccion == 2:
        fumadores_simple.ejecutar()
        ejecutar()
    elif eleccion == 3:
        exit()
