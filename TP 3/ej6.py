def es_no_singular(S):
    return len(set(S)) == len(S) # Recibe lista, la convierte en conjunto (el cual elimina dup), y compara len

def es_instantaneo(S): # doy por hecho que se verifico que es no singular
    for x in S:
        for y in S:
            if x != y and y.startswith(x):
                return False
    return True

def es_ud(S):
    LS = []
    C = set(S)
    
    S1 = set()
    for x in C:
        for y in C:
            if x != y:
                if y.startswith(x):
                    S1.add(y[len(x):])
                elif x.startswith(y):
                    S1.add(x[len(y):])
    
    
    while S1: #no nulo
        if S1 in LS:
            return True
        if not S1.isdisjoint(C):
            return False
        LS.append(S1.copy())
        
        sig = set()
        for x in S1:
            for y in C:
                if y.startswith(x):
                    sig.add(y[len(x):])
                elif x.startswith(y):
                    sig.add(x[len(y):])
        S1 = sig
    
    return True

C = ["1110", "0", "110", "1101", "1011", "10"]

if es_no_singular(C):
    if es_instantaneo(C):
        print("Es instantáneo")
    elif es_ud(C):
        print("Es UD")
    else:
        print("Es no singular")
else:
    print("Es bloque")