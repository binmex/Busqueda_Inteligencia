from collections import deque


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []


def bfs(root, target):
    if root is None:
        return

    queue = deque([root])
    visited = set()

    while queue:
        current_node = queue.popleft()
        print(current_node.value)

        if current_node.value == target:
            print("Nodo objetivo encontrado!")
            return

        visited.add(current_node)

        for child in current_node.children:
            if child not in visited and child not in queue:
                queue.append(child)


# Crear un árbol de ejemplo
root = TreeNode('A')
node_b = TreeNode('B')
node_c = TreeNode('C')
node_d = TreeNode('D')
node_e = TreeNode('E')
node_f = TreeNode('F')
node_h=TreeNode('H')

root.children = [node_b, node_c]
node_b.children = [TreeNode('G'),node_h,node_d]
node_c.children = [node_d, node_e]
node_d.children = [node_f,node_h, node_e]
# Solicitar al usuario que ingrese el nodo objetivo
target_node = input("Ingresa el nodo que deseas buscar: ")

# Llamar a la función BFS con el nodo raíz y el nodo objetivo
bfs(root, target_node)
