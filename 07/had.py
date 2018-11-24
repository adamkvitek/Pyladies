def nakresli_mapu(souradnice):

    mapa = []
    for cislo_radku in range(10):
        radek = []
        for cislo_sloupce in range(10):
            radek.append('.')
        mapa.append(radek)

    for ntice in souradnice:
        cislo_sloupce, cislo_radku = ntice
        
        mapa[cislo_radku][cislo_sloupce] = 'X'

    for radek in mapa:
        for symbol in radek:
            print(symbol, end=" ")
        print()

nakresli_mapu([(0, 0), (1, 0), (2, 2), (4, 3), (8, 9), (8, 9)])

def pohyb(souradnice, strana):
    cislo_sloupce, cislo_radku = souradnice[-1]
    if strana == 'v':
        cislo_sloupce = cislo_sloupce + 1
    elif strana == 'z':
        cislo_sloupce = cislo_sloupce - 1
    elif strana == 

    souradnice = [(0, 0)]
    pohyb(souradnice, 'v')
    print(souradnice)
    # → [(0, 0), (1, 0)]
    pohyb(souradnice, 'v')
    print(souradnice)
    # → [(0, 0), (1, 0), (2, 0)]
    pohyb(souradnice, 'j')
    print(souradnice)
    # → [(0, 0), (1, 0), (2, 0), (2, 1)]
    pohyb(souradnice, 's')
    print(souradnice)
    # → [(0, 0), (1, 0), (2, 0), (2, 1), (2, 0)]
