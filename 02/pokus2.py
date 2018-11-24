from random import randrange
cislo = randrange(3)

tah_cloveka = input('kámen, nůžky, nebo papír? ')

if tah_cloveka == 'kámen':
    if cislo == 0:
        print('Počítač vybral kámen. Plichta. :-|')
    elif cislo == 1:
        print('Počítač vybral nůžky. Výhra! :-)')
    else:
        print('Počítač vybral papír. Prohra. :-(')
if tah_cloveka == 'nůžky':
    if cislo == 0:
        print('Počítač vybral kámen. Prohra. :-(')
    elif cislo == 1:
        print('Počítač vybral nůžky. Plichta. :-|')
    else:
        print('Počítač vybral papír. Výhra! :-)')
if tah_cloveka == 'papír':
    if cislo == 0:
        print('Počítač vybral kámen. Výhra! :-)')
    elif cislo == 1:
        print('Počítač vybral nůžky. Prohra. :-(')
    else:
        print('Počítač vybral papír. Plichta. :-|')
else:
    print('Nemluvím jazykem vašeho kmene.')
