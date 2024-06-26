from rest_framework.views import APIView
from rest_framework.response import Response
from .kruskal import GrafoKruskal
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional

class KruskalView(APIView):
    def obtenerRelaciones (self,grafo):
        matriz = []
        for arista in grafo:
            if not [arista[0],arista[1]] in matriz:
                matriz.append ([arista[0],arista[1]])
        return matriz
    def comparar (self, grafo, base):
        matriz = []
        base = self.obtenerRelaciones(base)
        for arista in grafo:
            if not ([arista[0],arista[1]] in matriz) and not ([arista[1],arista[0]] in matriz):
                if [arista[1],arista[0]] in base:
                    matriz.append([arista[1],arista[0]])
                else:
                    matriz.append([arista[0],arista[1]])
        print (matriz)
        return matriz
    def obtenerPeso (self,grafo):
        aux = 0
        for arista in grafo:
            aux += arista[2]
        return aux
    def post(self, request, *args, **kwargs):
        try:
            grafo = request.data.get('aristas', [])
            numNodos = request.data.get('nodos', 0)
            if grafo == []:
                return Response({
                    "rta": 0,
                    "error": "El grafo es requerido."
                }, status=400)
            if numNodos > 0:
                aux = grafo
                grafo, error = convertir_a_matriz_adyacencia_bidireccional(grafo, numNodos)
                if grafo is None:
                    return Response({
                        "rta": 0,
                        "error": error
                    }, status=400)
                kruskal = GrafoKruskal(grafo)
                mst = kruskal.kruskal()
                peso = self.obtenerPeso(mst)
                mst =  self.obtenerRelaciones(mst)

                return Response({
                    'aristas':self.comparar(mst,aux),
                    "peso":peso
                    })
            return Response({
                "rta": 0,
                "error": "El número de nodos es requerido."
            }, status=400)
        except Exception as e:
            return Response({
                "error": "El servidor no puede procesar la solicitud debido a una memoria insuficiente. Por favor, libere recursos innecesarios y vuelva a intentarlo.",
                'rta': 0
            }, status=400)


