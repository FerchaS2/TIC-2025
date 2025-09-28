import math

def genInfo(ddp):
    return [-math.log2(p) for p in ddp]

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

def genEntropiaBinaria(w):
    ddp = [w,1-w]
    info = genInfo(ddp)
    return genEntropia(info, ddp)

w = 0.75
entropia = genEntropiaBinaria(w)
print(entropia)