# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas têm mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres têm menos de 20 anos.

from time import sleep

cont_mais_18 = 0
homens = 0
mulheres_menos_20 = 0

while True:
    idade = int(input('Idade: '))

    sexo = '0'
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').strip().upper()[0]

    if idade > 18:
        cont_mais_18 += 1

    if sexo == 'F':
        homens += 1

    if sexo == 'F' and idade < 20:
        mulheres_menos_20 += 1

    resp = 'x'
    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar [S/N]? ').strip().upper()[0]

    if resp == 'N':
        break

print('ANALISANDO...')
sleep(1)
print('Foram cadastrados: ')
sleep(0.5)
print(f'- {cont_mais_18} pessoas acima de 18 anos.')
sleep(0.5)
print(f'- {homens} homens.')
sleep(0.5)
print(f'- {mulheres_menos_20} mulheres abaixo dos 20 anos.')

