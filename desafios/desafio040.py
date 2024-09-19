# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

media = (nota1 + nota2) / 2

if media < 5:
    print('{}Reprovado{}'.format('\033[31m', '\033[m'))
elif media < 7:
    print('{}Em recuperação{}'.format('\033[33m', '\033[m'))
else:
    print('{}Aprovado!{}'.format('\033[34m', '\033[m'))