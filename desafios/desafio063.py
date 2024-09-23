# Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequência de Fibonacci.
# Exemplo:
# 0 -> 0
# 1 -> 1
# 2 -> 0 -> 1
# 3 -> 0 -> 1 -> 1
# 4 -> 0 -> 1 -> 1 -> 2
# 5 -> 0 -> 1 -> 1 -> 2 -> 3
# 6 -> 0 -> 1 -> 1 -> 2 -> 3 -> 5
# 7 -> 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
# 8 -> 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8 -> 13

n = int(input('Digite um número inteiro: '))
i = 1
anterior = 0
f = 0

while i <= n:
    if i == 1 or i == 2:
        f = i - 1
        print(f, end = ' -> ')
        ultimo = 1
        penultimo = 0
    elif i < n:
        f = ultimo + penultimo
        print(f, end = ' -> ')
        penultimo = ultimo
        ultimo = f
    else:
        f = ultimo + penultimo
        print(f)
    
    i += 1
