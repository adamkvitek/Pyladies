class Zviratko:
    def __init__(self, jmeno): # init je konstruktor objektu
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))

class Kotatko(Zviratko):
    def snez(self, jidlo):
        print('{} Kouka na to.'.format(self.jmeno))
        super().snez(jidlo)

    def udelej_zvuk(self):
        print("{}: Mňau!".format(self.jmeno))

class Stenatko(Zviratko):
    def udelej_zvuk(self):
        print("{}: Haf!".format(self.jmeno))

zviratka = [Kotatko('Micka'), Stenatko('Azorek')]

for zviratko in zviratka:
    zviratko.snez('Flakota')
    zviratko.udelej_zvuk()
