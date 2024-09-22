# Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint 

num = randint(0, 100)

chute = -1
cont = 0

while chute != num:
    chute = int(input('Adivinhe o número de 0 a 100: '))

    if num > chute:
        print('Você errou. O número certo é maior.')
    elif num < chute:
        print('Você errou. O número certo é menor.')

    cont += 1

print('Você acertou! O número certo era {}.'.format(num))
print('Você precisou de {} tentativas para acertar...'.format(cont))


