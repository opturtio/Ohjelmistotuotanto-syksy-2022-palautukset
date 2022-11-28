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
        onko_ostos_listalla = False
        ostos_listalla = None
        uusi_ostos = Ostos(lisattava)
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == uusi_ostos.tuotteen_nimi():
                onko_ostos_listalla = True
                ostos_listalla = ostos
                break

        if onko_ostos_listalla:
            ostos_listalla.muuta_lukumaaraa(1)
        else:
            self._ostokset.append(uusi_ostos)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for ostos in self._ostokset:
            if ostos.tuotteen_nimi() == poistettava.nimi():
                if ostos.lukumaara() > 1:
                    ostos.muuta_lukumaaraa(-1)
                    print(ostos.lukumaara())
                elif ostos.lukumaara() == 1:
                    self._ostokset.remove(ostos)


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
