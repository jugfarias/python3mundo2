# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{0} BEM VINDE À LOJA QUERO MAIS {0}'.format('=' * 10))

preco = float(input('Preço: R$'))

print('Qual a forma de pagamento?')

resposta = '0'
while resposta not in '1 2 3 4':
    print('1 - À vista no dinheiro ou cheque')
    print('2 - À vista no cartão')
    print('3 - Em até 2x no cartão')
    print('4 - 3x ou mais no cartão')

    resposta = input('Responda (1, 2, 3 ou 4): ')

if resposta == '1':
    preco -= preco * 0.1
    print('Você recebe 10% de desconto, totalizando: R${:.2f}'.format(preco))
elif resposta == '2':
    preco -= preco * 0.05
    print('Você recebe 5% de desconto, totalizando: R${:.2f}'.format(preco))
elif resposta == '3':
    parcela = preco / 2
    print('Você paga o preço normal, totalizando 2 parcelas de: R${}'.format(parcela))
else:
    vezes = int(input('Em quantas vezes? '))
    preco += preco * 0.2
    parcela = preco / vezes
    print('Você terá 20% de juros, totalizando {} parcelas de: R${}'.format(vezes, parcela))
