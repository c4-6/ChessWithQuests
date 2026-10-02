from typing import List, Tuple

class Figurka:
    def __init__(self, nazev: str, barva: int, znak: str):
        self.nazev = nazev
        self.barva = barva
        self.znak = znak
        self.vektory: List[Tuple[int, int]] = []
        self.vektory_utoku: List[Tuple[int, int]] = []
        self.skok: bool = False

class Pesak(Figurka):
    def __init__(self, barva: int):
        znak = "♙" if barva == 1 else "♟"
        super().__init__("Pěšák", barva, znak)
        self.vektory = [(0, -1 * self.barva)]
        self.vektory_utoku = [(1, -1 * self.barva), (-1, -1 * self.barva)]
        self.skok = False

class Vez(Figurka):
    def __init__(self, barva: int):
        znak = "♖" if barva == 1 else "♜"
        super().__init__("Věž", barva, znak)
        self.vektory = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.vektory_utoku = self.vektory
        self.skok = False

class Kun(Figurka):
    def __init__(self, barva: int):
        znak = "♘" if barva == 1 else "♞"
        super().__init__("Kůň", barva, znak)
        self.vektory = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
        self.vektory_utoku = self.vektory
        self.skok = True

class Strelec(Figurka):
    def __init__(self, barva: int):
        znak = "♗" if barva == 1 else "♝"
        super().__init__("Střelec", barva, znak)
        self.vektory = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.vektory_utoku = self.vektory
        self.skok = False

class Dama(Figurka):
    def __init__(self, barva: int):
        znak = "♕" if barva == 1 else "♛"
        super().__init__("Dáma", barva, znak)
        self.vektory = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.vektory_utoku = self.vektory
        self.skok = False

class Kral(Figurka):
    def __init__(self, barva: int):
        znak = "♔" if barva == 1 else "♚"
        super().__init__("Král", barva, znak)
        self.vektory = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        self.vektory_utoku = self.vektory
        self.skok = False