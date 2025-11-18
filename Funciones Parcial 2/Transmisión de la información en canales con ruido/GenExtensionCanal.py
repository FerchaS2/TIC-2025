import itertools

def extension_canal(matriz, n, alf_in_base=None, alf_out_base=None):
    """
    Genera la extensión de orden n de un canal.

    matriz: matriz base P(b|a)
    n: orden de la extensión
    alf_in_base: lista con alfabeto de entrada (opcional)
    alf_out_base: lista con alfabeto de salida (opcional)
    """

    r = len(matriz)
    s = len(matriz[0])

    if alf_in_base is None:
        alf_in_base = list(range(r))
    if alf_out_base is None:
        alf_out_base = list(range(s))

    # Alfabetos extendidos (listas de tuplas)
    alf_in_ext = list(itertools.product(alf_in_base, repeat=n))
    alf_out_ext = list(itertools.product(alf_out_base, repeat=n))

    matriz_ext = []

    for entrada in alf_in_ext:
        fila = []
        for salida in alf_out_ext:
            prob = 1.0
            for (ai, bj) in zip(entrada, salida):
                i = alf_in_base.index(ai)
                j = alf_out_base.index(bj)
                prob *= matriz[i][j]
            fila.append(prob)
        matriz_ext.append(fila)

    return matriz_ext, alf_in_ext, alf_out_ext


def imprimir_extension_matriz(matriz_ext, alf_in_ext, alf_out_ext, titulo="Matriz extendida del canal"):
    """
    Imprime la matriz extendida en formato de tabla.
    """

    print("\n" + titulo)
    print("-" * len(titulo))

    # Encabezado
    print(f"{'Entrada ↓':<12} |  ", end="")
    for salida in alf_out_ext:
        salida_str = ''.join(map(str, salida))
        print(f"  {salida_str:<8}", end="")
    print()

    print("-" * (15 + 12 * len(alf_out_ext)))

    # Filas
    for entrada, fila in zip(alf_in_ext, matriz_ext):
        entrada_str = ''.join(map(str, entrada))
        print(f"{entrada_str:<12} |", end="")
        for prob in fila:
            print(f" {prob:>8.5f}", end="")
        print()


matriz = [
    [0.9, 0.1],
    [0.2, 0.8]
]

mat_ext, A2, B2 = extension_canal(matriz, 2)

imprimir_extension_matriz(mat_ext, A2, B2)

M = [
    [0.7, 0.3],
    [0.1, 0.9],
    [0.5, 0.5]
]

# Alfabetos base
alf_in = ['A', 'B', 'C']
alf_out = ['X', 'Y']

# Extensión de orden 2
mat_ext, A2, B2 = extension_canal(M, 2, alf_in, alf_out)

# Imprimir como matriz
imprimir_extension_matriz(mat_ext, A2, B2, "Extensión de orden 2 del canal")
