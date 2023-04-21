<h1 align = "center">Los fumadores</h1>

En este [repositorio](https://github.com/Diegodesantos1/Los_fumadores) quedan resuelto el problema de los fumadores.

EL código empleado para resolverlo es el siguiente:

<h2 align = "center">Fumadores completo</h2>

```python
import threading
import time
import random
from colorama import Fore, Back, Style


def ejecutar():
    diccionario = {0: "papel", 1: "tabaco",
                   2: "filtros", 3: "green", 4: "cerillas"}
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
            print(f"Fumador pone {diccionario[ing1]} y {diccionario[ing2]}")
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
```

<h2 align = "center">Fumadores simplificado</h2>

```python
import threading
import time
import random
from colorama import Fore, Back, Style


def ejecutar():
    diccionario = {0: "papel", 1: "tabaco",
                   2: "filtros", 3: "green", 4: "cerillas"}
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
```

<h2 align = "center">Lanzador</h2>

```python
import fumadores_completo as fumadores
import fumadores_simple as fumadores_simple
from introducir.numero import solicitar_introducir_numero_extremo
from os import system


def ejecutar():
    eleccion = solicitar_introducir_numero_extremo(
        "\n¿Qué versión quieres ejecutar? \n1: Completa \n2: Simplicada \n3: Terminar\n\n", 1, 3)
    if eleccion == 1:
        system("cls")
        fumadores.ejecutar()
        ejecutar()
    elif eleccion == 2:
        system("cls")
        fumadores_simple.ejecutar()
        ejecutar()
    elif eleccion == 3:
        exit()
```
