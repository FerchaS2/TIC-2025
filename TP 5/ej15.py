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

def genEquivocacionRuido(prob_priori, matriz_canal):
    # Probabilidades de salida P(b)
    prob_salida = genProbSimSalida(prob_priori, matriz_canal)
    
    # Entropías H(A|b)
    entropias_post = genEntropiasPosteriori(prob_priori, matriz_canal)
    
    # Definición: H(A|B) = sum_b P(b) * H(A|b)
    H_A_B = 0
    for j in range(len(prob_salida)):
        H_A_B += prob_salida[j] * entropias_post[j]
    
    return H_A_B

import math

def genPerdida(prob_priori, matriz_canal):
    H_B_A = 0.0
    
    for i in range(len(prob_priori)):  # para cada símbolo de entrada a_i
        H_B_ai = 0.0
        
        for j in range(len(matriz_canal[0])):  # para cada símbolo de salida b_j
            p = matriz_canal[i][j]  # P(b_j | a_i)
            if p > 0:  # evitar log(0)
                H_B_ai += p * math.log2(1/p)
        
        H_B_A += prob_priori[i] * H_B_ai
    
    return H_B_A

def genMatrizSimultaneos(prob_priori, matriz_canal):
    n = len(matriz_canal)      # cantidad de símbolos de entrada
    m = len(matriz_canal[0])   # cantidad de símbolos de salida
    matriz = [[0.0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            matriz[i][j] = matriz_canal[i][j] * prob_priori[i]
    
    return matriz

def genEntropiaAfin(prob_priori, matriz_canal):
    matriz_simultaneos = genMatrizSimultaneos(prob_priori, matriz_canal)
    n = len(matriz_simultaneos)     # cantidad de símbolos de entrada
    m = len(matriz_simultaneos[0])  # cantidad de símbolos de salida
    
    H_AyB = 0.0
    
    for i in range(n):
        for j in range(m):
            p = matriz_simultaneos[i][j]
            if p > 0: # evitar log(0)
                H_AyB += p * math.log2(1/p)
    
    return H_AyB

def genMatrizPosteriori(prob_priori, matriz_canal):
    prob_simbolos = genProbSimSalida(prob_priori, matriz_canal)
    n = len(matriz_canal)      # cantidad de símbolos de entrada
    m = len(matriz_canal[0])   # cantidad de símbolos de salida
    matriz = [[0.0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            matriz[i][j] = (matriz_canal[i][j] * prob_priori[i]) / prob_simbolos[j]
    
    return matriz

def genInfoMutua(prob_priori, matriz_canal):
    matriz_posteriori = genMatrizPosteriori(prob_priori, matriz_canal)
    matriz_simultaneos = genMatrizSimultaneos(prob_priori, matriz_canal)
    
    n = len(matriz_posteriori)      # cantidad de símbolos de entrada
    m = len(matriz_posteriori[0])   # cantidad de símbolos de salida
    
    I_AyB = 0.0
    
    for i in range(n):
        p_a = prob_priori[i]
        for j in range(m):
            p_ayb = matriz_simultaneos[i][j]
            p_a_b = matriz_posteriori[i][j]
            if p_ayb > 0 and p_a > 0 and p_a_b > 0:
                I_AyB += p_ayb * math.log2(p_a_b/p_a)
    
    return I_AyB



prob_priori = [0.7, 0.3]
matriz = [
    [0.7, 0.3],
    [0.4, 0.6]
]

H_ruido = genEquivocacionRuido(prob_priori, matriz)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()
H_perdida = genPerdida(prob_priori, matriz)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()
H_AyB = genEntropiaAfin(prob_priori, matriz)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()
I_AyB = genInfoMutua(prob_priori, matriz)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")