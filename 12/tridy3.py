# napíšeme si vlastní třídu
# třídy se píšou stejně jako funkce

class Kotatko:
    def __init__(self, name): # init je konstruktor objektu
    self.jmeno = name # !!!name je parametr, jmeno je atribut!!!

    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

mourek = Kotatko('Mourek')
mourek.zamnoukej()

                    # kotatko je instance tridy Kotatko - instance je uskutečnění,
                    # třída je formička
                    # objekt třídy = instance

