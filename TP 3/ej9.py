import random

# INCISO A

def gen_cad(codigo, longitud):
    return ''.join(random.choices(codigo, k=longitud))

codigo = ["==", "<", "<=", ">", ">=", "<>"]
msg_sim = gen_cad(codigo, 10)
print(msg_sim)

# INCISO B

def gen_longitudes(codigo):
    return [len(palabra) for palabra in codigo]

longitudes = gen_longitudes(codigo)
print(longitudes)

# INCISO C

def sum_Kraft(codigo):
    longitudes = gen_longitudes(codigo)
    r = len(set(''.join(codigo))) # join concatena todos los elementos en un string y con set elimina duplicados
    acum = 0
    for l in longitudes:
        acum += r ** (-l)
    
    return acum

print(sum_Kraft(codigo))