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

C1 = ["11", "010", "00"]
C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
P = [0.5, 0.2, 0.3]
P2 = [P[i]*P[j] for i in range(len(P)) for j in range(len(P))]

print("Órden 1:")
if cumplePTShannon(C1, P, 1):
    print("Cumple el primer teorema de Shannon")
else:
    print("No cumple el primer teorema de Shannon")
print()
print("Órden 2:")
if cumplePTShannon(C2, P2, 1):
    print("Cumple el primer teorema de Shannon")
else:
    print("No cumple el primer teorema de Shannon")