from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._ostokset = []

    def tavaroita_korissa(self):
        return len(self._ostokset)
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
        self._ostokset.append(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        self._ostokset.remove(poistettava)

    def tyhjenna(self):
        self._ostokset = []
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse
        # JA kuinka monta kappaletta kyseistä tuotetta korissa on
