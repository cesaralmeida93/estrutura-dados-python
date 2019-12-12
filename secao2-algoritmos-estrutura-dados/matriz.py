matriz = [
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120],
]

print(matriz[2][3])

vetor = [10, 20, 30, 40, 50]

print(vetor[1])

matriz2 = [
    ['João', 8, 7, 6],
    ['Pedro', 4.5, 9, 10],
    ['Marcos', 6, 6, 8]
]

for linha in matriz2:
    for coluna in linha:
        print(str(coluna) + '\t', end=' ')
    print('')
