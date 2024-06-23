from rest_framework.views import APIView
from rest_framework.response import Response
from .kruskal import GrafoKruskal
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional
class KruskalView(APIView):
    def post(self, request, *args, **kwargs):
        grafo = request.data.get('aristas', [])
        numNodos = request.data.get('nodos',0)
        if numNodos > 0:
            grafo = convertir_a_matriz_adyacencia_bidireccional (grafo,numNodos)
            print (grafo)
            kruskal = GrafoKruskal(grafo)
            mst = kruskal.kruskal()
            return Response({'rta': mst})
        return Response({'rta': 0})
    