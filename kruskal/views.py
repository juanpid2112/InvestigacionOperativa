from rest_framework.views import APIView
from rest_framework.response import Response
from .kruskal import Grafo

class KruskalView(APIView):
    def post(self, request, *args, **kwargs):
        aristas = request.data.get('aristas', [])
        
        grafo = Grafo(len(aristas) + 1)
        for arista in aristas:
            grafo.agregar_arista(arista[0], arista[1], arista[2])
        
        resultado = grafo.kruskal()
        
        return Response(resultado)

    