def convertir_a_matriz_adyacencia_bidireccional(aristas, num_vertices):
    # Crear una matriz de adyacencia inicializada en 0
    matriz = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]
    
    # Rellenar la matriz con los valores proporcionados por las aristas
    for arista in aristas:
        if len(arista) != 4:
            print(f"Formato de arista inválido: {arista}")
            return None
        
        origen, destino, peso1, peso2 = arista
        
        # Ajustar los índices para que empiecen desde 1
        origen -= 1
        destino -= 1
        
        # Verificar que los nodos estén dentro del rango permitido
        if origen < 0 or destino < 0 or origen >= num_vertices or destino >= num_vertices:
            print(f"Índices de nodos inválidos: {origen + 1}, {destino + 1}")
            return None
        
        # Asignar los pesos a la matriz para grafo no dirigido
        matriz[origen][destino] = peso1
        matriz[destino][origen] = peso1
    
    # Imprimir la matriz de adyacencia para verificación
    print(f"Matriz de Adyacencia: {matriz}")
    return matriz

