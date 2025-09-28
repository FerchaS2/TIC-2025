import math

# Generar info teórico dado un r el cual es la base del logarítmo

def genInfo(ddp, r):
    return [-math.log(p,r) for p in ddp]

# Generar info práctico para detectar compactos

def genInfo(ddp, r):
    return [math.ceil(-math.log(p,r)) for p in ddp]