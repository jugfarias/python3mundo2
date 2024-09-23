# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:
# 5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial

num = int(input('Digite um número: '))
fatorial = 1

print('{}! = '.format(num), end = '')
while num >= 1:
    if num == 1:
        print('{} = {}'.format(num, fatorial))
    else:
        print(num, end = ' x ')
        
    fatorial *= num
    num -= 1

# Fazendo por método de math
num = int(input('Digite um número: '))
f = factorial(num)
print('{}! = {}'.format(num, f))

# Fazendo com for
fatorial = 1

num = int(input('Digite um número: '))

print('{}! = '.format(num), end = '')
for num in range (num, 0, -1):
    if num == 1:
        print('{} = {}'.format(num, fatorial))
    else:
        print(num, end = ' x ')
        
    fatorial *= num