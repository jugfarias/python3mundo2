# desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for n in range (1, 11):
    an = a1 + (n - 1) * r
    print(an)
