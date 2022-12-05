# menihän siinä aikaa tajuta miten kannattaa tehdä ja miten käyttää tuota metodi syötettä :D

class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.vanha = 0

    def palauta_tulos(self):
        return self.tulos

class Summa:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovellus.vanha = self.sovellus.tulos
        self.sovellus.tulos += int(self.lue_syote())

class Erotus:
    def __init__(self, sovellus, lue_syote):
        self.sovellus = sovellus
        self.lue_syote = lue_syote

    def suorita(self):
        self.sovellus.vanha = self.sovellus.tulos
        self.sovellus.tulos -= int(self.lue_syote())

class Nollaus:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        self.sovellus.tulos = 0

class Kumoa:
    def __init__(self, sovellus):
        self.sovellus = sovellus

    def suorita(self):
        self.sovellus.tulos = self.sovellus.vanha