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

P = [0.2, 0.15, 0.1, 0.3, 0.25]
C1  = ["01", "111", "110", "101", "100"]
C2  = ["00", "01", "10", "110", "111"]
C3  = ["0110", "010", "0111", "1", "00"]
C4  = ["11", "001", "000", "10", "01"]

ren, red = genRendimientoYRedundancia(C1, P)
print("Rendimiento 1 = ", ren)
print("Redundancia 1 = ", red)
print()
ren, red = genRendimientoYRedundancia(C2, P)
print("Rendimiento 2 = ", ren)
print("Redundancia 2 = ", red)
print()
ren, red = genRendimientoYRedundancia(C3, P)
print("Rendimiento 3 = ", ren)
print("Redundancia 3 = ", red)
print()
ren, red = genRendimientoYRedundancia(C4, P)
print("Rendimiento 4 = ", ren)
print("Redundancia 4 = ", red)