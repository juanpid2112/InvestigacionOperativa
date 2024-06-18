from rest_framework.views import APIView
from rest_framework.response import Response
from .dijkstra import GrafoDijkstra

class DijkstraView(APIView):
    def post(self, request, *args, **kwargs):
        grafo = request.data.get('grafo', [])
        origen = request.data.get('origen', 0)
        
        dijkstra = GrafoDijkstra(grafo)
        camino_mas_corto = dijkstra.dijkstra(origen)
        
        return Response({'camino_mas_corto': camino_mas_corto})
