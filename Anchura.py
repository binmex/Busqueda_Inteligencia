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

grafo_principal ={   'A': {'B': 92, 'C': 87},
    'B': {'D':92, 'E': 142},
    'C': {'F':92, 'G': 142},
    'D': {'H':92}
    }
print (BreadthFirstSearch(grafo_principal, 'A', 'H'))