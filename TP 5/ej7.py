# INCISO A

def genProbSimSalida(prob_priori, matriz_canal):
    n = len(matriz_canal[0]) # cantidad de simbolos de salida
    prob_simbolos = [0] * n
    
    for j in range(n):
        for i in range(len(prob_priori)):
            prob_simbolos[j] += prob_priori[i] * matriz_canal[i][j]
    
    return prob_simbolos

def genMatrizPosteriori(prob_priori, matriz_canal):
    prob_simbolos = genProbSimSalida(prob_priori, matriz_canal)
    n = len(matriz_canal)      # cantidad de símbolos de entrada
    m = len(matriz_canal[0])   # cantidad de símbolos de salida
    matriz = [[0.0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            matriz[i][j] = (matriz_canal[i][j] * prob_priori[i]) / prob_simbolos[j]
    
    return matriz

def genMatrizSimultaneos(prob_priori, matriz_canal):
    n = len(matriz_canal)      # cantidad de símbolos de entrada
    m = len(matriz_canal[0])   # cantidad de símbolos de salida
    matriz = [[0.0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            matriz[i][j] = matriz_canal[i][j] * prob_priori[i]
    
    return matriz

matriz_canal = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]
prob_priori = [0.3, 0.3, 0.4]

prob_simbolos = genProbSimSalida(prob_priori, matriz_canal)

matriz_posteriori = genMatrizPosteriori(prob_priori, matriz_canal)

matriz_simultaneos = genMatrizSimultaneos(prob_priori, matriz_canal)

print("Probabilidad de los símbolos:")
print(prob_simbolos)
print()

print("Matriz de probabilidades a posteriori:")
for fila in matriz_posteriori:
    print([round(x, 3) for x in fila])

print()
print("Matriz de sucesos simultáneos:")
for fila in matriz_simultaneos:
    print([round(x, 3) for x in fila])