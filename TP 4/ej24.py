# Codifica un caracter que viene por parámetro con 7 bits de ASCII y el octavo es la paridad

def codificacionCaracterAByte(caracter):
    """
    Convierte un caracter a su código ASCII (7 bits)
    y usa el bit menos significativo para almacenar la paridad (paridad par).
    """
    ascii_val = ord(caracter)
    paridad = bin(ascii_val).count("1") % 2
    valor_final = (ascii_val << 1) | paridad
    return bytes([valor_final])

def verificar_paridad(byte):
    """
    Verifica si el byte con paridad es correcto (paridad par).
    """
    valor = byte[0] # byte es como una lista cuya posición 0 es el byte que queremos
    bit_paridad = valor & 1
    ascii_val = valor >> 1
    paridad_byte = bin(ascii_val).count("1") % 2
    return bit_paridad == paridad_byte

b = codificacionCaracterAByte('A')
print(b)
print(list(b))

print(verificar_paridad(b))

# simulo un error cambiando el bit menos significativo
b_erroneo = bytes([b[0] ^ 1])
print(verificar_paridad(b_erroneo))
