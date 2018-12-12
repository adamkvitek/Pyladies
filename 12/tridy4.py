# Cvičení: Kočka

class Kocka:
    def __init__(self, name):
        self.jmeno = name
        self.pocet_zivotu = 9

    def zamnoukej(self):
        print('{}: Mnau, mnau, mnauuu!'.format(self.jmeno))

    def je_ziva(self):
        if self.pocet_zivotu > 0:
            print(self.pocet_zivotu, 'Jsem živá')
        if self.pocet_zivotu == 0:
            print(self.pocet_zivotu, 'Koukám na beetlejuice')
        return self.pocet_zivotu > 0

    def uber_zivot(self):
        if not self.je_ziva():
            print('Nemuzeme zabit mrtvou kocku.')
        else:
            self.pocet_zivotu -= 1

    def snez(self, jidlo):
        if not self.je_ziva():
            print('Zbytecne krmit mrtvou kocku.')
        if jidlo == 'ryba' and self.pocet_zivotu < 9:
            self.pocet_zivotu += 1
            print('Je mi skvěle!')
        else:
            print("Kocka se krmi.")

mourek = Kocka('Mourek')
mourek.je_ziva()
mourek.uber_zivot()
mourek.snez('ryba')
mourek.zamnoukej()
mourek.snez('korab kapitana Nema')
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.snez('ryba')
mourek.snez('ryba')
mourek.snez('ryba')
mourek.snez('ryba')
mourek.snez('ryba')
mourek.snez('ryba')
mourek.snez('ryba')
mourek.snez('ryba')
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()
mourek.uber_zivot()

