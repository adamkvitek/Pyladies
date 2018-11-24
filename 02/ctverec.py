from math import pi

strana = float(input('Zadej stranu čtverce v centimetrech: '))
cislo_je_spravne = strana > 0

if cislo_je_spravne:
    print('Obvod čtverce se stranou', strana, 'je', 4 * strana, 'cm')
    print('Obsah čtverce se stranou', strana, 'je', strana * strana, 'cm2')
    print('Obvod kruhu se stranou', strana, 'je', 2 * pi * strana, 'cm')
    print('Obsah kruhu se stranou', strana, 'je', pi * strana  ** 2, 'cm2')
else:
    print('Strana musí být kladná, jinak z toho nebude čtverec!')

print('Děkujeme za použití geometrické kalkulačky')

