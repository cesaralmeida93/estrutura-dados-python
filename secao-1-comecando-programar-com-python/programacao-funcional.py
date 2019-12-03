'''
Vantagens: redução do código fonte, melhora na velocidade, facilita algumas inplementações
Desvantagens: pode gerar códigos obscuros, paradigma pouco difundido
'''

def pot2(x):
    return x ** 2

pot2_ = lambda x: x**2

print(pot2_(5))


def fat(n):
    if (n == 0):
        return 1
    return n * fat(n-1)

fat_ = lambda n: n * fat_(n - 1) if n > 1 else 1

print(fat_(3))
