def es_canal_sin_ruido(matriz):
    columnas = zip(*matriz)  # Transponer para recorrer columnas

    for col in columnas:
        valores_no_cero = sum(1 for x in col if x != 0)
        if valores_no_cero > 1:
            return False

    return True

def es_canal_determinista(matriz):
    for fila in matriz:
        valores_no_cero = sum(1 for x in fila if x != 0)
        if valores_no_cero > 1:
            return False

    return True

canal1 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]

print(es_canal_sin_ruido(canal1))      # True o False según la matriz
print(es_canal_determinista(canal1))
