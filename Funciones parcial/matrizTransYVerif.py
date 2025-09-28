import math
import random

# Dado un msg genera la matriz de trancisiones

def alf(mensaje):
    alfabeto = []
    
    for char in mensaje:
        if char not in alfabeto:
            alfabeto.append(char)

    return alfabeto

def getSumaCol(mat, col, n):
    sum = 0
    for i in range(n):
        sum += mat[i][col]
    return sum

def matriz(alfabeto, mensaje):
    n = len(alfabeto)
    mat = [[0.0 for _ in range(n)] for _ in range(n)]
    total = len(mensaje) - 1
    
    for i in range(total):
        mat[alfabeto.index(mensaje[i+1])][alfabeto.index(mensaje[i])] += 1.0
    
    for j in range(n):
        sumCol = getSumaCol(mat,j,n)
        for i in range(n):
            mat[i][j] /= sumCol
    
    return mat

msg = "BBAAACCAAABCCCAACCCBBACCAABBAA"
alfa = alf(msg)
print(alfa)

mat = matriz(alfa, msg)
print(mat)

# Genera una cadena aleatoria dado un alfabeto, una matriz de trancisiones y una longitud L

def genCadena(alfabeto, mat, L):
    n = len(alfabeto)
    act = random.choice(alfabeto)
    resultado = "".join(act)
    
    for _ in range(L-1):
        col = alfabeto.index(act)
        char = random.choices(alfabeto, weights=[mat[i][col] for i in range(n)], k = 1)[0]
        resultado += char
        act = char
    
    return resultado

cad = genCadena(alfa, mat, 10)
print(cad)

# Dada una matriz de transición devuelve si es o no de memoria nula, con cierto grado de tolerancia

"""
mat = [
    [0.3, 0.2, 0.5],
    [0.3, 0.2, 0.5],
    [0.3, 0.2, 0.5]
]
"""

def esNula(matriz, tol = 0.1):
    n = len(matriz)
    
    for i in range(n):
        ref = mat[i][0]
        for j in range(n):
            if abs(ref - mat[i][j]) > tol:
                return False
    
    return True

if esNula(mat, 0.1):
    print(f"{mat} es nula")
else:
    print(f"{mat} NO es nula")