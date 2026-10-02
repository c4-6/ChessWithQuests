from model.herni_plocha import HerniPlocha
from model.tah import Tah
from typing import Tuple


class RevizorTahu:
    def __init__(self, herni_plocha: HerniPlocha):
        self.herni_plocha = herni_plocha

    def je_tah_geometricky_platny(self, tah: Tah) -> bool:
        start_x, start_y = tah.vychozi_pozice
        cil_x, cil_y = tah.cilova_pozice
        dx = cil_x - start_x
        dy = cil_y - start_y
        figurka = tah.figurka

        if dx == 0 and dy == 0:
            return False

        cilova_figurka = self.herni_plocha.vrat_obsah(tah.cilova_pozice)
        if cilova_figurka and cilova_figurka.barva == figurka.barva:
            return False

        je_utok = cilova_figurka is not None
        povolene_vektory = figurka.vektory_utoku if je_utok else figurka.vektory
        nazev = figurka.nazev.lower()

        if nazev in ["pěšák", "kůň", "král"]:
            if (dx, dy) not in povolene_vektory:
                if nazev == "pěšák" and not je_utok and dx == 0:
                    if figurka.barva == 1 and start_y == 6 and dy == -2:
                        # Pěšák nesmí přeskočit figurku
                        if self.herni_plocha.vrat_obsah((start_x, start_y - 1)) is not None:
                            return False
                    elif figurka.barva == -1 and start_y == 1 and dy == 2:
                        if self.herni_plocha.vrat_obsah((start_x, start_y + 1)) is not None:
                            return False
                    else:
                        return False
                else:
                    return False
        else:
            smer_x = 0 if dx == 0 else dx // abs(dx)
            smer_y = 0 if dy == 0 else dy // abs(dy)

            if (smer_x, smer_y) not in povolene_vektory:
                return False

            if abs(dx) != abs(dy) and abs(dx) > 0 and abs(dy) > 0:
                return False

        if not figurka.skok:
            krok_x = 0 if dx == 0 else dx // abs(dx)
            krok_y = 0 if dy == 0 else dy // abs(dy)

            aktualni_x = start_x + krok_x
            aktualni_y = start_y + krok_y

            while (aktualni_x, aktualni_y) != (cil_x, cil_y):
                if self.herni_plocha.vrat_obsah((aktualni_x, aktualni_y)) is not None:
                    return False
                aktualni_x += krok_x
                aktualni_y += krok_y

        return True

    def simulate_Move(self, tah: Tah) -> bool:
        # 1. Geometrická platnost (směr, překážky)
        if not self.je_tah_geometricky_platny(tah):
            return False

        # 2. Virtuální posun, abychom zjistili, jestli se nevystavíme šachu
        puvodni_cil = self.herni_plocha.posun_figurky_virtualne(tah)
        mame_sach = self.je_sach(tah.figurka.barva)
        self.herni_plocha.vrat_figurku_virtualne(tah, puvodni_cil)

        return not mame_sach

    def najdi_krale(self, barva: int) -> Tuple[int, int]:
        for y in range(8):
            for x in range(8):
                fig = self.herni_plocha.vrat_obsah((x, y))
                if fig and fig.barva == barva and fig.nazev.lower() == "král":
                    return (x, y)
        return (-1, -1)

    def je_pole_napadeno(self, pozice: Tuple[int, int], barva_obrance: int) -> bool:
        barva_utocnika = -barva_obrance
        for y in range(8):
            for x in range(8):
                fig = self.herni_plocha.vrat_obsah((x, y))
                if fig and fig.barva == barva_utocnika:
                    tah = Tah((x, y), pozice, fig)
                    if self.je_tah_geometricky_platny(tah):
                        return True
        return False

    def je_sach(self, barva: int) -> bool:
        kral_poz = self.najdi_krale(barva)
        if kral_poz == (-1, -1): return False
        return self.je_pole_napadeno(kral_poz, barva)

    def ma_platny_tah(self, barva: int) -> bool:
        for start_y in range(8):
            for start_x in range(8):
                fig = self.herni_plocha.vrat_obsah((start_x, start_y))
                if fig and fig.barva == barva:
                    for cil_y in range(8):
                        for cil_x in range(8):
                            tah = Tah((start_x, start_y), (cil_x, cil_y), fig)
                            if self.simulate_Move(tah):
                                return True
        return False

    def check_Mat(self, barva: int) -> bool:
        return self.je_sach(barva) and not self.ma_platny_tah(barva)

    def check_Pat(self, barva: int) -> bool:
        return not self.je_sach(barva) and not self.ma_platny_tah(barva)