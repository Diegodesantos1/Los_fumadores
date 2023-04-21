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