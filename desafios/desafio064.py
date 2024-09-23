# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

num = 0
soma = 0
cont = 0
continua = True

while continua:
    num = int(input('Digite um número (digite 999 para parar): '))
    
    if num == 999:
        continua = False
    else:
        soma += num
        cont += 1
    
print('{} números computados. \nSoma total: {}.'.format(cont, soma))