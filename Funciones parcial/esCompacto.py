import math

# Dada una codificación y sus probabilidades determina si es o no compacto

def genInfo(ddp, r):
    return [math.ceil(-math.log(p,r)) for p in ddp]

def es_compacto(codigo, ddp):
    r = len(set(''.join(codigo)))
    entropia = genEntropia(genInfo(ddp, r), ddp)
    longitudes = gen_longitudes(codigo)
    lon_media = genLonMedia(longitudes, ddp)
    return lon_media < entropia

def es_no_singular(S):
    return len(set(S)) == len(S)

def es_instantaneo(S): # doy por hecho que se verifico que es no singular
    for x in S:
        for y in S:
            if x != y and y.startswith(x):
                return False
    return True

def genEntropia(cantinfo, ddp):
    return sum(i*p for i,p in zip(cantinfo,ddp))

def gen_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

def genLonMedia(longitudes, ddp):
    return sum(i*p for i,p in zip(longitudes,ddp))

""""
Estos dos son para compactos teóricos, lo que uso yo es para compactos a nivel práctico

def es_compacto(codigo, ddp):
    r = len(set(''.join(codigo)))
    entropia = genEntropia(genInfo(ddp, r), ddp)
    longitudes = gen_longitudes(codigo)
    lon_media = genLonMedia(longitudes, ddp)
    return math.isclose(lon_media, entropia, rel_tol=1e-9)

def genInfo(ddp, r):
    return [-math.log(p,r) for p in ddp]
"""

codigo = [".,", ";", ",,", ":", "...", ",:;"]
#codigo = ["==", "<", "<=", ">", ">=", "<>"]
#codigo = [")", "[]", "]]", "([", "[()]", "([)]"]

ddp = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]
longitudes = gen_longitudes(codigo)
r = len(set(''.join(codigo))) # join concatena todos los elementos en un string y con set elimina duplicados

entropia = genEntropia(genInfo(ddp,r), ddp)
lon_media = genLonMedia(longitudes, ddp)
print(entropia)
print(lon_media)

if  es_no_singular(codigo) and es_instantaneo(codigo) and es_compacto(codigo, ddp):
    print("Es compacto")
else:
    print("No es compacto")