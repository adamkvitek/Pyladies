from math import pi

def obsah_elipsy(a, b):
    """Vrátí obsah elipsy s poloosami daných délek"""
    # Jen samotný výpočet:
    return pi * a * b

# print a input jsou "venku":
a = float(input('Zadej délku poloosy 1: '))
b = float(input('Zadej délku poloosy 2: '))
print('Obsah je', obsah_elipsy(a, b))

