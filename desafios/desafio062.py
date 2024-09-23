# Melhore o desafio 061, perguntando se o usuário quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = a1 + (10 - 1) * r
resp = 1
n_max = 10

while resp != 0:
    
    n = 1
    while n <= n_max:
        an = a1 + (n - 1) * r
        print(an, end = ' -> ')

        n += 1

    resp = int(input('\nQuantos termos mais você quer ver? '))
    
    n_max += resp

print('ACABOU')
