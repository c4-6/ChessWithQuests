#figurky
class Figurka:
    def __init__(self, nazev, barva):
        self.nazev = nazev
        self.barva = barva
        self.vektory = []
        self.vektory_utoku = []


class Kun(Figurka):
    def __init__(self, barva):
        super().__init__("Kůň", barva)
        self.vektor = []
        self.vektor_utoku = []
        self.skok = True


class Kral(Figurka):
    def __init__(self, barva):
        super().__init__("Král", barva)
        self.vektor = []
        self.vektor_utoku = []
        self.skok = False


class Dama(Figurka):
    def __init__(self, barva):
        super().__init__("Dáma", barva)
        self.vektor = []
        self.vektor_utoku = []
        self.skok = False


class Vez(Figurka):
    def __init__(self, barva):
        super().__init__("Věž", barva)
        self.vektor = []
        self.vektor_utoku = []
        self.skok = False


class Pesak(Figurka):
    # vektor se vynásobí barvou, aby šel správným směrem
    def __init__(self, barva):
        super().__init__("Pěšák", barva)
        self.vektor = []
        self.vektor_utoku = []
        self.skok = False


class Strelec(Figurka):
    def __init__(self, barva):
        super().__init__("Střelec", barva)
        self.vektor = []
        self.vektor_utoku = []
        self.skok = False