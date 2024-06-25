import heapq

class GrafoDijkstra:
    def __init__(self, grafo):
        self.grafo = grafo
        self.V = len(grafo)

    def dijkstra(self, origen, destino):
        # Inicializar las distancias a infinito y la ruta
        distancia = {nodo: float('infinity') for nodo in range(self.V)}
        distancia[origen] = 0
        padre = {nodo: None for nodo in range(self.V)}
        visitados = set()
        cola = [(0, origen)]  # (distancia, nodo)

        while cola:
            distancia_actual, nodo_actual = heapq.heappop(cola)

            if nodo_actual in visitados:
                continue

            visitados.add(nodo_actual)

            if nodo_actual == destino:
                break

            for vecino, peso in enumerate(self.grafo[nodo_actual]):
                if peso > 0:
                    distancia_nueva = distancia_actual + peso
                    if distancia_nueva < distancia[vecino]:
                        distancia[vecino] = distancia_nueva
                        padre[vecino] = nodo_actual
                        heapq.heappush(cola, (distancia_nueva, vecino))

        # Construir la ruta desde el origen al destino
        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = padre[actual]
        ruta = ruta[::-1]  # Invertir la ruta

        # Construir el formato de arcos [nodoOrigen, nodoDestino, peso1, peso2]
        arcos = []
        for i in range(len(ruta) - 1):
            nodo_origen = ruta[i]
            nodo_destino = ruta[i + 1]
            peso1 = self.grafo[nodo_origen][nodo_destino]
            peso2 = 0  # Peso2 es siempre 0 en este caso
            arcos.append([nodo_origen + 1, nodo_destino + 1, peso1, peso2])

        return distancia[destino], arcos

