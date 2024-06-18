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
        max_flujo = 0

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
                v = u

        return max_flujo
