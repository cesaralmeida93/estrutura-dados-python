# Recursividade

def fat(n):
    if n == 0:
        return 1
    return n * fat(n - 1)

# fat(3)
#     3 * fat(2) => 3 * 2 = 6
#     fat(2)
#         2 * fat(1) => 2 * 1 = 2
#         fat(1)
#             1 * fat(0) => 1 * 1 = 1
#             fat(0) = 1

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# fibonacci(5) => 3 + 2 = 5
#     fibonacci(4) => 2 + 1 = 3
#         fibonacci(3) => 1 + 1 = 2
#             fibonacci(2) => 1
#                 fibonacci(1) => 1


print(fibonacci(7))


def potencia(base, exp):
    if exp == 0:
        return 1
    return base * potencia(base, exp - 1)

# potencia(2, 5) 
#     2 * potencia(2, 4) => 2 * 16 = 32
#         2 * potencia(2, 3) => 2 * 8 = 16
#             2 * potencia(2, 2) => 2 * 4 = 8 
#                 2 * potencia(2, 1) => 2 * 2 = 4
#                     2 * potencia(2, 0) => 2 * 1 = 2


print(potencia(10, 2))