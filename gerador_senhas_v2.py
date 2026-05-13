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
    elif letra in "Ll": senha = senha + "1"
    elif letra in "Cc": senha = senha + "3"
    elif letra in "Gg": senha = senha + "6"
    elif letra in "Zz": senha = senha + "2"
    elif letra in "Bb": senha = senha + "9"
    elif letra in "Pp": senha = senha + "7"
    elif letra in "Dd": senha = senha + "8"
    elif letra in "Mm": senha = senha + "5"
    elif letra in "Nn": senha = senha + "4"
    elif letra in "Vv": senha = senha + "0"
    elif letra in "Ww": senha = senha + "9"
    elif letra in "@": senha = senha + "B"
    elif letra in "!": senha = senha + "C"
    elif letra in "&": senha = senha + "D"
    elif letra in "?": senha = senha + "E"
    elif letra in "*": senha = senha + "F"
    elif letra in "-": senha = senha + "G"
    elif letra in "#": senha = senha + "H"
    elif letra in "%": senha = senha + "I"
    else:
        senha = senha + letra
        
print('A senha gerada é:\n',senha)


# fazer com que seja obrigatório ter número, letra maiúscula, letra minúscula e caractere especial;