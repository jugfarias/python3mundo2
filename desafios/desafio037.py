# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

dec = int(input('Número decimal: '))
print('Escolha para qual sistema você quer converter o número {}.'.format(dec))
print('1 - binário \n2- octal \n3- hexadecimal')

resposta = '0'
while resposta not in '1 2 3':
    resposta = input('Escolha (1, 2 ou 3): ')

if resposta == '1':
    bin = bin(dec)[2:]
    print('O número {} no sistema binário é: \033[32m{}\033[m.'.format(dec, bin))
if resposta == '2':
    oct = oct(dec)[2:]
    print('O número {} no sistema octal é: \033[32m{}\033[m.'.format(dec, oct))
if resposta == '3':
    hex = hex(dec)[2:].upper()
    print('O número {} no sistema hexadecimal é: \033[32m{}\033[m.'.format(dec, hex))
