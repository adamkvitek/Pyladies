from random import randrange

tah_pocitace = randrange(3)
tah_cloveka = input('kámen, nůžky, nebo papír? ')

print(tah_pocitace)

def tahy_pocitace():
    if tah_pocitace == 0:
        tah_pocitace_kamen()
    elif tah_pocitace == 1:
        tah_pocitace_nuzky()
    elif tah_pocitace >= 2:
        tah_pocitace_papir()

def tah_pocitace_kamen():
    if tah_cloveka == 'kámen':
        print('Plichta')
    elif tah_cloveka == 'nůžky':
        print('Počítač vyhrál')
    elif tah_cloveka == 'papír':
        print('Vyhrál jsi!')
    else:
       print('Nerozumím.')

def tah_pocitace_nuzky():
    if tah_cloveka == 'kámen':
        print('Vyhrál jsi!')
    elif tah_cloveka == 'nůžky':
        print('Plichta')
    elif tah_cloveka == 'papír':
        print('Počítač vyhrál')
    else:
       print('Nerozumím.')

def tah_pocitace_papir():
    if tah_cloveka == 'kámen':
        print('Počítač vyhrál')
    elif tah_cloveka == 'nůžky':
        print('Vyhrál jsi!')
    elif tah_cloveka == 'papír':
        print('Plichta')
    else:
       print('Nerozumím.')

tahy_pocitace()

