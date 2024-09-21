# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero = int(input('Escolha um número de 1 a 10: '))

for i in range (1, 11):
    print('{} x {} = {}'.format(i, numero, i * numero))
