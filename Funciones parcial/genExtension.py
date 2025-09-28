# Dado un alfabeto crea una extensión de orden N

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
N = 2

def genExtension(alfa, N):
    if N == 1:
        return alfa[:]
    else:
        anteriores = genExtension(alfa, N-1)
        return [s + c for s in anteriores for c in alfa] 

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