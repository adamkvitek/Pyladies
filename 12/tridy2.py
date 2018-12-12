# napíšeme si vlastní třídu
# třídy se píšou stejně jako funkce

class Kotatko:
    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))

    def snez(self, jidlo):
        print("{}: Mňau mňau! {} mi chutná!".format(self.jmeno, jidlo))

mourek = Kotatko()
mourek.jmeno = 'Mourek'
mourek.snez('ryba')

                    # kotatko je instance tridy Kotatko - instance je uskutečnění,
                    # třída je formička
                    # objekt třídy = instance

