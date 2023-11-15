class Nodo:
    def __init__(self, estado, padre=None):
        self.estado = estado
        self.padre = padre
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

def busqueda_profundidad(nodo, objetivo):
    pila = [(nodo, [nodo.estado])]  # Modificado para rastrear el camino
    visitados = set()

    while pila:
        actual, camino = pila.pop()

        if actual.estado == objetivo:
            # Se encontró el objetivo, puedes retornar el camino o el nodo
            return camino

        if actual.estado not in visitados:
            visitados.add(actual.estado)
            # Agrega los hijos al final de la pila para explorar en profundidad
            pila.extend((hijo, camino + [hijo.estado]) for hijo in actual.hijos[::-1])

    # Si no se encuentra el objetivo
    return None

# Ejemplo de uso
# Crear nodos y establecer las relaciones padre-hijo según el problema
nodo_inicial = Nodo(estado="A")
nodo_b = Nodo(estado="B", padre=nodo_inicial)
nodo_c = Nodo(estado="C", padre=nodo_inicial)
nodo_d = Nodo(estado="D", padre=nodo_b)
nodo_e = Nodo(estado="E", padre=nodo_b)

# Agregar hijos a los nodos
nodo_inicial.agregar_hijo(nodo_b)
nodo_inicial.agregar_hijo(nodo_c)
nodo_b.agregar_hijo(nodo_d)
nodo_b.agregar_hijo(nodo_e)

# Realizar la búsqueda por profundidad
objetivo = "E"
resultado = busqueda_profundidad(nodo_inicial, objetivo)

if resultado:
    print(f"Se encontró el objetivo {objetivo}")
    print("Recorrido:", resultado)
else:
    print(f"No se encontró el objetivo {objetivo}")
