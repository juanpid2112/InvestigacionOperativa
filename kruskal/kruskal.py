class GrafoKruskal:
    def __init__(self, grafo):
        self.grafo = grafo
        self.V = len(grafo)

    def encontrar(self, parent, i):
        if parent[i] == i:
            return i
        return self.encontrar(parent, parent[i])

    def union(self, parent, rank, x, y):
        raiz_x = self.encontrar(parent, x)
        raiz_y = self.encontrar(parent, y)
        
        if rank[raiz_x] < rank[raiz_y]:
            parent[raiz_x] = raiz_y
        elif rank[raiz_x] > rank[raiz_y]:
            parent[raiz_y] = raiz_x
        else:
            parent[raiz_y] = raiz_x
            rank[raiz_x] += 1

    def kruskal(self):
        resultado = []
        i, e = 0, 0
        aristas = []

        for origen in range(self.V):
            for destino in range(origen, self.V):
                if self.grafo[origen][destino] > 0:
                    aristas.append([origen, destino, self.grafo[origen][destino]])

        aristas = sorted(aristas, key=lambda item: item[2])

        parent = []
        rank = []

        for nodo in range(self.V):
            parent.append(nodo)
            rank.append(0)

        while e < self.V - 1:
            origen, destino, peso = aristas[i]
            i += 1
            x = self.encontrar(parent, origen)
            y = self.encontrar(parent, destino)

            if x != y:
                e += 1
                resultado.append([origen, destino, peso])
                self.union(parent, rank, x, y)

        return resultado

