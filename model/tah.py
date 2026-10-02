from typing import Tuple
from model.figury import Figurka


class Tah:
    def __init__(self, vychozi_pozice: Tuple[int, int], cilova_pozice: Tuple[int, int], figurka: Figurka):
        self.vychozi_pozice = vychozi_pozice
        self.cilova_pozice = cilova_pozice
        self.figurka = figurka
        self.typ_tahu = "normalni"

    def over_platnost(self) -> bool:
        return True

    def proved_tah(self):
        pass