def columnas_se_pueden_combinar(matriz, c1, c2):
    proporcion = None

    for fila in matriz:
        a = fila[c1]
        b = fila[c2]

        # Si ambos son cero no aportan información -> los ignoramos
        if not (a == 0 and b == 0):
            # Si uno es cero y el otro no -> NO pueden ser proporcionales
            if a == 0 or b == 0:
                return False

            # Calcular proporción
            nueva_prop = b / a

            if proporcion is None:
                proporcion = nueva_prop  # guardamos la primera proporción
            else:
                if abs(nueva_prop - proporcion) > 1e-9:
                    return False  # proporciones distintas -> NO sirve

    return True  # si llegamos acá -> todas proporcionales

def construir_determinante(m, c1, c2):
    """
    Construye D de forma (m x (m-1)) que agrupa columnas c1 y c2 en UNA nueva columna.
    Retorna D como lista de filas.
    """
    m_new = m - 1
    # mapping[j] = índice de la columna nueva donde va la columna original j
    mapping = [None] * m

    new_idx = 0
    combined_idx = None  # índice asignado a la columna combinada (cuando aparezca la 1ra)
    for j in range(m):
        if j == c1 or j == c2:
            if combined_idx is None:
                # primera de las dos columnas combinadas -> le asignamos una nueva columna
                combined_idx = new_idx
                mapping[j] = combined_idx
                new_idx += 1
            else:
                # segunda de las columnas combinadas -> usa el mismo índice que la primera
                mapping[j] = combined_idx
        else:
            # columna no combinada -> le asignamos la siguiente columna nueva
            mapping[j] = new_idx
            new_idx += 1

    # Ahora construimos D (m filas x m_new columnas) según el mapping
    D = [[0 for _ in range(m_new)] for _ in range(m)]
    for j in range(m):
        D[j][mapping[j]] = 1

    return D


def multiplicar_matrices(A, B):
    """Multiplica A (n x m) por B (m x p) y devuelve (n x p)."""
    n = len(A)
    m = len(A[0])
    # suponemos B tiene m filas
    p = len(B[0])
    C = [[0.0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            s = 0.0
            for k in range(m):
                s += A[i][k] * B[k][j]
            C[i][j] = s
    return C


def reducir_columnas_con_determinante(M, c1, c2):
    """
    Devuelve (D, M_reducida) donde D es la matriz determinante (m x (m-1))
    y M_reducida = M @ D.
    """
    n = len(M)
    m = len(M[0])
    D = construir_determinante(m, c1, c2)
    M_reducida = multiplicar_matrices(M, D)
    return D, M_reducida

M = [
    [1/6, 1/3, 1/2, 0],
    [1/12, 1/6, 1/4, 1/2]
]

print(columnas_se_pueden_combinar(M, 0, 1))

# juntar columnas 0 y 1
D, M_reducida = reducir_columnas_con_determinante(M, 0, 1)

print("D =")
for fila in D:
    print(fila)

print("\nM reducida =")
for fila in M_reducida:
    print([round(x,3) for x in fila])