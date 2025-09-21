'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de 
cada valor serão entregues.
Obs.: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

notas50 = 0
notas20 = 0
notas10 = 0
notas1 = 0

valor_saque = int(input('Valor do saque: '))
valor_restante = valor_saque

notas50 += int(valor_restante/50)
valor_restante %= 50

notas20 += int(valor_restante/20)
valor_restante %= 20

notas10 += int(valor_restante/10)
valor_restante %= 10

notas1 = valor_restante

print(f'{notas50} notas de R$ 50,00')
print(f'{notas20} notas de R$ 20,00')
print(f'{notas10} notas de R$ 10,00')
print(f'{notas1} notas de R$ 1,00')