def getTasaCompresion(mensaje_original, mensaje_codificado):
    originalLen = len(mensaje_original)
    codificadoLen = len(mensaje_codificado)
    tasa = 0 if codificadoLen == 0 else originalLen / codificadoLen

    
    return tasa

def comprimirRLC(mensaje):
    bytes_list = []
    actual = mensaje[0]
    contador = 1

    for c in mensaje[1:]:
        if c == actual and contador < 255:  # 255 = máx. valor que cabe en 1 byte
            contador += 1
        else:
            # agrego el par (caracter ASCII, cantidad)
            bytes_list.append(ord(actual))
            bytes_list.append(contador)
            actual = c
            contador = 1

    # agregar el último par
    bytes_list.append(ord(actual))
    bytes_list.append(contador)

    return bytearray(bytes_list)

# Mensajes
msgA = "XXXYZZZZ"
msgB = "AAAABBBCCDAA"
msgC = "UUOOOOAAAIEUUUU"

# Compresiones
codA = comprimirRLC(msgA)
codB = comprimirRLC(msgB)
codC = comprimirRLC(msgC)

# Resultados
print("Mensaje A:", msgA)
print("Codificación:", list(codA))
print("Tasa de compresión =", getTasaCompresion(msgA, codA))
print()

print("Mensaje B:", msgB)
print("Codificación:", list(codB))
print("Tasa de compresión =", getTasaCompresion(msgB, codB))
print()

print("Mensaje C:", msgC)
print("Codificación:", list(codC))
print("Tasa de compresión =", getTasaCompresion(msgC, codC))