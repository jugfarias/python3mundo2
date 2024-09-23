# Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10 - 1) * r
n = 1

while n <= 10:
    an = a1 + (n - 1) * r
    print(an, end = ' -> ')

    n += 1

print('ACABOU')
