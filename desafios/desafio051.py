# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10 - 1) * r

for n in range (a1, decimo + r, r):
    print(n, end=' -> ')

print('ACABOU')
