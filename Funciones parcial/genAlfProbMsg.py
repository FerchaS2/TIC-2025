# Dado un msg genera su alfabeto y su distribución de probabilidades

def alf_y_prob(mensaje):
    alfabeto = []
    apariciones = []
    
    for char in mensaje:
        if char in alfabeto:
            i = alfabeto.index(char)
            apariciones[i] += 1
        else:
            alfabeto.append(char)
            apariciones.append(1)
    
    total = len(mensaje)
    probabilidades = [c/total for c in apariciones]
    
    return alfabeto,probabilidades

# Ejemplo de uso

msg = "ABDAACAABACADAABDAADABDAAABDCDCDCDC"
alfa,prob = alf_y_prob(msg)

print("Alfabeto: ", alfa)
from fractions import Fraction
print("Probabilidades: ", [Fraction(p).limit_denominator() for p in prob])


# Generar simulación de mensaje dado un alfabeto y su ddp.

import random

def genmsg(alf, prob, longitud):
    return ''.join(random.choices(alf, weights=prob, k=longitud))

# Longitud es la del msg

msg_sim = genmsg(alfa, prob, 20)
print(msg_sim)