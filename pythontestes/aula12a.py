# CONDIÇÕES ANINHADAS: estruturas dentro de estruturas

nome = input('Qual é seu nome? ')

if nome == 'Ravena':
    print('Que nome bonito!')
elif nome == 'Aurora':
    print('Que nome diferente')
elif nome in 'Coral Júpiter Marte Céu Rosa':
    print('Que nome legal!!')
else:
    print('Que nome normal...')


print('Tenha um bom dia {}'.format(nome))
