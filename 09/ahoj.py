def paty_pad(jmeno):
    if jmeno == 'Adam':
        return 'Adame'
    elif jmeno[-1] == 'a':
        return jmeno[:-1] + 'o'
    elif jmeno[-1] == 'j':
        return jmeno + 'i'
    elif jmeno == 'Daniel':
        return 'Danieli'
    elif jmeno == 'daniel':
        return 'danieli'
    elif jmeno == 'Karel':
        return 'Karle'
    elif jmeno[-1] == 'š':
        return jmeno + 'i'
    elif jmeno == 'ňufíček':
        return 'ňufíčku'
    elif jmeno[-1] == 'k':
        return jmeno + 'u'
    else:
        return jmeno

def pozdrav(jmeno):
    print('Vítám tě,', paty_pad(jmeno))

pozdrav(input('Jak se jmenuješ? '))

