import math

def es_canal_uniforme(matriz):
    # Tomamos la primera fila como referencia, ordenada
    ref = sorted(matriz[0])
    
    # Verificamos el resto de las filas, ordenándolas
    for fila in matriz:
        if sorted(fila) != ref:
            return False
    
    return True

def capacidad_determinista(matriz):
    num_salidas = len(matriz[0])
    return math.log2(num_salidas)

def capacidad_sin_ruido(matriz):
    num_entradas = len(matriz)
    return math.log2(num_entradas)

def capacidad_uniforme(matriz):
    num_salidas = len(matriz[0])
    fila = matriz[0]  # cualquier fila sirve
    
    H_cond = 0
    for p in fila:
        if p > 0:
            H_cond += p * math.log2(1/p)
    
    return math.log2(num_salidas) - H_cond


M = [
    [1/3, 1/6, 1/2],
    [1/2, 1/3, 1/6]
]

print(es_canal_uniforme(M))