def alf_y_prob(mensaje):
    alfabeto = []
    apariciones = []
    
    for char in mensaje:
        if char in alfabeto:
            i = alfabeto.index(char)
            apariciones[i] += 1
        else:
            alfabeto.append(char)
            apariciones.append(1)
    
    total = len(mensaje)
    probabilidades = [c/total for c in apariciones]
    
    return alfabeto,probabilidades

def alf(mensaje):
    alfabeto = []
    
    for char in mensaje:
        if char not in alfabeto:
            alfabeto.append(char)
    
    return alfabeto

def genMatrizCanal(entrada, salida):
    alf_entrada, prob_entrada = alf_y_prob(entrada)
    alf_salida = alf(salida)
    
    matriz = [[0.0 for _ in range(len(alf_salida))] for _ in range(len(alf_entrada))]

    # print(matriz)
    for ce, cs in zip(entrada, salida):
        matriz[alf_entrada.index(ce)][alf_salida.index(cs)] += 1
    
    # print(matriz)
    
    for i in range(len(matriz)):
        suma = sum(matriz[i])
        for k in range(len(alf_salida)):
            matriz[i][k] /= suma
    
    return matriz


entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"
matriz = genMatrizCanal(entrada, salida)

print("Matriz de representación del canal:\n")

# Imprimir encabezado de columnas
print("       ", end="")
for s in alf(salida):
    print(f"{s:^8}", end="")
print("\n" + "-" * (9 * (len(alf(salida)) + 1)))

# Imprimir filas con etiquetas
for i, fila in enumerate(matriz):
    print(f"{alf(entrada)[i]:>3} |", end=" ")
    for valor in fila:
        print(f"{valor:>8.3f}", end="")
    print()
