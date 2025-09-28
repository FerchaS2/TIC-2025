import math

# Dado una codificación y sus probabilidades calcula su entropía y su longitud media

def genInfo(ddp, r):
    return [-math.log(p,r) for p in ddp]

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

def gen_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def genLonMedia(longitudes, ddp):
    return sum(i*p for i,p in zip(longitudes,ddp))

codigo = ["==", "<", "<=", ">", ">=", "<>"]
ddp = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]
r = len(set(''.join(codigo))) # join concatena todos los elementos en un string y con set elimina duplicados

entropia = genEntropia(genInfo(ddp,r), ddp)
print(entropia)

longitudes = gen_longitudes(codigo)

print(genLonMedia(longitudes, ddp))