# Melhore o desafio 061, perguntando se o usuário quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
resp = 1
n_max = 0
n = 1
cont = 0
resp = 10

while resp != 0:
    n_max += resp

    while n <= n_max:
        an = a1 + (n - 1) * r
        print(an, end = ' -> ')

        n += 1

    print('PAUSA')

    resp = int(input('Quantos termos mais você quer ver? '))

print('ACABOU')
print('Progressão finalizada com {} termos apresentados.'.format(n_max))
