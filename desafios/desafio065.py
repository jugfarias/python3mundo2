# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continua = True
soma = cont = maior = menor = 0

while continua:
    num = float(input('Digite um valor: '))
    soma += num
    cont += 1

    if cont == 1:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num

    resp = '0'
    while resp not in 'S N':
        resp = input('Deseja continuar digitando números? [S/N] ').upper()
    
    if resp == 'S':
        continua = True
    else:
        continua = False
    
media = soma / cont
print('A média dos {} valores digitados é: {}'.format(cont, media))
print('O maior valor foi: {}'.format(maior))
print('O menor valor foi: {}'.format(menor))


