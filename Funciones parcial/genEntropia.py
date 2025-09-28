import math

# Generar entropía dada una lista con la cantidad de info y una lista con la distribución de probabilidades

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

# Generar entropía binaria dado un w (omega)

def genInfo(ddp, r):
    return [-math.log(p,r) for p in ddp]

def genEntropiaBinaria(w):
    ddp = [w,1-w]
    info = genInfo(ddp, 2)
    return genEntropia(info, ddp)