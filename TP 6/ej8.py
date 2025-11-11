import math

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

def es_canal_uniforme(matriz):
    # Tomamos la primera fila como referencia, ordenada
    ref = sorted(matriz[0])
    
    # Verificamos el resto de las filas, ordenándolas
    for fila in matriz:
        if sorted(fila) != ref:
            return False
    
    return True

def capacidad_determinista(matriz):
    num_salidas = len(matriz[0])
    return math.log2(num_salidas)

def capacidad_sin_ruido(matriz):
    num_entradas = len(matriz)
    return math.log2(num_entradas)

def capacidad_uniforme(matriz):
    num_salidas = len(matriz[0])
    fila = matriz[0]  # cualquier fila sirve
    
    H_cond = 0
    for p in fila:
        if p > 0:
            H_cond += p * math.log2(1/p)
    
    return math.log2(num_salidas) - H_cond

def evaluar_canal(nombre, matriz):
    sr = es_canal_sin_ruido(matriz)
    det = es_canal_determinista(matriz)
    uni = es_canal_uniforme(matriz)

    print(f"\n================== Canal {nombre}: ==================")
    if not (sr or det or uni):
        print("-> No es ni sin ruido, ni determinista, ni uniforme")
    else:
        if sr:
            print("-> Canal sin ruido")
            print("Capacidad sin ruido: C = ", round(capacidad_sin_ruido(matriz),4))
            print()
        if det:
            print("-> Canal determinista")
            print("Capacidad determinista: C = ", round(capacidad_determinista(matriz),4))
            print()
        if uni:
            print("-> Canal uniforme")
            print("Capacidad uniforme: C = ", round(capacidad_uniforme(matriz),4))
            print()


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