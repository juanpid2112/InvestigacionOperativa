from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional
from .ford_fulkerson import GrafoFlujoMaximo

class FlujoMaximoView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            grafo = request.data.get('aristas', [])
            fuente = request.data.get('fuente', 0)
            sumidero = request.data.get('sumidero',-1)
            numNodos = request.data.get('nodos', 0)
            if numNodos > 0 and sumidero != -1:
                grafo = convertir_a_matriz_adyacencia_bidireccional (grafo,numNodos)
            
                flujo_maximo = GrafoFlujoMaximo(grafo)
                print (flujo_maximo)
                maximo = flujo_maximo.ford_fulkerson(fuente, sumidero)
            
                return Response({'rta': maximo})
            return Response({'rta': 0})
        except:
            return Response({'rta': 0})
    