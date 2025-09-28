import math

#Inciso A   lo mismo que el ej1 del tp2 pero modificando la base del logaritmo por r

def genInfo(ddp, r):
    return [-math.log(p,r) for p in ddp]

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

codigo = ["1", "2", "3", "31"]
ddp = [0.5, 0.25, 0.125, 0.125]
r = len(set(''.join(codigo))) # join concatena todos los elementos en un string y con set elimina duplicados

entropia = genEntropia(genInfo(ddp,r), ddp)
print(entropia)

#Inciso B

def gen_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

longitudes = gen_longitudes(codigo)

def genLonMedia(longitudes, ddp):
    return sum(i*p for i,p in zip(longitudes,ddp))

print(genLonMedia(longitudes, ddp))