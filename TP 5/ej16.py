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

def genEntropiaPriori(prob_priori):
    H = 0.0
    for p in prob_priori:
        if p > 0:
            H += p * math.log2(1 / p)
    return H

def genEntropiaSalida(prob_priori, matriz_canal):
    prob_salida = genProbSimSalida(prob_priori, matriz_canal)
    H_B = 0.0
    for p in prob_salida:
        if p > 0:  # evitar log2(0)
            H_B += p * math.log2(1/p)
    return H_B

# Canal C1
prob_priori_C1 = [0.14, 0.52, 0.34]
matriz_C1 = [
    [0.50, 0.30, 0.20],
    [0.00, 0.40, 0.60],
    [0.20, 0.80, 0.00]
]

# Canal C2
prob_priori_C2 = [0.25, 0.25, 0.50]
matriz_C2 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]

# Canal C3
prob_priori_C3 = [0.12, 0.24, 0.14, 0.50]
matriz_C3 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]

print("================== CANALES EJERCICIO 13 ==================")
print()
print("-----====================== C1 ======================-----")

H_A = genEntropiaPriori(prob_priori_C1)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

H_B = genEntropiaSalida(prob_priori_C1, matriz_C1)
print(f"Entropía de salida H(B): {H_B:.4f} bits")
print()

H_ruido = genEquivocacionRuido(prob_priori_C1, matriz_C1)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()

H_perdida = genPerdida(prob_priori_C1, matriz_C1)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()

H_AyB = genEntropiaAfin(prob_priori_C1, matriz_C1)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()

I_AyB = genInfoMutua(prob_priori_C1, matriz_C1)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")

print()
print("-----====================== C2 ======================-----")

H_A = genEntropiaPriori(prob_priori_C2)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

H_B = genEntropiaSalida(prob_priori_C2, matriz_C2)
print(f"Entropía de salida H(B): {H_B:.4f} bits")
print()

H_ruido = genEquivocacionRuido(prob_priori_C2, matriz_C2)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()

H_perdida = genPerdida(prob_priori_C2, matriz_C2)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()

H_AyB = genEntropiaAfin(prob_priori_C2, matriz_C2)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()

I_AyB = genInfoMutua(prob_priori_C2, matriz_C2)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")

print()
print("-----====================== C3 ======================-----")

H_A = genEntropiaPriori(prob_priori_C3)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

H_B = genEntropiaSalida(prob_priori_C3, matriz_C3)
print(f"Entropía de salida H(B): {H_B:.4f} bits")
print()

H_ruido = genEquivocacionRuido(prob_priori_C3, matriz_C3)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()

H_perdida = genPerdida(prob_priori_C3, matriz_C3)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()

H_AyB = genEntropiaAfin(prob_priori_C3, matriz_C3)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()

I_AyB = genInfoMutua(prob_priori_C3, matriz_C3)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")



# Canales del ejercicio 14

# Canal C1
prob_priori_C1 = [0.70, 0.30]
matriz_C1 = [
    [0.7, 0.3],
    [0.4, 0.6]
]

# Canal C2
prob_priori_C2 = [0.50, 0.50]
matriz_C2 = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]

# Canal C3
prob_priori_C3 = [0.25, 0.50, 0.25]
matriz_C3 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.5, 0.5, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

# Canal C4
prob_priori_C4 = [0.25, 0.25, 0.25, 0.25]
matriz_C4 = [
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0]
]

print()
print("================== CANALES EJERCICIO 14 ==================")
print()
print("-----====================== C1 ======================-----")

H_A = genEntropiaPriori(prob_priori_C1)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

H_B = genEntropiaSalida(prob_priori_C1, matriz_C1)
print(f"Entropía de salida H(B): {H_B:.4f} bits")
print()

H_ruido = genEquivocacionRuido(prob_priori_C1, matriz_C1)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()

H_perdida = genPerdida(prob_priori_C1, matriz_C1)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()

H_AyB = genEntropiaAfin(prob_priori_C1, matriz_C1)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()

I_AyB = genInfoMutua(prob_priori_C1, matriz_C1)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")

print()
print("-----====================== C2 ======================-----")

H_A = genEntropiaPriori(prob_priori_C2)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

H_B = genEntropiaSalida(prob_priori_C2, matriz_C2)
print(f"Entropía de salida H(B): {H_B:.4f} bits")
print()

H_ruido = genEquivocacionRuido(prob_priori_C2, matriz_C2)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()

H_perdida = genPerdida(prob_priori_C2, matriz_C2)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()

H_AyB = genEntropiaAfin(prob_priori_C2, matriz_C2)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()

I_AyB = genInfoMutua(prob_priori_C2, matriz_C2)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")

print()
print("-----====================== C3 ======================-----")

H_A = genEntropiaPriori(prob_priori_C3)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

H_B = genEntropiaSalida(prob_priori_C3, matriz_C3)
print(f"Entropía de salida H(B): {H_B:.4f} bits")
print()

H_ruido = genEquivocacionRuido(prob_priori_C3, matriz_C3)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()

H_perdida = genPerdida(prob_priori_C3, matriz_C3)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()

H_AyB = genEntropiaAfin(prob_priori_C3, matriz_C3)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()

I_AyB = genInfoMutua(prob_priori_C3, matriz_C3)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")

print()
print("-----====================== C4 ======================-----")

H_A = genEntropiaPriori(prob_priori_C4)
print(f"Entropía a priori H(A): {H_A:.4f} bits")
print()

H_B = genEntropiaSalida(prob_priori_C4, matriz_C4)
print(f"Entropía de salida H(B): {H_B:.4f} bits")
print()

H_ruido = genEquivocacionRuido(prob_priori_C4, matriz_C4)
print(f"Equivocación H(A|B) = {H_ruido:.4f} bits")
print()

H_perdida = genPerdida(prob_priori_C4, matriz_C4)
print(f"Pérdida H(B|A) = {H_perdida:.4f} bits")
print()

H_AyB = genEntropiaAfin(prob_priori_C4, matriz_C4)
print(f"H(A,B) = {H_AyB:.4f} bits")
print()

I_AyB = genInfoMutua(prob_priori_C4, matriz_C4)
print(f"I(A,B) = I(B,A) = {I_AyB:.4f} bits")