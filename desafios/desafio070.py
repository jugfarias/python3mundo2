# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

primeira = True
total = 0
mais_que_mil = 0

while True:

    nome = input('Produto: ')
    valor = float(input(f'Valor do {nome}: '))

    total += valor

    if primeira or valor < valor_mais_barato:
        mais_barato = nome
        valor_mais_barato = valor   

    if valor > 1000:
        mais_que_mil += 1

    resp = '0'
    while resp != 'S' and resp != 'N':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break

print(f'O total foi de: R${total:.2f}')
print(f'Acima de R$1000,00: {mais_que_mil}')
print(f'Produto mais barato: {mais_barato}')