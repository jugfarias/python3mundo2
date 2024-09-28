# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from time import sleep
from random import randint

cont = 0
while True:
    print('[ P ] Par')
    print('[ I ] Ímpar')
    parouimpar = input('Par [P] ou ímpar [I]? ')[0].strip().upper()

    print('PAR...')
    sleep(0.5)
    print('OU...')
    sleep(0.5)
    print('ÍMPAR!!')

    num = 0
    while num <= 0 or num > 10: 
        num = int(input('Escolha um número de 1 a 10: '))

    comp = randint(1, 10)
    print(f'O computador escolheu {comp}')
    sleep(0.5)

    soma = num + comp

    print(f'{num} + {comp} = {soma}')

    if soma % 2 == 0:
        print('PAR GANHOU!')
        if parouimpar == 'P':
            print('PARABÉNS, JOGADOR!')
            cont += 1
            print(f"Você já venceu {cont} vezes")
        else: 
            print('O computador venceu desta vez...')
            break
    else:
        print('ÍMPAR GANHOU!')
        if parouimpar == 'I':
            print('PARABÉNS, JOGADOR!')
            cont += 1
            print(f"Você já venceu {cont} vezes")
        else: 
            print('O computador venceu desta vez...')
            break
