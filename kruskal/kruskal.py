class GrafoKruskal:
    def __init__(self, grafo):
        self.grafo = grafo
        self.V = len(grafo)
        self.aristas = self.convertir_a_aristas()

    def convertir_a_aristas(self):
        aristas = []
        for i in range(self.V):
            for j in range(i+1, self.V):
                if self.grafo[i][j] != 0:
                    aristas.append([i, j, self.grafo[i][j]])
        return aristas

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        resultado = []
        i, e = 0, 0
        self.aristas = sorted(self.aristas, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.aristas[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                resultado.append([u + 1, v + 1, w, 0])  # +1 para índices desde 1, peso2 es 0
                self.union(parent, rank, x, y)
        return resultado
