# Dada una lista con las cadenas de código, retorna:
# - la distancia de Hamming 
# - la cantidad de errores que se pueden detectar 
# - la cantidad de errores que se pueden corregir


# Devuelve la distancia de Hamming entre dos cadenas binarias del mismo largo.

def distancia_hamming(c1, c2):
    return sum(b1 != b2 for b1, b2 in zip(c1, c2))

# Devuelve la distancia mínima, errores detectables y corregibles.

def analizar_codigo(codigos):
    d_min = float("inf")

    for i in range(len(codigos)):
        for j in range(i + 1, len(codigos)):
            d = distancia_hamming(codigos[i], codigos[j])
            if d < d_min:
                d_min = d

    detectables = d_min - 1
    corregibles = (d_min - 1) // 2 # // es dividión entera

    return d_min, detectables, corregibles


# Ejemplo de uso
codigo = ["000", "011", "101", "110"]
d, det, cor = analizar_codigo(codigo)

print("Distancia mínima de Hamming =", d)
print("Errores detectables =", det)
print("Errores corregibles =", cor)
