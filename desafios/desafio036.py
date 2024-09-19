# Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: '))
salario = float(input('Salário do comprador: '))
anos = int(input('Em quantos anos? '))
meses = anos * 12

prestacao = valor_casa / meses

if prestacao > salario * 0.3:
    print('\033[31mEmpréstimo negado.\033[m')
else:
    print('Empréstimo de R${:.2f} aprovado.'.format(valor_casa))
    print('Você deverá pagar {} vezes de R${:.2f}.'.format(meses, prestacao))