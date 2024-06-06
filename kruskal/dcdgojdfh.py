def buscar (matriz,linea):
    for linea in matriz: 
        

def funcion ():
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

    for linea in matriz:
