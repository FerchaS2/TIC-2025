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

msg = "UUOOOOAAAIEUUUU"
comprimido = comprimirRLC(msg)

print(list(comprimido))
