from random import randrange

sablony = (
        'PP!', 'P!P','!PP',
        '!HH', 'H!H', 'HH!',
        'P-!P', 'H!-H',
        'P!', '!P', 'H!', '!H',
)

def tah_pocitace(pole, symbol_p):
    if symbol_p == 'x':
        symbol_hrace = 'o'
    else:
        symbol_hrace = 'x'
    for sablona in sablony:
        to_co_hledam = sablona
        to_co_hledam = to_co_hledam.replace('P', symbol_p)
        to_co_hledam = to_co_hledam.replace('H' symbol_hrace)
        to_co_hledam = 
