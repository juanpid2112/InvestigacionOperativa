from rest_framework.views import APIView
from rest_framework.response import Response
from .dijkstra import GrafoDijkstra
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional


class DijkstraView(APIView):

    def post(self, request, *args, **kwargs):
        try:
            grafo = request.data.get('aristas', [])
            numNodos = request.data.get('nodos',0)
            if numNodos > 0:
                grafo = convertir_a_matriz_adyacencia_bidireccional (grafo,numNodos)
                origen = request.data.get('origen', 0)
                
                dijkstra = GrafoDijkstra(grafo)
                camino_mas_corto = dijkstra.dijkstra(origen)
                
                return Response({'rta': camino_mas_corto})
            return Response({'rta': 0})
        except:
            return Response({'rta': 0})
    
