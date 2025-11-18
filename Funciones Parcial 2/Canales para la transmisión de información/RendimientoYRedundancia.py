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

probs = [0.3, 0.1, 0.4, 0.2]
codigo = ["BA", "CAB", "A", "CBA"]

ren, red = genRendimientoYRedundancia(codigo, probs)
print("Rendimiento = ", ren)
print("Redundancia = ", red)