from rest_framework.views import APIView
from rest_framework.response import Response
from .dijkstra import GrafoDijkstra
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional

class DijkstraView(APIView):

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
                grafo = convertir_a_matriz_adyacencia_bidireccional(grafo, numNodos)
                if grafo is None:
                    return Response({
                        "rta": 0,
                        "error": "El grafo contiene un error en su formato, o el número de nodos no es correcto."
                    }, status=400)
                origen = request.data.get('origen', 1)
                destino = request.data.get('destino', 1)
                
                # Ajustar los índices para que empiecen desde 1
                if origen <= 0 or origen > numNodos or destino <= 0 or destino > numNodos:
                    return Response({
                        "rta": 0,
                        "error": "El nodo origen o destino es inválido."
                    }, status=400)
                
                dijkstra = GrafoDijkstra(grafo)
                distancia, arcos = dijkstra.dijkstra(origen - 1, destino - 1)
                
                return Response({'distancia': distancia, 'aristas': arcos})
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


