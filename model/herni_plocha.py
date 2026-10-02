from typing import List, Tuple
from model.figury import Figurka, Pesak, Vez, Kun, Strelec, Dama, Kral
from model.tah import Tah


class HerniPlocha:
    def __init__(self):
        self.rozmery = (8, 8)
        self.herni_deska: List[List[Figurka]] = [[None for _ in range(8)] for _ in range(8)]
        self.vyhozene_figurky_b: List[Figurka] = []
        self.vyhozene_figurky_c: List[Figurka] = []
        self._inicializuj_plochu()

    def _inicializuj_plochu(self):
        kolekce_c = [Vez(-1), Kun(-1), Strelec(-1), Dama(-1), Kral(-1), Strelec(-1), Kun(-1), Vez(-1)]
        self.herni_deska[0] = kolekce_c
        self.herni_deska[1] = [Pesak(-1) for _ in range(8)]

        kolekce_b = [Vez(1), Kun(1), Strelec(1), Dama(1), Kral(1), Strelec(1), Kun(1), Vez(1)]
        self.herni_deska[7] = kolekce_b
        self.herni_deska[6] = [Pesak(1) for _ in range(8)]

    def vrat_obsah(self, souradnice: Tuple[int, int]) -> Figurka:
        x, y = souradnice
        if 0 <= x < 8 and 0 <= y < 8:
            return self.herni_deska[y][x]
        return None

    def posun_figurky(self, tah: Tah) -> bool:
        start_x, start_y = tah.vychozi_pozice
        cil_x, cil_y = tah.cilova_pozice
        cilova_figurka = self.herni_deska[cil_y][cil_x]

        if cilova_figurka:
            if cilova_figurka.barva == 1:
                self.vyhozene_figurky_b.append(cilova_figurka)
            else:
                self.vyhozene_figurky_c.append(cilova_figurka)

        self.herni_deska[cil_y][cil_x] = tah.figurka
        self.herni_deska[start_y][start_x] = None
        return True

    def posun_figurky_virtualne(self, tah: Tah) -> Figurka:
        # Pro ověření šachu - přesune figurku jen v paměti a vrátí původní
        start_x, start_y = tah.vychozi_pozice
        cil_x, cil_y = tah.cilova_pozice
        puvodni_cil = self.herni_deska[cil_y][cil_x]

        self.herni_deska[cil_y][cil_x] = tah.figurka
        self.herni_deska[start_y][start_x] = None
        return puvodni_cil

    def vrat_figurku_virtualne(self, tah: Tah, puvodni_cil: Figurka):
        # Vrátí virtuální tah zpět
        start_x, start_y = tah.vychozi_pozice
        cil_x, cil_y = tah.cilova_pozice

        self.herni_deska[start_y][start_x] = tah.figurka
        self.herni_deska[cil_y][cil_x] = puvodni_cil