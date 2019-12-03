import random

print(random.randrange(10)) # imprime um número aleatório entre 0 e 9

print(random.randint(1, 4)) # imprime im inteiro aleatório entre 1 e 4

lista = [1, 2, 3, 4]
random.shuffle(lista) # embaralha os valores da lista de maneira aleatória
print(lista)

print(random.sample(lista, 2)) # imprime 3 elementos únicos aleatórios da lista

print(random.random()) # gera um float aleatório entre 0(inclusive) e 1(exclusive)

print(random.uniform(1, 10)) # gera um float aleatório entre 1(inclusive) e 10(inclusive)