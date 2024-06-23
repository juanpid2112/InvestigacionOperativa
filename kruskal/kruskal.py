class GrafoKruskal:
    def __init__(self, grafo):
        self.grafo = grafo
        self.vertices = len(grafo)
        self.aristas = self.convertir_a_aristas()

    def convertir_a_aristas(self):
        aristas = []
        for i in range(self.vertices):
            for j in range(i, self.vertices):
                if self.grafo[i][j] != 0:
                    aristas.append([i, j, self.grafo[i][j]])
        return aristas

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i = 0
        e = 0
        self.aristas = sorted(self.aristas, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e < self.vertices - 1:
            u, v, w = self.aristas[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result

