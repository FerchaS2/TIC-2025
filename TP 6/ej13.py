def prob_error(matriz, probs_priori):
    """
    Calcula P_E según regla de decisión de máxima posibilidad:
    para cada salida b se elige a* = máx de la columna (si hay empate, el primero),
    y se suma P(b|a)P(a) para todos a != a*.
    
    """
    n_entradas = len(matriz)
    n_salidas = len(matriz[0])
    prob_error = 0.0

    for b in range(n_salidas):
        # elegir a* = índice del máximo en la columna b (primera ocurrencia si empate)
        a_star = max(range(n_entradas), key=lambda a: matriz[a][b])

        # sumar contribuciones de error para todos a != a_star
        for a in range(n_entradas):
            if a != a_star:
                prob_error += matriz[a][b] * probs_priori[a]

    return prob_error

matriz = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.3, 0.3, 0.4]
]

probs_priori_1 = [1/3, 1/3, 1/3]
probs_priori_2 = [1/8, 3/8, 4/8]
probs_priori_3 = [4/15, 3/15, 8/15]

print("Probabilidad de error 1 =", round(prob_error(matriz, probs_priori_1), 4))
print()
print("Probabilidad de error 2 =", round(prob_error(matriz, probs_priori_2), 4))
print()
print("Probabilidad de error 3 =", round(prob_error(matriz, probs_priori_3), 4))
print()