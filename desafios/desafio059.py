# Crie um programa que leia dois valores e mostre um menu na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

op = '0'

while op != '5':
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    op = '0'
    while op not in '4 5':
        print('[ 1 ] SOMAR')
        print('[ 2 ] MULTIPLICAR')
        print('[ 3 ] MAIOR')
        print('[ 4 ] NOVOS NÚMEROS')
        print('[ 5 ] SAIR')
        op = input('Escolha 1, 2, 3, 4 ou 5: ')
    
        if op == '1':
            resultado = num1 + num2
            print('A soma dos números {} e {} é: {}'.format(num1, num2, resultado))
        elif op == '2':
            resultado = num1 * num2
            print('O produto dos números {} e {} é: {}'.format(num1, num2, resultado))
        elif op == '3':
            if num1 > num2:
                print('{} é maior que {}.'.format(num1, num2))
            elif num1 < num2:
                print('{} é maior que {}.'.format(num2, num1))
            else:
                print('Não existe maior. Ambos os números são {}.'.format(num1))
