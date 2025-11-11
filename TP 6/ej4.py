def canal_compuesto(matriz_A, matriz_B):
    # Filas de A y columnas de B
    filas_A = len(matriz_A)
    columnas_A = len(matriz_A[0])
    filas_B = len(matriz_B)
    columnas_B = len(matriz_B[0])
    
    # Verificación de compatibilidad
    if columnas_A != filas_B:
        print("Las dimensiones de las matrices no permiten multiplicación")
        resultado = [-1]
    else:
        # Inicializar matriz resultado con ceros
        resultado = [[0.0 for _ in range(columnas_B)] for _ in range(filas_A)]

        # Multiplicación matricial
        for i in range(filas_A):
            for j in range(columnas_B):
                for k in range(columnas_A):
                    resultado[i][j] += matriz_A[i][k] * matriz_B[k][j]
    
    return resultado