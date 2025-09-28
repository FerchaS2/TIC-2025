import math

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

def genInfo(prob):
    return [-math.log2(p) for p in prob]

cantinfo = genInfo(prob)
print(cantinfo)

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

entropia = genEntropia(cantinfo, prob)
print(entropia)