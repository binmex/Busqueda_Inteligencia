def imprimir_tablero(tablero):
    for fila in tablero:
        print(" | ".join(fila))
        print("-" * 13)

def movimiento_valido(tablero, movimiento):
    i, j = movimiento
    return 0 <= i < 3 and 0 <= j < 3 and tablero[i][j] == " "

def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True

def evaluar_estado(tablero):
    # Evaluación: +1 si un cuadrado es formado por X, -1 por O, 0 si empate
    for i in range(2):
        for j in range(2):
            if tablero[i][j] == tablero[i][j + 1] == tablero[i + 1][j] == tablero[i + 1][j + 1] == "X":
                return 1
            elif tablero[i][j] == tablero[i][j + 1] == tablero[i + 1][j] == tablero[i + 1][j + 1] == "O":
                return -1

    return 0

# Resto del código permanece igual


def minimax(tablero, profundidad, es_maximizando):
    puntuacion = evaluar_estado(tablero)

    if puntuacion == 1:
        return puntuacion - profundidad
    elif puntuacion == -1:
        return puntuacion + profundidad
    elif tablero_lleno(tablero):
        return 0

    if es_maximizando:
        mejor_valor = float("-inf")
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = "X"
                    valor = minimax(tablero, profundidad + 1, False)
                    tablero[i][j] = " "
                    mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        peor_valor = float("inf")
        for i in range(3):
            for j in range(3):
                if tablero[i][j] == " ":
                    tablero[i][j] = "O"
                    valor = minimax(tablero, profundidad + 1, True)
                    tablero[i][j] = " "
                    peor_valor = min(peor_valor, valor)
        return peor_valor

def movimiento_optimo(tablero):
    mejor_valor = float("-inf")
    mejor_movimiento = None

    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = "X"
                valor = minimax(tablero, 0, False)
                tablero[i][j] = " "

                # Agrega una penalización si bloquea una victoria del jugador O
                penalizacion = 0
                for a in range(3):
                    for b in range(3):
                        if tablero[a][b] == "O":
                            penalizacion += evaluar_estado(tablero)
                valor -= penalizacion

                if valor > mejor_valor:
                    mejor_valor = valor
                    mejor_movimiento = (i, j)

    return mejor_movimiento

def jugar_cuadrito():
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    while not tablero_lleno(tablero):
        imprimir_tablero(tablero)
        movimiento_usuario = tuple(map(int, input("Ingresa tu movimiento (fila y columna separadas por espacio): ").split()))

        if movimiento_valido(tablero, movimiento_usuario):
            tablero[movimiento_usuario[0]][movimiento_usuario[1]] = "O"
        else:
            print("Movimiento no válido. Intenta de nuevo.")
            continue

        if tablero_lleno(tablero):
            break

        movimiento_IA = movimiento_optimo(tablero)
        tablero[movimiento_IA[0]][movimiento_IA[1]] = "X"

        if evaluar_estado(tablero) == 1:
            imprimir_tablero(tablero)
            print("¡Has perdido! La IA gana.")
            break
        elif evaluar_estado(tablero) == -1:
            imprimir_tablero(tablero)
            print("¡Felicidades! Has ganado.")
            break

    if not evaluar_estado(tablero):
        imprimir_tablero(tablero)
        print("¡Es un empate!")

# Jugar el juego
jugar_cuadrito()
