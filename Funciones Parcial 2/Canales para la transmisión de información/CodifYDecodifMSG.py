# dado un alfabeto fuente y su codificación codificar y decodificar un msg

def alf(mensaje):
    alfabeto = []
    
    for char in mensaje:
        if char not in alfabeto:
            alfabeto.append(char)
    
    return alfabeto

def codificar(mensaje, alfabeto, codigos):
    # Construir cadena binaria completa
    aux = "".join(codigos[alfabeto.index(char)] for char in mensaje)
    longitud_original = len(aux)  # guardamos la longitud real

    # Relleno con 0 hasta múltiplo de 8
    if len(aux) % 8 != 0:
        aux = aux.ljust((len(aux) + 7) // 8 * 8, "0")

    bytes_list = [int(aux[i:i+8], 2) for i in range(0, len(aux), 8)]
    bytes_array = bytearray(bytes_list)
    
    return bytes_array, longitud_original



def decodificar(bytes_array, alfabeto, codigos, longitud_bits):
    # Reconstruyo el string binario
    bits = "".join(format(byte, "08b") for byte in bytes_array)
    bits = bits[:longitud_bits]  # recortar los ceros de relleno

    mensaje = ""
    buffer = ""

    # Voy leyendo bit a bit
    for bit in bits:
        buffer += bit
        # si el buffer coincide con un código conocido, lo traduzco
        if buffer in codigos:
            idx = codigos.index(buffer)
            mensaje += alfabeto[idx]
            buffer = ""

    return mensaje

alfa = "ABC"
alfabeto = alf(alfa)
codigo = ["0", "10", "11"]
msg = "ABACBAACABABAACBABA"

b_arr, long_bits = codificar(msg, alfabeto, codigo)
print("Bytes:", list(b_arr))
print("Bits:", "".join(format(byte, "08b") for byte in b_arr))

decodificado = decodificar(b_arr, alfabeto, codigo, long_bits)
print("Decodificado:", decodificado)