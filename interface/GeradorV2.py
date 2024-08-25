import PySimpleGUI as sg


# Layout
sg.theme('Reddit')


layout = [
    [sg.Text('Digite uma chave para sua senha:')],
    [sg.Input(key='chave', size=15)],
    [sg.Button('Gerar senha')],
]
# Janela
window = sg.Window('Gerador de senhas aleatórias', layout)
# Eventos


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    else:
        event, values = window.read()
        chave = values['chave']
        print = sg.Print
        senha = ""
        for letra in chave:
            if letra in "Aa":
                senha = senha + "@"
            elif letra in "Ii":
                senha = senha + "!"
            elif letra in "Oo":
                senha = senha + "&"
            elif letra in "Uu":
                senha = senha + "?"
            elif letra in "Ee":
                senha = senha + "*"
            elif letra in "Ff":
                senha = senha + "-"
            elif letra in "Rr":
                senha = senha + "#"
            elif letra in "Tt":
                senha = senha + "%"
            elif letra in "Ss":
                senha = senha + "$"
            else:
                senha = senha + letra
        print('A senha gerada é:\n', senha)
