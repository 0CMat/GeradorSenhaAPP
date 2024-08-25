print('Gerador de senhas!')
chave = input('Digite uma chave para sua senha:\n')

senha = ""

for letra in chave:
    if letra in "Aa": senha = senha + "@"
    elif letra in "Ii": senha = senha + "!"
    elif letra in "Oo": senha = senha + "&"
    elif letra in "Uu": senha = senha + "?"
    elif letra in "Ee": senha = senha + "*"
    elif letra in "Ff": senha = senha + "-"
    elif letra in "Rr": senha = senha + "#"
    elif letra in "Tt": senha = senha + "%"
    elif letra in "Ss": senha = senha + "$"
    else:
        senha = senha + letra
        
print('A senha gerada é:\n',senha)