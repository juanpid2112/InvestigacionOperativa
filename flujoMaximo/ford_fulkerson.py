class GrafoFlujoMaximo:
    def __init__(self, grafo):
        self.grafo = grafo
        self.vertices = len(grafo)
        self.padre = [-1] * self.vertices

    def bfs(self, s, t):
        visitado = [False] * self.vertices
        cola = []
        cola.append(s)
        visitado[s] = True

        while cola:
            u = cola.pop(0)
            for ind, val in enumerate(self.grafo[u]):
                if not visitado[ind] and val > 0:
                    cola.append(ind)
                    visitado[ind] = True
                    self.padre[ind] = u

        return visitado[t]

    def ford_fulkerson(self, fuente, sumidero):
        # Ajustar los índices para que empiecen desde 1
        fuente -= 1
        sumidero -= 1
        
        max_flujo = 0
        iteraciones = 0
        aristas_actualizadas = []

        while self.bfs(fuente, sumidero):
            camino_flujo = float('inf')
            v = sumidero
            while v != fuente:
                u = self.padre[v]
                camino_flujo = min(camino_flujo, self.grafo[u][v])
                v = u

            max_flujo += camino_flujo

            v = sumidero
            while v != fuente:
                u = self.padre[v]
                self.grafo[u][v] -= camino_flujo
                self.grafo[v][u] += camino_flujo
                aristas_actualizadas.append([u + 1, v + 1, self.grafo[u][v] + camino_flujo, self.grafo[v][u]])
                v = u

            iteraciones += 1

        return max_flujo, iteraciones, aristas_actualizadas

    def obtener_grafo_completo(self):
        grafo_completo = []
        for u in range(self.vertices):
            for v in range(self.vertices):
                if self.grafo[u][v] > 0:
                    grafo_completo.append([u + 1, v + 1, self.grafo[u][v], 0])
        return grafo_completo







