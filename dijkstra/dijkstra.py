import heapq

class GrafoDijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def dijkstra(self, origen):
        distancia = {nodo: float('infinity') for nodo in range(len(self.grafo))}
        distancia[origen] = 0
        visitados = set()
        cola = [(0, origen)]  # (distancia, nodo)

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)

            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            for vecino, peso in enumerate(self.grafo[nodo_actual]):
                if peso > 0:
                    distancia_nueva = distancia_actual + peso
                    if distancia_nueva < distancia[vecino]:
                        distancia[vecino] = distancia_nueva
                        heapq.heappush(cola, (distancia_nueva, vecino))

        return distancia
