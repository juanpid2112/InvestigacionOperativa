from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional
from .ford_fulkerson import GrafoFlujoMaximo

class FlujoMaximoView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            grafo = request.data.get('aristas', [])
            if grafo == []:
                return Response({
                    "rta": 0,
                    "error":"El grafo es requerido."
                    }, status=400)
            fuente = request.data.get('fuente', 0)
            sumidero = request.data.get('sumidero',-1)
            numNodos = request.data.get('nodos', 0)
            if numNodos > 0 and sumidero != -1:
                grafo = convertir_a_matriz_adyacencia_bidireccional (grafo,numNodos)
                if grafo is None:
                    return Response({
                        "rta": 0,
                        "error":"El grafo contiene un error en su formato, o el numero de nodos no es correcto."
                        }, status=400)
                flujo_maximo = GrafoFlujoMaximo(grafo)
                print (flujo_maximo)
                maximo = flujo_maximo.ford_fulkerson(fuente, sumidero)
            
                return Response({'rta': maximo})
            return Response({
                "error":"El numero de nodos y el sumidero son datos requeridos.",
                'rta': 0
                }, status=400)
        except Exception as e:
            return Response({
                "error":str(e),
                'rta': 0
                }, status=400)
    