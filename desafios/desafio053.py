# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Exemplos de palíndromos:
# APOS A SOPA
# A SACADA DA CASA
# A TORRE DA DERROTA
# O LOBO AMA O BOLO
# ANOTARAM A DATA DA MARATONA

frase = input('Digite uma frase: ')
frase = frase.replace(' ', '')

frase_invertida = ''

for i in range(len(frase) - 1, -1, -1):
    frase_invertida += frase[i]

if frase == frase_invertida:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')

