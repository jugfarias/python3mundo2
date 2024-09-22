# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

for i in range (0, 5):
    peso = float(input('Digite seu peso em kg: '))

    if i == 0:
        maior = peso
        menor = peso

    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso

print('Maior peso: {}kg\nMenor peso: {}kg'.format(maior, menor))
