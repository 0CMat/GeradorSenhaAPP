from PySimpleGUI import PySimpleGUI as sg
import random


# Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Bem-vindo ao gerador de senhas!')],
    [sg.Text('Quantidade de senhas a serem geradas:'),
     sg.Input(key='number', size=10)],
    [sg.Text('Digite o tamanho da senha a ser gerada:'),
     sg.Input(key='length', size=10)],
    [sg.Button('Gerar senha')],
]
# Janela
window = sg.Window('Gerador de senhas aleatórias', layout)
# Eventos
event, values = window.read()

number = int(values['number'])
length = int(values['length'])

# sg.popup('Exemplo de senha:', number)
# sg.popup('Exemplo de senha:', length)
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
contador = 0


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    else:
        for senhas in range(number):
            senhas = ' '
            contador = contador + 1
            for c in range(length):
                senhas += random.choice(chars)
            sg.Print('Senha gerada', contador, ':', senhas)
