def convertir_a_matriz_adyacencia_bidireccional(aristas, num_vertices):
    matriz = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    for arista in aristas:
        origen, destino, peso1, peso2 = arista
        matriz[origen][destino] = peso1
        matriz[destino][origen] = peso2
    return matriz
