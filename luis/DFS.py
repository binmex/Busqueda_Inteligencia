def dfs(visited, graph, node, target):
    if node not in visited:
        print(node)
        visited.add(node)
        if node == target:
            return True  # Devuelve True si se encuentra el nodo objetivo
        for neighbour in graph[node]:
            if dfs(visited, graph, neighbour, target):
                return True  # Si se encuentra el objetivo en el subárbol, devuelve True
    return False  # Devuelve False si el nodo objetivo no se encuentra en el subárbol


# Ejemplo de uso:
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()
start_node = 'A'
target_node = 'F'

found = dfs(visited, graph, start_node, target_node)

if found:
    print(f"Se encontró el nodo {target_node}.")
else:
    print(f"No se encontró el nodo {target_node}.")
