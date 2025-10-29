import math

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

def genEntropiasPosteriori(prob_priori, matriz_canal):
    matriz_posteriori = genMatrizPosteriori(prob_priori, matriz_canal)
    n = len(matriz_canal)       # cantidad de símbolos de entrada
    m = len(matriz_canal[0])    # cantidad de símbolos de salida
    
    entropias = []
    for j in range(m):
        H = 0.0
        for i in range(n):
            p = matriz_posteriori[i][j]
            if p > 0:
                H += p * math.log2(1 / p)
        entropias.append(H)
    
    return entropias

def genEntropiaPriori(prob_priori):
    H = 0.0
    for p in prob_priori:
        if p > 0:
            H += p * math.log2(1 / p)
    return H

def imprimir_entropia_posteriori(entropias, alfabeto_salida=None):
    if alfabeto_salida is None:
        alfabeto_salida = [f"b{i+1}" for i in range(len(entropias))]

    print("Entropías a posteriori:")
    for simbolo, h in zip(alfabeto_salida, entropias):
        print(f"H(A / {simbolo}) = {h:.4f} bits")

matriz = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5],
    [0.3, 0.4, 0.3]
]
prob_priori = [0.3, 0.3, 0.4]
A = ["a", "b", "c"]
B = ["1", "2", "3"]

H_A = genEntropiaPriori(prob_priori)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

entropias = genEntropiasPosteriori(prob_priori, matriz)

imprimir_entropia_posteriori(entropias, B)