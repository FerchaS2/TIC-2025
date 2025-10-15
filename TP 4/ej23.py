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

codigo1 = ["0100100", "0101000", "0010010", "0100000"]
codigo2 = ["0100100", "0010010", "0101000", "0100001"]
codigo3 = ["0110000", "0000011", "0101101", "0100110"]

d1, det1, cor1 = analizar_codigo(codigo1)
print("Código 1:")
print("Distancia mínima de Hamming =", d1)
print("Errores detectables =", det1)
print("Errores corregibles =", cor1)
print()

d2, det2, cor2 = analizar_codigo(codigo2)
print("Código 2:")
print("Distancia mínima de Hamming =", d2)
print("Errores detectables =", det2)
print("Errores corregibles =", cor2)
print()

d3, det3, cor3 = analizar_codigo(codigo3)
print("Código 3:")
print("Distancia mínima de Hamming =", d3)
print("Errores detectables =", det3)
print("Errores corregibles =", cor3)