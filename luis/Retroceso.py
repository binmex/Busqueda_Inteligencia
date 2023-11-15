def retroceso(k, solucion, grafo, objetivo):
    if k == len(solucion):
        return

    for nodo in grafo[solucion[k - 1]]:
        solucion[k] = nodo
        if A(solucion, 1, k):
            if R(solucion, 1, k, objetivo):
                guardar(solucion, 1, k)
            retroceso(k + 1, solucion, grafo, objetivo)
# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': ['Z'],
    'Z': ['Q']
}
# Función de restricción (puede necesitar ajustes según tu problema)
def A(solucion, inicio, fin):
    # Restricción: No visitar nodos ya visitados en la solución parcial
    nodos_visitados = set(solucion[inicio:fin + 1])
    return len(nodos_visitados) == fin - inicio + 1
# Función de validación de la solución (puede necesitar ajustes según tu problema)
def R(solucion, inicio, fin, objetivo):
    # Restricción: El último nodo en la solución parcial debe ser igual al nodo objetivo
    return solucion[fin] == objetivo
def guardar(solucion, inicio, fin):
    print("Guardando solución:", solucion[inicio:fin + 1])

n = 5  # Definir la longitud de la solución
solucion = [None] * (n + 1)  # Crear una lista para la solución
solucion[1] = 'A'  # Establecer el nodo de inicio

# Llamar al algoritmo de retroceso
retroceso(2, solucion, graph, 'Q')
