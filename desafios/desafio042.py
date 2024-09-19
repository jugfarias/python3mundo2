# Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

lado1 = int(input('Lado 1: '))
lado2 = int(input('Lado 2: '))
lado3 = int(input('Lado 3: '))

if (lado1 + lado2) > lado3 and (lado2 + lado3) > lado1 and (lado1 + lado3) > lado2:
    print('Pode formar um triângulo.')
    
    if lado1 == lado2 == lado3:
        print('Triângulo equilátero.')
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print('Triângulo isósceles.')
    else:
        print('Triângulo escaleno.')
else:
    print('Não pode formar um triângulo.')