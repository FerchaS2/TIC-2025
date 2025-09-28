import random

def gen_msg(n, codigo, ddp):
    return ''.join(random.choices(codigo, weights=ddp, k=n))

codigo = [".,", ";", ",,", ":", "...", ",:;"]
ddp = [0.1, 0.5, 0.1, 0.2, 0.05, 0.05]
n = 5

print(gen_msg(n, codigo, ddp))