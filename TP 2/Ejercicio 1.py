import math

#Inciso A

def genInfo(ddp):
    return [-math.log2(p) for p in ddp]

ddp = [0.1, 0.3, 0.1, 0.5]
print(ddp)

cantinfo = genInfo(ddp)
print(cantinfo)

#Inciso B

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

entropia = genEntropia(cantinfo, ddp)
print(entropia)