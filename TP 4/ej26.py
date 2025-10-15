""""
Explicaciónde texto_a_matriz_bits

    -   ord(c) → convierte carácter a número ASCII
    
    -   format(...,"07b") → pasa ese número a binario de 7 bits
    
    -   map(int,...) → convierte los caracteres '0' y '1' en enteros
    
    -   list(...) → los mete en una lista
    
    -   [ ... for c in mensaje ] → repite eso para todos los caracteres
"""

def texto_a_matriz_bits(mensaje):
    """Convierte un mensaje en una matriz de bits (7 columnas por carácter)."""
    return [list(map(int, format(ord(c), "07b"))) for c in mensaje]


def agregar_VRC(matriz):
    """Agrega el bit de paridad (VRC) a cada fila."""
    for fila in matriz:
        paridad = sum(fila) % 2  # paridad par
        fila.append(paridad)


def calcular_LRC(matriz):
    """Calcula la fila LRC (paridad vertical de cada columna)."""
    n_cols = len(matriz[0])
    lrc = []
    for col in range(n_cols):
        suma = sum(fila[col] for fila in matriz)
        lrc.append(suma % 2)
    return lrc


def agregar_paridad_cruzada(lrc, matriz):
    """Agrega el bit de paridad cruzada en la esquina superior derecha."""
    total_bits = sum(sum(fila[:-1]) for fila in matriz) + sum(lrc[:-1])
    cruzado = total_bits % 2
    lrc[-1] = cruzado


def generar_matriz_paridad(mensaje):
    """
    Genera una matriz con bits de paridad:
    - 1ra fila = LRC
    - Última columna = VRC
    - Esquina superior derecha = bit de paridad cruzada
    Retorna un bytearray con las filas convertidas a bytes.
    """
    # convertir texto a matriz
    matriz = texto_a_matriz_bits(mensaje)
    agregar_VRC(matriz)
    lrc = calcular_LRC(matriz)
    lrc.append(0)  # placeholder para el bit cruzado
    agregar_paridad_cruzada(lrc, matriz)

    # insertar LRC en la primera fila
    matriz.insert(0, lrc)

    # convertir filas a bytes
    bytes_list = [int("".join(map(str, fila)), 2) for fila in matriz]
    return bytearray(bytes_list)

msg = "CASA"
b = generar_matriz_paridad(msg)

print("Bytearray resultante:", list(b))
print("En binario:")
for byte in b:
    print(format(byte, "08b"))
