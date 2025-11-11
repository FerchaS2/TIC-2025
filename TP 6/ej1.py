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

def evaluar_canal(nombre, matriz):
    sr = es_canal_sin_ruido(matriz)
    det = es_canal_determinista(matriz)

    print(f"\nCanal {nombre}:")
    if sr and det:
        print("➡ Canal sin ruido")
        print("➡ Canal determinista")
    elif sr:
        print("➡ Canal sin ruido")
    elif det:
        print("➡ Canal determinista")
    else:
        print("➡ No es sin ruido ni determinista")


# Canal M1
M1 = [
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
    [0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0]
]

# Canal M2
M2 = [
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 0.2, 0.0, 0.8],
    [0.0, 0.0, 1.0, 0.0]
]

# Canal M3
M3 = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]

# Canal M4
M4 = [
    [0.0, 0.0, 1.0, 0.0],
    [1.0, 0.0, 0.0, 0.0],
    [0.0, 1.0, 0.0, 0.0],
    [0.0, 0.0, 0.0, 1.0]
]

canales = {
    "M1": M1,
    "M2": M2,
    "M3": M3,
    "M4": M4
}

for nombre, matriz in canales.items():
    evaluar_canal(nombre, matriz)
