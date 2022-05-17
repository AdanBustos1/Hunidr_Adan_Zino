import numpy as np
import random
def generar_barcos():
            tablero_base = np.full((10,10), ' ')
            while True:
                #Primero creamos un barco de 4 unidades
                eslora = 4
                #Orientacion del barco
                orient = random.choice(['N', 'S', 'E', 'O'])
                #Posicion inicial
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                # Recogemos las 4 posiciones colindantes a current_pos
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                # Comprobamos si esas posiciones son validas
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                #Ahora repetimos el proceso para crear 2 de 3 unidades
                eslora = 3
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                eslora = 3
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                #Ahora repetimos el proceso para crear 3 de 2 Unidades
                eslora = 2
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                eslora = 2
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                eslora = 2
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                #Ahora repetimos el proceso para crear 4 de 1 unidad
                eslora = 1
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                #Ahora repetimos el proceso para crear 4 de 1 unidad
                eslora = 1
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                #Ahora repetimos el proceso para crear 4 de 1 unidad
                eslora = 1
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            while True:
                #Ahora repetimos el proceso para crear 4 de 1 unidad
                eslora = 1
                orient = random.choice(['N', 'S', 'E', 'O'])
                current_pos = np.random.randint(10, size = 2)
                fila = current_pos[0]
                col = current_pos[1]
                coors_posiN = tablero_base[fila:fila - eslora:-1, col]
                coors_posiE = tablero_base[fila, col: col + eslora]
                coors_posiS = tablero_base[fila:fila + eslora, col]
                coors_posiO = tablero_base[fila, col: col - eslora:-1]
                if orient == 'N' and 0 <= fila - eslora < 10 and 'O' not in coors_posiN:
                    tablero_base[fila:fila - eslora:-1, col] = 'O'
                    break
                elif orient == 'E' and 0 <= col + eslora < 10 and 'O' not in coors_posiE:
                    tablero_base[fila, col: col + eslora] = 'O'
                    break
                elif orient == 'S' and 0 <= fila + eslora < 10 and 'O' not in coors_posiS:
                    tablero_base[fila:fila + eslora, col] = 'O'
                    break
                elif orient == 'O' and 0 <= col - eslora < 10 and 'O' not in coors_posiO:
                    tablero_base[fila, col: col - eslora:-1] = 'O'
                    break
                else:
                    continue
            return tablero_base













class hundirflota:
        tablero_jugador = generar_barcos()
        tablero_jugador_copia = np.full((10, 10), " ")
        tablero_enemigo = generar_barcos()
        tablero_enemigo_copia = np.full((10, 10), " ")
        

        

def dispara_enemigo():
            ok = True
            while ok == True:
                posiciony = random.randint(1,11)
                posicionx = random.randint(1,11)
                if hundirflota.tablero_jugador[posicionx-1:posicionx ,posiciony-1:posiciony] == " ":
                    hundirflota.tablero_enemigo_copia[posicionx-1:posicionx ,posiciony-1:posiciony] = '-'
                    hundirflota.tablero_jugador[posicionx-1:posicionx ,posiciony-1:posiciony] = '-'
                    print("El enemigo disparó al agua:", posicionx, posiciony,"\n",hundirflota.tablero_jugador)
                    ok = False
                elif hundirflota.tablero_jugador[posicionx-1:posicionx ,posiciony-1:posiciony] == "O":
                    hundirflota.tablero_enemigo_copia[posicionx-1:posicionx ,posiciony-1:posiciony] = 'x'
                    hundirflota.tablero_jugador[posicionx-1:posicionx ,posiciony-1:posiciony] = 'x'
                    print("El enemigo disparó a tu barco:", posicionx, posiciony,"\n",hundirflota.tablero_jugador)
                    ok = True
                else:
                    ok = True     
def dispara_jugador():
            ok = True
            while ok == True:
                posiciony = int(input('Introuce la posicion X:'))
                posicionx = int(input('Introuce la posicion Y:'))
                if hundirflota.tablero_enemigo[posicionx-1:posicionx ,posiciony-1:posiciony] == " ":
                    hundirflota.tablero_jugador_copia[posicionx-1:posicionx ,posiciony-1:posiciony] = '-'
                    hundirflota.tablero_enemigo[posicionx-1:posicionx ,posiciony-1:posiciony] = '-'
                    print("Tu disparo se fue al agua:","\n",hundirflota.tablero_jugador_copia)
                    ok = False
                elif hundirflota.tablero_enemigo[posicionx-1:posicionx ,posiciony-1:posiciony] == "O":
                    hundirflota.tablero_jugador_copia[posicionx-1:posicionx ,posiciony-1:posiciony] = 'x'
                    hundirflota.tablero_enemigo[posicionx-1:posicionx ,posiciony-1:posiciony] = 'x'
                    print("En el blanco, vuelve a disparar","\n",hundirflota.tablero_jugador_copia)
                    ok = True
                else:
                    print("esa casilla ya fue disparada")
                    ok = True
def comprobar_tablero():
            okk = True
            while okk == True :
                if "O" in hundirflota.tablero_enemigo:
                    okk = True
                    return okk
                elif "O" not in hundirflota.tablero_jugador:
                    okk = False
                    return okk
                else:
                    okk = False
                    return okk
            
                
def comprobar_ganador():
            if "O" in hundirflota.tablero_jugador:
                print("Adan siempre gana")
            elif "O" in hundirflota.tablero_enemigo:
                print("Adan se dejo ganar")