from rest_framework.views import APIView
from rest_framework.response import Response
from .dijkstra import GrafoDijkstra
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional

class DijkstraView(APIView):
    def obtenerRelaciones (self,grafo):
        matriz = []
        for arista in grafo:
            if not [arista[0],arista[1]] in matriz:
                matriz.append ([arista[0],arista[1]])
        return matriz
    def buscarMaximo (self,grafo):
        aux = -1
        for arista in grafo:
            if arista[0] > aux:
                aux = arista[0]
            if arista[1] > aux:
                aux = arista[1]
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
                origen = request.data.get('fuente', 1)
                destino = request.data.get('sumidero', -1)
                if destino == -1:
                    destino = self.buscarMaximo(aux)
                
                # Ajustar los índices para que empiecen desde 1
                if origen < 1 and destino == -1:
                    return Response({
                        "rta": 0,
                        "error": "El nodo origen o destino es inválido."
                    }, status=400)
                
                dijkstra = GrafoDijkstra(grafo)
                distancia, arcos = dijkstra.dijkstra(origen - 1, destino - 1)
                
                return Response({'distancia': distancia, 'aristas': self.obtenerRelaciones(arcos)})
            else:
                return Response({
                    "rta": 0,
                    "error": "El número de nodos es requerido."
                }, status=400)
        except Exception as e:
            return Response({
                "error": str(e),
                'rta': 0
            }, status=400)


