# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 300

for i in range (0, 5):
    peso = float(input('Digite seu peso em kg: '))

    if peso > maior:
        maior = peso
    
    if peso < menor:
        menor = peso

print('Maior peso: {}\nMenor peso: {}'.format(maior, menor))
