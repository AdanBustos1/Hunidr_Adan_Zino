import numpy as np
import random
from funciones import generar_barcos, hundirflota, comprobar_tablero, comprobar_ganador, dispara_jugador, dispara_enemigo
import funciones

from funciones import  hundirflota
print("Bienvenido a Hundir la flota, el juego es sencillo, serás tu VS la maquina. Cada turno tiene que disparar al tablero enemigo e intentar hundir sus barcos y el enemigo hará lo mismo. ¡SUERTE!")
opcion = int(input("escoge 1)jugar o 2)salir:"))
if opcion == 1:
    while comprobar_tablero() == True:
        print(hundirflota.tablero_enemigo)
        dispara_jugador()
        dispara_enemigo()
    comprobar_ganador()
elif opcion == 2:
    print("GUD VAI AMIGOOOO")

