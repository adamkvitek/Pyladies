# soboury.py

# soubor = open('basnicka.txt', encoding='utf-8') # kódování je důležité pro češtinu
with open('basnicka.txt', encoding='utf-8') as soubor: # otevře a pak zavře soubor (with open)
    obsah = soubor.read()

print(obsah)

with open('basnicka.txt', encoding='utf-8') as soubor:
    for radek in soubor:
        radek = radek.rstrip() # umaže řádky navíc
        print(radek)

with open('vystup.txt', encoding='utf-8', mode='w') as soubor:
    print('Naše staré hodiny', file=soubor)
    print('Bijí', '2+2', 'hodiny', file=soubor)
