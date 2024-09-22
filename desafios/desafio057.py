# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ter um valor correto.

gen = 'n'

while gen != 'F' and gen != 'M' and gen != 'NB':
    gen = input('Qual seu gênero? [M, F ou NB] ').upper()
