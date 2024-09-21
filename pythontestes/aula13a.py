# Laços de repetição
# FOR:
# for <contador> in range (<inicio>, <fim>, <passo>):

print('0 -> 6:')
for i in range (0,6): 
    print(i)

print('0 -> 6 (passo 2):')
for i in range (0, 6, 2):
    print(i)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

for i in range (inicio, fim + 1, passo):
    print(i)


soma = 0
for i in range (0, 4): # pede um valor 4 vezes
    n = int(input('Digite um valor: '))
    soma += n

print('O somatório de todos os valores foi {}.'.format(soma))