# Faça um program que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Número inteiro: '))
eh_primo = True

for i in range (2, num):
    if num % i == 0:
        eh_primo = False
        exit()

if eh_primo:
    print('{} é um número primo.'.format(num))
else:
    print('{} não é um número primo.'.format(num))
