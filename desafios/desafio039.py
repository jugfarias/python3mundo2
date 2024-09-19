# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano_atual = date.today().year

ano_nasc = int(input('Ano de nascimento: '))

idade = ano_atual - ano_nasc

if idade < 18:
    print('\033[34mUm dia você deverá se alistar ao serviço militar.\033[m')
elif idade == 18:
    print('\033[32mEstá na hora de se alistar ao serviço militar!\033[m')
else:
    print('\033[31mJá passou do tempo de alistamento.\033[m')
    print('Você está {} anos atrasado.'.format(idade - 18))