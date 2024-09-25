cont = 0
soma = 0

while True:
    n = int(input('Digite um número: '))

    if n == 999:
        break

    soma += n
    cont += 1

#print('A soma de {} numeros foi: {}'.format(cont, soma))
print(f'A soma de {cont} números foi: {soma}') # uso de f-string

nome = 'José'
idade = 33
salario = 1879.8

print(f'O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}.')