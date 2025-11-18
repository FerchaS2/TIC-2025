import math

"""
12. Para una fuente de información con distribución de probabilidades:
P = { 0.385, 0.154, 0.128, 0.154, 0.179 }
a. Calcular la entropía de la fuente
b. Generar una codificación de Huffman
c. Obtener una codificación de Shannon-Fano
e. Comparar la longitud media, el rendimiento y la redundancia de cada código
"""

def alf_y_prob(mensaje):
    alfabeto = []
    apariciones = []
    
    for char in mensaje:
        if char in alfabeto:
            i = alfabeto.index(char)
            apariciones[i] += 1
        else:
            alfabeto.append(char)
            apariciones.append(1)
    
    total = len(mensaje)
    probabilidades = [c/total for c in apariciones]
    
    return alfabeto,probabilidades

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

# Algoritmo de Huffman

def genHuffman(ddp):
    items = [[p, [i]] for i, p in enumerate(ddp)]
    codigos = [''] * len(ddp)
    while len(items) > 1:
        items.sort(key=lambda x: x[0], reverse=True)
        min1 = items.pop()
        min2 = items.pop()
        for i in min1[1]:
            codigos[i] = '0' + codigos[i]
        for i in min2[1]:
            codigos[i] = '1' + codigos[i]
        juntos = min1
        juntos[0] += min2[0]
        juntos[1] += min2[1]
        items.append(juntos)
    return codigos

# Algoritmo de Shannon-Fano

def auxShannonFano(items, codigos, prefijo):
    if len(items) == 1:
        idx = items[0][1]
        codigos[idx] = prefijo
    else:
        total = sum(p for p, _ in items)
        mitad = total / 2

        acum = 0
        i = 0
        while i < len(items) and acum < mitad:
            acum += items[i][0]
            i += 1

        # Evitar desbalance y control de índice
        if i > 1 and abs(mitad - (acum - items[i-1][0])) < abs(mitad - acum):
            i -= 1

        grupo1 = items[:i]
        grupo2 = items[i:]

        auxShannonFano(grupo1, codigos, prefijo + '0')
        auxShannonFano(grupo2, codigos, prefijo + '1')

def genShannonFano(ddp):
    items = [[p, i] for i, p in enumerate(ddp)]
    codigos = [''] * len(ddp)
    items.sort(key=lambda x: x[0], reverse=True)
    auxShannonFano(items, codigos, '')
    return codigos

# Alternativa si viene de un msg
# msg = "58784784525368669895745123656253698989656452121702300223659"
# alf, P = alf_y_prob(msg)

P = [0.385, 0.154, 0.128, 0.154, 0.179]

huffman = genHuffman(P)
shannonfano = genShannonFano(P)

print("Entropia = ", genEntropia(genInfo(P,2), P))
print("Huffman = ", huffman)
print("Shannon-Fano = ", shannonfano)
print()
rendimiento, redundancia = genRendimientoYRedundancia(huffman, P)
print("Longitud media huff = ", genLonMedia(gen_longitudes(huffman), P))
print("Rendimiento huff = ", rendimiento)
print("Redundancia huff = ", redundancia)
print()
rendimiento, redundancia = genRendimientoYRedundancia(shannonfano, P)
print("Longitud media shann = ", genLonMedia(gen_longitudes(shannonfano), P))
print("Rendimiento shann = ", rendimiento)
print("Redundancia shann = ", redundancia)