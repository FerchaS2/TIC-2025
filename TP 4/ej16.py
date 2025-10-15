def getTasaCompresion(mensaje_original, mensaje_codificado):
    originalLen = len(mensaje_original)
    codificadoLen = len(mensaje_codificado)
    tasa = 0 if codificadoLen == 0 else originalLen / codificadoLen

    
    return tasa

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

msg = "ABACBAACABABAACBABA"
b_arr, _ = codificar(msg, ["A","B","C"], ["0","10","11"])

tasa = getTasaCompresion(msg, b_arr)
print("Tasa de compresión:", tasa)