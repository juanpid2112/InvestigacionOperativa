def convertir_a_matriz_adyacencia_bidireccional(aristas, num_vertices):
    aux = []
    for x in range(num_vertices):
        aux.append(x)
    verticeMayor = -1
    for arista in aristas:
        if not arista[0] in aux or not arista[1] in aux:#Verifico que la arista este en los valores posibles
            return None
        if arista[0] > verticeMayor:
            verticeMayor = arista[0]
        if arista[1] > verticeMayor:
            verticeMayor = arista[1]
    if verticeMayor != num_vertices-1:
        return None
    try:
        matriz = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
        for arista in aristas:
            origen, destino, peso1, peso2 = arista
            matriz[origen][destino] = peso1
            matriz[destino][origen] = peso2
    except Exception as e:
        matriz = None
    return matriz