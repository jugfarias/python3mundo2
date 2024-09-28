# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Digite um número inteiro: '))

    if num < 0:
        break

    i = 1
    while i <= 10:
        print(f'{i} x {num} = {i * num}')
        i += 1