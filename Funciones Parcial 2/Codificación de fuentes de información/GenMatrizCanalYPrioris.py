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

def probabilidades_a_priori(mensaje):
    """
    Calcula P(a) para cada símbolo a del mensaje.
    Devuelve: (alfabeto, lista de probabilidades)
    """
    total = len(mensaje)
    alfabeto = []
    conteo = []

    for c in mensaje:
        if c in alfabeto:
            conteo[alfabeto.index(c)] += 1
        else:
            alfabeto.append(c)
            conteo.append(1)

    probs = [n / total for n in conteo]
    return alfabeto, probs

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

def imprimir_priori(alfabeto, probabilidades, titulo="Probabilidades a priori"):
    print(f"\n{titulo}:\n")
    for a, p in zip(alfabeto, probabilidades):
        print(f"P('{a}') = {p:.5f}")


print("Canal 1:")

entrada = "1101011001101010010101010100011111"
salida = "1001111111100011101101010111110110"
matriz = genMatrizCanal(entrada, salida)
alfa, prioris = probabilidades_a_priori(entrada)

imprimir_priori(alfa, prioris)
imprimir_matriz_canal(matriz, alf(entrada), alf(salida))

print()
print("Canal 2:")

entrada = "110101100110101100110101100111110011"
salida = "110021102110022010220121122100112011"
matriz = genMatrizCanal(entrada, salida)

alfa, prioris = probabilidades_a_priori(entrada)

imprimir_priori(alfa, prioris)
imprimir_matriz_canal(matriz, alf(entrada), alf(salida))
