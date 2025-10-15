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

P = [0.385, 0.154, 0.128, 0.154, 0.179]

print("Entropia = ", genEntropia(genInfo(P,2), P))
print("Huffman = ", genHuffman(P))
print("Shannon-Fano = ", genShannonFano(P))