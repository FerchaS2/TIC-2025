#Inciso A

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


msg = "ABDAACAABACADAABDAADABDAAABDCDCDCDC"
alfa,prob = alf_y_prob(msg)
print("Alfabeto: ", alfa)
from fractions import Fraction
print("Probabilidades: ", [Fraction(p).limit_denominator() for p in prob])

#Inciso B

import random

def genmsg(alf, prob, longitud):
    return ''.join(random.choices(alf, weights=prob, k=longitud))

msg_sim = genmsg(alfa, prob, 20)
print(msg_sim)