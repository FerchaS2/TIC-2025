def generar_codigo_con_paridades(mensaje):
    # armo la matriz con los caracteres
    matriz = []

    for c in mensaje:
        codigo_ascii = ord(c)                  # convierte el caracter a su valor ASCII (ej: 'A' → 65)
        binario = format(codigo_ascii, "07b")  # convierte 65 -> '1000001' (7 bits)
        bits = [int(b) for b in binario]       # convierte cada '1'/'0' en entero → [1,0,0,0,0,0,1]
        matriz.append(bits)                    # agrega esa lista como una fila a la matriz


    filas = len(matriz)
    columnas = 7

    # calcular VRC (por fila)
    for fila in matriz:
        paridad_v = sum(fila) % 2  # 1 si hay impar cantidad de 1s
        fila.append(paridad_v)     # agregamos la paridad como última columna

    # calcular fila de LRC
    lrc = []
    for col in range(columnas):
        suma_col = sum(matriz[fila][col] for fila in range(filas))
        lrc.append(suma_col % 2)   # paridad par por columna

    # bit de paridad cruzada
    suma_paridades = sum(f[-1] for f in matriz) + sum(lrc) # f[-1] sería la última columna de la fila, es decir el bit del VRC
    bit_cruzado = suma_paridades % 2

    lrc.append(bit_cruzado)
    matriz.insert(0, lrc)  # primera fila = LRC

    # convertir toda la matriz a un bytearray
    bits = []
    for fila in matriz:
        for bit in fila:
            bits.append(bit)

    bytes_list = []
    for i in range(0, len(bits), 8):
        grupo = bits[i:i+8]                     # agarro 8 bits
        binario = "".join(str(b) for b in grupo) # los convierto en '10100110'
        valor = int(binario, 2)                  # lo paso a entero (base 2)
        bytes_list.append(valor)                # lo añado al bytes_list

    bytearray_resultante = bytearray(bytes_list)


    return bytearray_resultante

def verificar_y_decodificar(bytearray_datos):
    """
    Recibe un bytearray con el formato del ejercicio 26a.
    Verifica y corrige errores de paridad (si se puede) y devuelve el mensaje original.
    Si hay errores no corregibles, devuelve "".
    """

    # Paso 1. Convertir los bytes en una cadena binaria completa
    bits_str = ""
    for byte in bytearray_datos:
        bits_str += format(byte, "08b")

    # Paso 2. Convertir la cadena binaria en una lista de enteros
    bits = [int(b) for b in bits_str]

    # Paso 3. Calcular dimensiones de la matriz
    # Tenemos 8 bits por fila (7 de datos + 1 de paridad VRC)
    columnas = 8
    filas = len(bits) // columnas

    # Paso 4. Crear la matriz de bits (lista de listas)
    matriz = []
    for i in range(filas):
        fila = bits[i * columnas:(i + 1) * columnas]
        matriz.append(fila)

    # Paso 5. Verificar paridades de filas (VRC)
    errores_fila = []
    for i in range(1, filas):  # empezamos en 1 porque la fila 0 es el LRC
        datos = matriz[i][:-1]  # todos menos el último (paridad)
        paridad = matriz[i][-1]
        suma = sum(datos) % 2
        if suma != paridad:
            errores_fila.append(i)

    # Paso 6. Verificar paridades de columnas (LRC)
    errores_columna = []
    for j in range(columnas - 1):  # no incluimos la última columna (paridades verticales)
        col_bits = [matriz[i][j] for i in range(1, filas)]  # ignoramos fila 0 (LRC)
        paridad_lrc = matriz[0][j]
        suma = sum(col_bits) % 2
        if suma != paridad_lrc:
            errores_columna.append(j)

    # Paso 7. Verificar la paridad cruzada (intersección)
    paridad_cruzada = matriz[0][-1]
    total_unos = sum(sum(fila[:-1]) for fila in matriz[1:]) + sum(matriz[0][:-1])
    if total_unos % 2 != paridad_cruzada:
        cruzado_error = True
    else:
        cruzado_error = False

    # Paso 8. Determinar qué hacer
    if not (len(errores_fila) == 0 and len(errores_columna) == 0 and not cruzado_error):
        if len(errores_fila) == 1 and len(errores_columna) == 1:
            # Error único corregible -> invertimos ese bit
            fila_err = errores_fila[0]
            col_err = errores_columna[0]
            matriz[fila_err][col_err] ^= 1  # flip
        else:
            # Demasiados errores -> imposible de corregir
            return ""

    # Paso 9. Reconstruir mensaje desde las filas de datos (ignorando paridades)
    mensaje = ""
    for i in range(1, filas):  # ignoramos fila 0 (LRC)
        bits_caracter = matriz[i][:-1]  # sin el bit de paridad
        valor = int("".join(str(b) for b in bits_caracter), 2)
        mensaje += chr(valor)

    return mensaje


msg = "LUNA"
codigo = generar_codigo_con_paridades(msg)

print("Mensaje original:", msg)
print("Bytes codificados:", list(codigo))
print("Matriz (bits por fila):")
for byte in codigo:
    print(format(byte, "08b"))

# ===== PRUEBA 1: Error único (corregible) =====
print("\n--- PRUEBA 1: Un bit modificado (corregible) ---")
codigo_error1 = bytearray(codigo)
# Invertimos 1 bit (por ejemplo, el bit menos significativo del segundo byte)
codigo_error1[1] ^= 0b00000010

print("Bytes con error:", list(codigo_error1))
print("Mensaje decodificado:", verificar_y_decodificar(codigo_error1))

# ===== PRUEBA 2: Error doble (no corregible) =====
print("\n--- PRUEBA 2: Dos bits modificados (NO corregible) ---")
codigo_error2 = bytearray(codigo)
# Invertimos 2 bits en distintos bytes
codigo_error2[1] ^= 0b00000010
codigo_error2[3] ^= 0b00010000

print("Bytes con errores:", list(codigo_error2))
print("Mensaje decodificado:", verificar_y_decodificar(codigo_error2))