# Crie um programa que faça o computador jogar Jokenpô com você.

import random

jokenpo = ['pedra', 'papel', 'tesoura']
comp = random.choice(jokenpo)

escolha = '0'

while escolha not in 'pedra papel tesoura':
    escolha = input('Escolha: pedra, papel ou tesoura? ').lower().strip()

if comp == escolha:
    print('Empate, ambos escolheram {}.'.format(comp))
elif comp == 'pedra':
    if escolha == 'tesoura':
        print('Pedra quebra tesoura. O computaodor venceu.')
    elif escolha == 'papel':
        print('Papel envolve pedra. Você venceu.')
elif comp == 'papel':
    if escolha == 'pedra':
        print('Papel envolve pedra. O computador venceu.')
    elif escolha == 'tesoura':
        print('Tesoura corta papel. Você venceu.')
elif comp == 'tesoura':
    if escolha == 'papel':
        print('Tesoura corta papel. O Computador venceu.')
    elif escolha == 'pedra':
        print('Pedra quebra tesoura. Você venceu.')