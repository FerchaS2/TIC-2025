import math

# Dado el código, su ddp y el orden de la extensión N verifica si cumple el Primer Teorema de Shannon.

def genInfo(ddp, r):
    return [-math.log(p,r) for p in ddp]

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

def gen_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def genLonMedia(longitudes, ddp):
    return sum(i*p for i,p in zip(longitudes,ddp))

def genExtension(alfa, N):
    if N == 1:
        return [[a] for a in alfa]
    else:
        anteriores = genExtension(alfa, N-1)
        return [a + [b] for a in anteriores for b in alfa]

def genExtensionCompleta(alfa, ddp, N):
    extension = genExtension(alfa,N)
    probs = []
    for palabra in extension:
        prob = 1.0
        for simbolo in palabra:
            idx = alfa.index(simbolo)
            prob *= ddp[idx]
        probs.append(prob)
    
    extension = ["".join(palabra) for palabra in extension]
    return extension, probs

def cumplePTShannon(codigo, ddp, N):
    r = len(set(''.join(codigo))) # join concatena todos los elementos en un string y con set elimina duplicados
    entropia = genEntropia(genInfo(ddp, r), ddp)
    extension, ddpext = genExtensionCompleta(codigo, ddp, N)
    lonMedia = genLonMedia(gen_longitudes(extension), ddpext)
    print("Entropia = ", entropia)
    print("Longitud media (ext) = ", lonMedia)
    return entropia <= lonMedia/N and lonMedia/N < entropia + 1/N

probs = [0.3, 0.1, 0.4, 0.2]
codigo = ["BA", "CAB", "A", "CBA"]

print("Órden 1:")
if cumplePTShannon(codigo, probs, 1):
    print("Cumple el primer teorema de Shannon")
else:
    print("No cumple el primer teorema de Shannon")
print()
print("Órden 2:")
if cumplePTShannon(codigo, probs, 2):
    print("Cumple el primer teorema de Shannon")
else:
    print("No cumple el primer teorema de Shannon")