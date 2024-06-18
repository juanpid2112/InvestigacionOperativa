from rest_framework.views import APIView
from rest_framework.response import Response
from .ford_fulkerson import GrafoFlujoMaximo

class FlujoMaximoView(APIView):
    def post(self, request, *args, **kwargs):
        grafo = request.data.get('grafo', [])
        fuente = request.data.get('fuente', 0)
        sumidero = request.data.get('sumidero', len(grafo) - 1)
        
        flujo_maximo = GrafoFlujoMaximo(grafo)
        print (flujo_maximo)
        maximo = flujo_maximo.ford_fulkerson(fuente, sumidero)
        
        return Response({'flujo_maximo': maximo})
