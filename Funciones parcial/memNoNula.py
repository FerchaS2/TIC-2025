# Genera vector estacionario de la fuente de la fuente con memoria y calcula su entropía
# Todo en base a su matriz de transición
# El vector estacionario es un vector columna, como también lo es el vector estacionario resultante

import math

matriz = [
    [0.5, 1/3, 0],
    [0.5, 1/3, 1],
    [0, 1/3, 0]
]


def genVecEstacionario(matriz, tol = 1e-9, max_it = 100000):
    n = len(matriz)
    vecp = [1.0/n] * n
    
    for ite in range(max_it):
        vecaux = [0.0] * n
        for j in range(n):
            suma = 0.0
            for i in range(n):
                suma += vecp[i] * matriz[j][i]
            vecaux[j] = suma
        
        dif = 0.0
        
        for i in range(n):
            dif += abs(vecaux[i] - vecp[i])
        
        #print(f"iter {ite+1:4d}  cambio={dif:.12f}  v={['%.6f'%x for x in vecaux]}")
        
        if dif <= tol:
            return vecaux
        
        vecp = vecaux
    
    return vecp

vecp = genVecEstacionario(matriz, tol=1e-9, max_it=100000)
print(vecp)

def genEntropiaFuente(matriz, vecp):
    n = len(matriz)
    vecaux = [0.0] * n
    
    for i in range(n):
        for j in range(n):
            if matriz[j][i] != 0:
                vecaux[i] += matriz[j][i] * math.log(1.0/matriz[j][i],2)

    sumEnt = 0.0
    
    for i in range(n):
        sumEnt += vecaux[i] * vecp[i]
    
    return sumEnt

print(f"Entropia de la fuente = {genEntropiaFuente(matriz, vecp)}")