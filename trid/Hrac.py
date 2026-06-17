class Kwest:
    def __init__(self):
        self.nazev = ""
        self.popis = ""

    def validate(self):
        pass


class Uzivatel:
    def __init__(self):
        self.uzivatelske_jmeno = ""
        self.jmeno = ""
        self.email = ""
        self.elo = 0
        self.splnene_kvesty = []

    def pridej_kwest(self, kwest):
        pass


class Hrac:
    def __init__(self, barva, uzivatel):
        self.barva = barva
        self.uzivatel = uzivatel

    def getEloRating(self):
        pass