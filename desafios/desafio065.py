# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

continua = True
soma = 0 
cont = 0

while continua:
    soma += float(input('Digite um valor: '))
    cont += 1

    resp = '0'
    while resp not in 'S N':
        resp = input('Deseja continuar digitando números? [S/N] ').upper()
    
    if resp == 'S':
        continua = True
    else:
        continua = False
    
media = soma / cont
print('A média dos valores digitados é: {}'.format(media))


