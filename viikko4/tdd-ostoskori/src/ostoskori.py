from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        summa = 0
        for ostos in self._ostokset:
            summa += ostos.lukumaara()
        print(summa)
        return summa
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto",
        # tulee metodin palauttaa 2

    def hinta(self): # kertoo korissa olevien ostosten yhteenlasketun hinnan
        summa = 0
        for tuote in self._ostokset:
            summa += tuote.hinta()
        return summa

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        ostos = Ostos(lisattava)
        if ostos in self._ostokset:
            ostos.muuta_lukumaaraa(1)
        else:
            self._ostokset.append(ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        self._ostokset = []
        # tyhjentää ostoskorin

    def ostokset(self):
        ostokset = []
        for ostos in self._ostokset:
            ostokset.append((ostos.tuotteen_nimi(), ostos.lukumaara()))
        return ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse
        # JA kuinka monta kappaletta kyseistä tuotetta korissa on
