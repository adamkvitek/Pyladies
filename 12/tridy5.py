class Zviratko:
    def __init__(self, jmeno): # init je konstruktor objektu
        self.jmeno = jmeno

    def snez(self, jidlo):
        print("{}: {} mi chutná!".format(self.jmeno, jidlo))

class Kotatko(Zviratko):
    def snez(self, jidlo):
        print('{} Kouka na to.'.format(self.jmeno))
        super().snez(jidlo)

    def zamnoukej(self):
        print('{}: Mnau!'.format(self.jmeno))

class Stenatko(Zviratko):
    def zastekej(self):
        print('{}: Haf!'.format(self.jmeno))

micka = Kotatko('Micka')
azorek = Stenatko('Azorek')
micka.zamnoukej()
azorek.zastekej()
micka.snez('ryba')
azorek.snez('kost')

