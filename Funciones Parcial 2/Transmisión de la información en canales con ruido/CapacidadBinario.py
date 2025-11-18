import math

def genProbSimSalida(prob_priori, matriz_canal):
    n = len(matriz_canal[0]) # cantidad de simbolos de salida
    prob_simbolos = [0] * n
    
    for j in range(n):
        for i in range(len(prob_priori)):
            prob_simbolos[j] += prob_priori[i] * matriz_canal[i][j]
    
    return prob_simbolos

def genMatrizSimultaneos(prob_priori, matriz_canal):
    n = len(matriz_canal)      # cantidad de símbolos de entrada
    m = len(matriz_canal[0])   # cantidad de símbolos de salida
    matriz = [[0.0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            matriz[i][j] = matriz_canal[i][j] * prob_priori[i]
    
    return matriz

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

def estimar_capacidad_binaria(matriz_canal, paso):
    max_cap = -1
    mejor_prob = None

    p = 0.0
    while p <= 1.0 + 1e-9:
        prob_priori = [p, 1 - p]
        
        I = genInfoMutua(prob_priori, matriz_canal)

        if I > max_cap:
            max_cap = I
            mejor_prob = prob_priori[:]

        p += paso

    return max_cap, mejor_prob

def mostrar_resultado(matriz, paso, nombre):
    cap, prob = estimar_capacidad_binaria(matriz, paso)

    print(f"\n=================== {nombre} ===================")
    print("Matriz:")
    for fila in matriz:
        print(fila)
    print()
    print(f"Capacidad estimada: {cap:.4f} bits")
    print(f"P(a0): {prob[0]:.4f}, P(a1): {prob[1]:.4f}")


M1 = [
    [0.60, 0.40],
    [0.20, 0.80]
]

M2 = [
    [0.25, 0.75],
    [0.90, 0.10]
]

M3 = [
    [0.51, 0.49],
    [0.72, 0.28]
]

M4 = [
    [0.77, 0.23],
    [0.20, 0.80]
]

paso = 0.0001

mostrar_resultado(M1, paso, "Canal 1")
mostrar_resultado(M2, paso, "Canal 2")
mostrar_resultado(M3, paso, "Canal 3")
mostrar_resultado(M4, paso, "Canal 4")