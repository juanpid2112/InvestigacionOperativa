from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
class kruskal (APIView):
    def get (self,request):
        matriz = [
            ["A","B",30],
            ["A","C",35],
            ["A","G",42],
            ["B","C",36],
            ["B","D",34],
            ["B","E",37],
            ["B","F",43],
            ["B","G",42],
            ["C","D",32],
            ["C","E",52],
            ["C","H",57],
            ["D","E",41],
            ["E","H",40],
            ["E","F",47],
            ["F","H",45],
            ["F","G",38],
            ["G","H",46],
            ["E","F",47],
        ]

        matriz_ordenada = sorted(matriz, key=lambda x: x[2])  
        
        resultado = []
        resultado.append(matriz_ordenada[0])
        for linea in matriz_ordenada:
            cont=0
            for y in resultado:
                print(linea[0])
                print(linea[1])
                if (linea[0] in y) or (linea[1] in y):
                    cont +=1
            print (cont)
            if cont != 2:
                resultado.append(linea)

        print (resultado)
        return Response ({"Resultado": resultado})
    
    