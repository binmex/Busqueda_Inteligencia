# Definir el tablero como una lista de 9 elementos
tablero = [" ", " ", " ",
           " ", " ", " ",
           " ", " ", " "]

# Definir las posiciones ganadoras como una lista de tuplas
ganadoras = [(0, 1, 2), (3, 4, 5), (6, 7, 8), # Horizontales
             (0, 3, 6), (1, 4, 7), (2, 5, 8), # Verticales
             (0, 4, 8), (2, 4, 6)] # Diagonales

# Definir los símbolos de los jugadores
jugador = "X"
oponente = "O"

# Definir una función para mostrar el tablero
def mostrar_tablero():
    print(tablero[0] + "|" + tablero[1] + "|" + tablero[2])
    print("-+-+-")
    print(tablero[3] + "|" + tablero[4] + "|" + tablero[5])
    print("-+-+-")
    print(tablero[6] + "|" + tablero[7] + "|" + tablero[8])

# Definir una función para comprobar si el tablero está lleno
def tablero_lleno():
    return " " not in tablero

# Definir una función para comprobar si hay un ganador
def hay_ganador():
    for a, b, c in ganadoras:
        if tablero[a] == tablero[b] == tablero[c] != " ":
            return tablero[a]
    return None

# Definir una función para evaluar el estado del tablero
def evaluar():
    ganador = hay_ganador()
    if ganador == jugador:
        return 10
    elif ganador == oponente:
        return -10
    else:
        return 0

# Definir una función para implementar el algoritmo de min-max
def min_max(es_max):
    # Si el juego ha terminado, devolver el valor del tablero
    valor = evaluar()
    if valor != 0:
        return valor
    if tablero_lleno():
        return 0
    # Si es el turno del jugador que maximiza, elegir el mayor valor posible
    if es_max:
        mejor_valor = -float("inf") #valor muy pequeño que siempre es negativo -1000
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = jugador #computadora
                valor = min_max(False)
                tablero[i] = " "
                mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    # Si es el turno del jugador que minimiza, elegir el menor valor posible
    else:
        mejor_valor = float("inf")
        for i in range(9):
            if tablero[i] == " ":
                tablero[i] = oponente
                valor = min_max(True)
                tablero[i] = " "
                mejor_valor = min(mejor_valor, valor)
        return mejor_valor

# Definir una función para encontrar el mejor movimiento para el jugador
# Modificar la función evaluar para considerar cuadrados
def evaluar():
    ganador = hay_ganador()
    if ganador == jugador:
        return 10
    elif ganador == oponente:
        return -10
    else:
        valor = 0
        for a, b, c in ganadoras:
            if tablero[a] == tablero[b] == tablero[c] == jugador:
                valor += 1
            elif tablero[a] == tablero[b] == tablero[c] == oponente:
                valor -= 1
        return valor

# Modificar la función mejor_movimiento para considerar cuadrados
def mejor_movimiento():
    mejor_valor = -float("inf")
    mejor_posicion = -1
    for i in range(9):
        if tablero[i] == " ":
            tablero[i] = jugador
            valor = min_max(False)
            tablero[i] = " "
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_posicion = i
    return mejor_posicion

# Definir una función para jugar el juego
def jugar():
    # Mostrar el tablero inicial
    mostrar_tablero()
    # Repetir hasta que el juego termine
    while True:
        # Pedir al usuario que elija una posición válida
        posicion = int(input("Elige una posición del 1 al 9: ")) - 1
        while posicion not in range(9) or tablero[posicion] != " ":
            posicion = int(input("Posición inválida. Elige otra: ")) - 1
        # Colocar el símbolo del oponente en la posición elegida
        tablero[posicion] = oponente
        # Mostrar el tablero actualizado
        mostrar_tablero()
        print("")
        # Comprobar si el oponente ha ganado o si el tablero está lleno
        if hay_ganador() == oponente:
            print("Has ganado. ¡Felicidades!")
            break
        if tablero_lleno():
            print("Es un empate. ¡Bien jugado!")
            break
        # Encontrar el mejor movimiento para el jugador
        posicion = mejor_movimiento()
        # Colocar el símbolo del jugador en la posición elegida
        tablero[posicion] = jugador
        # Mostrar el tablero actualizado
        mostrar_tablero()
        # Comprobar si el jugador ha ganado o si el tablero está lleno
        if hay_ganador() == jugador:
            print("He ganado. ¡Gracias por jugar!")
            break
        if tablero_lleno():
            print("Es un empate. ¡Bien jugado!")
            break

# Llamar a la función jugar para iniciar el juego
jugar()