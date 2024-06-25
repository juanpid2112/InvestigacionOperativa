from rest_framework.views import APIView
from rest_framework.response import Response
from .utils.convertir import convertir_a_matriz_adyacencia_bidireccional
from .ford_fulkerson import GrafoFlujoMaximo

class FlujoMaximoView(APIView):
    def obtenerRelaciones (self,grafo):
        matriz = []
        for arista in grafo:
            if not [arista[0],arista[1]] in matriz:
                matriz.append ([arista[0],arista[1]])
        return matriz
    def acomodar (self,grafo,grafoBase):
        grafoAux = grafoBase
        grafoBase = self.obtenerRelaciones(grafoBase)
        print (grafoBase)
        matriz = []
        for arista in grafo:
            print ([arista[1],arista[0]])
            if [arista[1],arista[0]] in grafoBase:
                if not [arista[1],arista[0]] in matriz:
                    matriz.append([arista[1],arista[0],arista[3],arista[2]])
            elif [arista[0],arista[1]] in grafoBase:
                if not [arista[0],arista[1]] in matriz:
                    matriz.append(arista)
        for arista in grafoAux:
            esta = False
            for aristaG in matriz:
                if arista[0] == aristaG[0] and arista[1] == aristaG[1]:
                    esta = True
                    break
            if not esta:
                matriz.append (arista)

        return matriz

    def post(self, request, *args, **kwargs):
        try:
            grafo = request.data.get('aristas', [])
            aux = grafo
            if grafo == []:
                return Response({
                    "rta": 0,
                    "error": "El grafo es requerido."
                }, status=400)
            fuente = request.data.get('fuente', -1)
            sumidero = request.data.get('sumidero', -1)
            numNodos = request.data.get('nodos', 0)
            if numNodos <= 0:
                return Response({
                    "error": "El numero de nodos es requerido.",
                    'rta': 0
                }, status=400)    
            if fuente != 0 and sumidero != -1 :
                grafo, error = convertir_a_matriz_adyacencia_bidireccional(grafo, numNodos)
                if grafo is None:
                    return Response({
                        "rta": 0,
                        "error": error
                    }, status=400)

                if fuente <= 0 or fuente > numNodos or sumidero <= 0 or sumidero > numNodos:
                    return Response({
                        "rta": 0,
                        "error": "El nodo fuente o sumidero es inválido."
                    }, status=400)

                flujo_maximo, iteraciones, aristas_actualizadas = GrafoFlujoMaximo(grafo).ford_fulkerson(fuente, sumidero)
                grafo_completo = GrafoFlujoMaximo(grafo).obtener_grafo_completo()

                return Response({
                    "flujoMax": flujo_maximo,
                    "iteraciones": iteraciones,
                    "aristas": self.acomodar(grafo_completo,aux)
                })
            return Response({
                "error": "La fuente y el sumidero son datos requeridos.",
                'rta': 0
            }, status=400)
        except Exception as e:
            return Response({
                "error": str(e),
                'rta': 0
            }, status=400)




