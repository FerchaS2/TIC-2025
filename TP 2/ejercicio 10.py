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

#Ejercicio 10 ahora

N = 2

def genExtension(alfa, N):
    if N == 1:
        return alfa[:]
    else:
        anteriores = genExtension(alfa, N-1)
        return [s + c for s in anteriores for c in alfa] 

# extension = genExtension(alfa, N)
# print(extension)

def genExtensionCompleta(alfa, ddp, N):
    extension = genExtension(alfa,N)
    probs = []
    for palabra in extension:
        prob = 1
        for simbolo in palabra:
            idx = alfa.index(simbolo)
            prob *= ddp[idx]
        probs.append(prob)
    return extension, probs

extension, ddpext = genExtensionCompleta(alfa, prob, N)

print(extension)
print(ddpext)