# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0

for i in range (1, 7):
    num = int(input('Número {}: '.format(i)))
    if num % 2 == 0:
        soma += num

print('A soma dos números pares passados é: {}'.format(soma))
