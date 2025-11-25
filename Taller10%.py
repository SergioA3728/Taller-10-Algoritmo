# 1. Grafo representado como un diccionario de diccionarios
graph = {
    'Bodega': {'A': 7, 'B': 9, 'C': 14},
    'A': {'B': 10, 'D': 15},
    'B': {'C': 2, 'D': 11},
    'C': {'E': 9},
    'D': {'E': 6},
    'E': {}
}

def dijkstra(graph, start):
    # Inicializar distancias y predecesores
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    visited = set()
    prev = {}

    while len(visited) < len(graph):
        # Escoger el nodo no visitado con menor distancia
        unvisited_nodes = [n for n in graph if n not in visited]
        
        if not unvisited_nodes:
            break
            
        current = min(unvisited_nodes, key=lambda node: dist[node])
        if dist[current] == float('inf'):
            break

        visited.add(current)

        for neighbor, weight in graph[current].items():
            new_distance = dist[current] + weight
            if new_distance < dist[neighbor]:
                dist[neighbor] = new_distance
                prev[neighbor] = current

    return dist, prev

# 3. Prints de resultados
if __name__ == "__main__":
    inicio = 'Bodega'
    distancias, previos = dijkstra(graph, inicio)
#
    print(f"=== RESULTADOS DE RUTAS DESDE {inicio.upper()} ===\n")

    tiendas_objetivo = ['A', 'B', 'C', 'D', 'E']

    for destino in tiendas_objetivo:
        camino = []
        nodo_actual = destino
        
        if distancias[destino] == float('inf'):
            print(f"Tienda {destino}: No hay ruta disponible.")
            continue

        while nodo_actual in previos:
            camino.insert(0, nodo_actual)
            nodo_actual = previos[nodo_actual]

        camino.insert(0, inicio)  

        ruta_texto = " -> ".join(camino)
        print(f"Tienda {destino}")
        print(f"   Ruta: {ruta_texto}")
        print(f"   Distancia total: {distancias[destino]} km")
        print("-" * 30)