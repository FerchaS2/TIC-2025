import math

def genInfo(ddp, r):
    return [-math.log(p,r) for p in ddp]

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

def gen_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def genLonMedia(longitudes, ddp):
    return sum(i*p for i,p in zip(longitudes,ddp))

def genRendimientoYRedundancia(codigo, ddp):
    r = len(set(''.join(codigo)))
    h = genEntropia(genInfo(ddp, r), ddp)
    l = genLonMedia(gen_longitudes(codigo), ddp)
    rendimiento = h/l
    return rendimiento, 1-rendimiento

C1 = ["11", "010", "00"]
C2 = ["10", "001", "110", "010", "0000", "0001", "111", "0110", "0111"]
P = [0.5, 0.2, 0.3]
P2 = [P[i]*P[j] for i in range(len(P)) for j in range(len(P))]

ren1, red1 = genRendimientoYRedundancia(C1, P)
print("Rendimiento 1 = ", ren1)
print("Redundancia 1 = ", red1)

ren2, red2 = genRendimientoYRedundancia(C2, P2)
print("Rendimiento 2 = ", ren2)
print("Redundancia 2 = ", red2)