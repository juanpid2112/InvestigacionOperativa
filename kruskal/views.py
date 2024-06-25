from rest_framework.views import APIView
from rest_framework.response import Response
from .kruskal import GrafoKruskal
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional

class KruskalView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            grafo = request.data.get('aristas', [])
            numNodos = request.data.get('nodos', 0)
            
            if not grafo:
                return Response({
                    "rta": 0,
                    "error": "El grafo es requerido."
                }, status=400)

            if numNodos > 0:
                print(f"Number of nodes: {numNodos}")
                print(f"Edges: {grafo}")

                grafo = convertir_a_matriz_adyacencia_bidireccional(grafo, numNodos)
                
                if grafo is None:
                    return Response({
                        "rta": 0,
                        "error": "El grafo contiene un error en su formato, o el número de nodos no es correcto."
                    }, status=400)
                
                print(f"Adjacency Matrix: {grafo}")
                
                kruskal = GrafoKruskal(grafo)
                mst = kruskal.kruskal()
                
                return Response({'rta': mst})
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

