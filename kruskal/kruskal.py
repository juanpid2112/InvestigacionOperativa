class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = []

    def agregar_arista(self, u, v, w):
        self.grafo.append([u, v, w])

    def encontrar(self, padre, i):
        if padre[i] == i:
            return i
        return self.encontrar(padre, padre[i])

    def unir(self, padre, rango, x, y):
        raiz_x = self.encontrar(padre, x)
        raiz_y = self.encontrar(padre, y)

        if rango[raiz_x] < rango[raiz_y]:
            padre[raiz_x] = raiz_y
        elif rango[raiz_x] > rango[raiz_y]:
            padre[raiz_y] = raiz_x
        else:
            padre[raiz_y] = raiz_x
            rango[raiz_x] += 1

    def kruskal(self):
        if not self.grafo:
            return []
        
        resultado = []
        i, e = 0, 0

        self.grafo = sorted(self.grafo, key=lambda item: item[2])

        padre = []
        rango = []

        for nodo in range(self.V):
            padre.append(nodo)
            rango.append(0)

        while e < self.V - 1 and i < len(self.grafo):  # Añadir control de longitud de la lista grafo
            u, v, w = self.grafo[i]
            i += 1
            x = self.encontrar(padre, u)
            y = self.encontrar(padre, v)

            if x != y:
                e += 1
                resultado.append([u, v, w])
                self.unir(padre, rango, x, y)

        return resultado
