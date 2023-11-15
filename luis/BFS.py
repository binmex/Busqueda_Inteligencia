graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

visited = set()  # Utilizamos un conjunto para mayor eficiencia
queue = []

def bfs(visited, graph, start, target):
    visited.add(start)
    queue.append(start)

    while queue:
        current_node = queue.pop(0)
        print(current_node, end=" ")

        if current_node == target:
            print(f"\nSe encontró el nodo {target}.")
            return
        for neighbour in graph[current_node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print(f"\nNo se encontró el nodo {target} en el grafo.")
# Uso del BFS para buscar el nodo '2'
print("Recorrido en Amplitud (BFS):")
bfs(visited, graph, start='5', target='8')
