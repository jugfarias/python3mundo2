# ESTRUTURA DE REPETIÇÃO WHILE

i = 1

while i < 10:
    print(i)
    i += 1

valor = 1
pares = impares = 0

while valor != 0:
    valor = int(input('Digite um valor:'))
    
    if valor != 0:
        if valor % 2 == 0:
            pares += 1
        else:
            impares += 1

print('Você digitou {} pares e {} ímpares'.format(pares, impares))
