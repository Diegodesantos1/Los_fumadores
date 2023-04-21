import threading
import time
import random
from colorama import Fore, Back, Style

papel = 0
tabaco = 1
filtros = 2
green = 3
cerillas = 4
num_fumadores = 5
ingredientes_necesarios = 5
mutex = threading.Lock()
ingredientes = [False] * ingredientes_necesarios
turno = threading.Event()
turno_fumador = threading.Event()
terminar_evento = threading.Event()

def poner_ingredientes():
    while not terminar_evento.is_set():
        ing1, ing2 = random.sample(range(ingredientes_necesarios), 2)
        print(f"Agente pone {ing1} y {ing2} en la mesa")
        ingredientes[ing1] = True
        ingredientes[ing2] = True
        turno.clear()
        turno_fumador.set()