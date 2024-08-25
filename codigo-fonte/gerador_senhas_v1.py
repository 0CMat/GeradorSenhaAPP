import random

print('Bem-vindo ao gerador de senhas!')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?@$%&^*(),.;/1234567890'

number = int(input('Quantidade senhas para ser gerados:\n'))
length = int(input('Digite o tamanho da senha a ser gerada:\n'))

print('Senhas geradas:\n')
contador = 0
for senhas in range(number):
    senhas = ' '
    contador = contador + 1
    for c in range(length):
        senhas += random.choice(chars)
    print('Exemplo de senha ', contador ,':',senhas,'\n')
