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

def imprimir_matriz_canal(matriz, alfabeto_entrada, alfabeto_salida, titulo="Matriz de representación del canal"):
    """
    Imprime una matriz de canal con encabezados y formato tabular.
    """
    print(f"\n{titulo}:\n")

    # Encabezado de columnas
    print("       ", end="")
    for s in alfabeto_salida:
        print(f"{s:^8}", end="")
    print("\n" + "-" * (9 * (len(alfabeto_salida) + 1)))

    # Filas con etiquetas
    for i, fila in enumerate(matriz):
        print(f"{alfabeto_entrada[i]:>3} |", end=" ")
        for valor in fila:
            print(f"{valor:>8.3f}", end="")
        print()

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

def genMatrizSimultaneos(prob_priori, matriz_canal):
    n = len(matriz_canal)      # cantidad de símbolos de entrada
    m = len(matriz_canal[0])   # cantidad de símbolos de salida
    matriz = [[0.0 for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            matriz[i][j] = matriz_canal[i][j] * prob_priori[i]
    
    return matriz

def imprimir_probabilidades_simbolos(alfabeto, probabilidades):
    print("Probabilidad de los símbolos:")
    for s, p in zip(alfabeto, probabilidades):
        print(f"P({s}) = {p:.3f}")


print("============= Canal 1 =============")

entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"
alfa, prob = alf_y_prob(entrada)
matriz = genMatrizCanal(entrada, salida)
prob_simbolos_salida = genProbSimSalida(prob, matriz)

imprimir_matriz_canal(matriz, alf(entrada), alf(salida))
print()
imprimir_probabilidades_simbolos(alf(salida), prob_simbolos_salida)
print()
imprimir_matriz_canal(genMatrizPosteriori(prob, matriz), alf(entrada), alf(salida), "Matriz de probabilidades a posteriori")
print()
imprimir_matriz_canal(genMatrizSimultaneos(prob, matriz), alf(entrada), alf(salida), "Matriz de probabilidades simultáneas")

print()
print("============= Canal 2 =============")

entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"
alfa, prob = alf_y_prob(entrada)
matriz = genMatrizCanal(entrada, salida)
prob_simbolos_salida = genProbSimSalida(prob, matriz)

imprimir_matriz_canal(matriz, alf(entrada), alf(salida))
print()
imprimir_probabilidades_simbolos(alf(salida), prob_simbolos_salida)
print()
imprimir_matriz_canal(genMatrizPosteriori(prob, matriz), alf(entrada), alf(salida), "Matriz de probabilidades a posteriori")
print()
imprimir_matriz_canal(genMatrizSimultaneos(prob, matriz), alf(entrada), alf(salida), "Matriz de probabilidades simultáneas")

print()
print("============= Canal 3 =============")

entrada = "abcacaabbcacaabcacaaabcaca"
salida = "01010110011001000100010011"
alfa, prob = alf_y_prob(entrada)
matriz = genMatrizCanal(entrada, salida)
prob_simbolos_salida = genProbSimSalida(prob, matriz)

imprimir_matriz_canal(matriz, alf(entrada), alf(salida))
print()
imprimir_probabilidades_simbolos(alf(salida), prob_simbolos_salida)
print()
imprimir_matriz_canal(genMatrizPosteriori(prob, matriz), alf(entrada), alf(salida), "Matriz de probabilidades a posteriori")
print()
imprimir_matriz_canal(genMatrizSimultaneos(prob, matriz), alf(entrada), alf(salida), "Matriz de probabilidades simultáneas")