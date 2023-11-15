import pprint
import os

# Pprint para mostrar de forma Pretty
pp = pprint.PrettyPrinter(indent=4)

# Grafo principal
grafo_principal = {}

# Lee el archivo .txt y carga el grafo_principal
with open('mapa.txt', 'r') as f:
    for l in f:
        ciudad_a, ciudad_b, costo = l.split()
        if ciudad_a not in grafo_principal:
            grafo_principal[ciudad_a] = {}
        grafo_principal[ciudad_a][ciudad_b] = int(costo)
        if ciudad_b not in grafo_principal:
            grafo_principal[ciudad_b] = {}
        grafo_principal[ciudad_b][ciudad_a] = int(costo)
        print(grafo_principal)


# Breadth First Search Method (Busqueda en Amplitud)
def BreadthFirstSearch(grafo, inicio, destino):
    cola = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while cola:
        (node, camino, costo) = cola.pop(0)
        for temp in grafo[node].keys():
            if temp == destino:
                return camino + [temp], costo + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    cola.append((temp, camino + [temp], costo + grafo[node][temp]))


# Depth First Search Method (Busqueda en Profundidad)
def DepthFirstSearch(grafo, inicio, destino):
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while pila:
        (node, camino, costo) = pila.pop()
        for temp in grafo[node].keys():
            if temp == destino:
                return camino + [temp], costo + grafo[node][temp]
            else:
                if temp not in visitado:
                    visitado.add(temp)
                    pila.append((temp, camino + [temp], costo + grafo[node][temp]))


# Iterative Deepening Search Method (Busqueda en Profundidad Iterativa)
def IterativeDeepening(grafo, inicio, destino):
    nivel = 0
    contador = 0
    pila = [(inicio, [inicio], 0)]
    visitado = {inicio}
    while True:
        nivel += 1
        while pila:
            if contador <= nivel:
                contador = 0
                (node, camino, costo) = pila.pop()
                for temp in grafo[node].keys():
                    if temp == destino:
                        return camino + [temp], costo + grafo[node][temp]
                    else:
                        if temp not in visitado:
                            visitado.add(temp)
                            contador += 1
                            pila.append((temp, camino + [temp], costo + grafo[node][temp]))
            else:
                q = pila
                visitado_bfs = {inicio}
                while q:
                    (node, camino, costo) = q.pop(0)
                    for temp in grafo[node].keys():
                        if temp == destino:
                            return camino + [temp], costo + grafo[node][temp]
                        else:
                            if temp not in visitado_bfs:
                                visitado_bfs.add(temp)
                                q.append((temp, camino + [temp], costo + grafo[node][temp]))
                break

# A-Star Search Method (Busqueda A-Estrella)
def a_star_search(grafo, inicio, destino):
    #Metodo
    return None

# Best First search (Busqueda Primero el Mejor)
def best_first_search(grafo, inicio, destino):
    #Metodo
    return None

n = 1
while n == 1:
    os.system("CLS")
    print("""============================================
                Grafo Completo
============================================""")
    pp.pprint(grafo_principal)
    print("""============================================
[1] Amplitud
[2] Profundidad
[3] Profundidad Iterativa
[4] A Star
[5] Primero el mejor
[0] Salir
============================================""")
    x = input("Opcion: ")
    if x == '1':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Resultados
============================================""")
        print (BreadthFirstSearch(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '2':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Resultados
============================================""")
        print (DepthFirstSearch(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '3':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Resultados
============================================""")
        print (IterativeDeepening(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '4':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Resultados
============================================""")
        print(a_star_search(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '5':
        inicio = input("Ingresa el Inicio: ")
        while inicio not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            inicio = input("Ingresa el Inicio: ")
        destino = input("Ingresa el Destino: ")
        while destino not in grafo_principal:
            print("Ciudad no encontrada intenta nuevamente")
            destino = input("Ingresa el Destino: ")
        print("""============================================
                 Resultados
============================================""")
        print(best_first_search(grafo_principal, inicio, destino))
        print("============================================")
        os.system("pause")

    elif x == '0':
        break