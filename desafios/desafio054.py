# Crie um programa que leia um ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year

menores = 0
maiores = 0

for i in range (0, 7):
    nasc = int(input('Digite seu ano de nascimento: '))
    idade = ano_atual - nasc

    if idade < 21:
        menores += 1 
    else:
        maiores += 1

print('{} pessoas são maiores de idade e {} são menores.'.format(maiores, menores))
