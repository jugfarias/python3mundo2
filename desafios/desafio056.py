# desenvolva um programa que leia o nome, idade e sexo de quatro pessoas. No final do programa, mostre:
# - a média de idade do grupo
# - qual é o nome do homem mais velho
# - quantas mulheres têm menos de 20 anos

mulheres_menos_de_20 = 0
soma_idades = 0
idade_mais_velho = 0
nome_mais_velho = ''

for i in range (0, 4):
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))

    sexo = 'nenhum'
    while sexo not in 'masc fem nb':
        sexo = input('Digite seu sexo (masc, fem ou nb): ')
    
    soma_idades += idade

    if sexo == 'masc' and idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome
    
    elif sexo == 'fem' and idade < 20:
        mulheres_menos_de_20 += 1


media_idade = soma_idades / 4

print('Média da idade do grupo: {}'.format(media_idade))
print('Nome do homem mais velho: {}'.format(nome_mais_velho))
print('Mulheres abaixo de 20 anos: {}'.format(mulheres_menos_de_20))
