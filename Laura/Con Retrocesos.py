class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def backtracking(tree_node, target, path=None):
    if path is None:
        path = []

    path.append(tree_node.value)

    if tree_node.value == target:
        print("Nodo objetivo encontrado!")
        print("Recorrido:", " -> ".join(path))
        return True

    for child in tree_node.children:
        if backtracking(child, target, path):
            return True

    path.pop()  # Retroceder si no se encontró en este camino
    return False

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
node_d.children = [node_f,node_h]

# Solicitar al usuario que ingrese el nodo objetivo
target_node = input("Ingresa el nodo que deseas buscar: ")

# Llamar a la función de búsqueda con retroceso con el nodo raíz y el nodo objetivo
if not backtracking(root, target_node):
    print("Nodo objetivo no encontrado.")
