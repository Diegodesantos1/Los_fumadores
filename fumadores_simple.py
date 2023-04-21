import threading
import time
import random
from colorama import Fore, Back, Style


def ejecutar():
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
    mostrar = True

    def poner_ingredientes():
        while not terminar_evento.is_set():
            ing1, ing2 = random.sample(range(ingredientes_necesarios), 2)
            ingredientes[ing1] = True
            ingredientes[ing2] = True
            turno.clear()
            turno_fumador.set()

    def fumar(num):
        while not terminar_evento.is_set():
            turno_fumador.wait()
            with mutex:
                if all(ingredientes):
                    print(
                        Fore.RED + f"Fumador {num} está fumando..." + Style.RESET_ALL)
                    time.sleep(3)
                    ingredientes[0] = ingredientes[1] = ingredientes[2] = ingredientes[3] = ingredientes[4] = False
                    print(
                        Fore.RED + f"Fumador {num} ha terminado de fumar" + Style.RESET_ALL)
                    turno.set()
                    time.sleep(3)
                turno_fumador.clear()

    hilos = [threading.Thread(target=fumar, args=(i,))
             for i in range(num_fumadores)]
    hilo_principal = threading.Thread(target=poner_ingredientes)

    for hilo in hilos:
        hilo.start()

    hilo_principal.start()
    time.sleep(10)
    terminar_evento.set()
    hilo_principal.join()

    for hilo in hilos:
        hilo.join()


if __name__ == '__main__':
    ejecutar()
