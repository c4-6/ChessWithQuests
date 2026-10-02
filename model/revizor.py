from model.herni_plocha import HerniPlocha
from model.tah import Tah


class RevizorTahu:
    def __init__(self, herni_plocha: HerniPlocha):
        self.herni_plocha = herni_plocha
        self.tah = None

    def simulate_Move(self, tah: Tah) -> bool:
        start_x, start_y = tah.vychozi_pozice
        cil_x, cil_y = tah.cilova_pozice
        dx = cil_x - start_x
        dy = cil_y - start_y
        figurka = tah.figurka

        # 0. Ošetření kliknutí na stejné místo
        if dx == 0 and dy == 0:
            return False

        cilova_figurka = self.herni_plocha.vrat_obsah(tah.cilova_pozice)

        # Nelze stoupnout na vlastní figurku
        if cilova_figurka and cilova_figurka.barva == figurka.barva:
            return False

        je_utok = cilova_figurka is not None

        # Zvolíme správné vektory podle toho, zda jde o útok (vyhození) nebo jen přesun
        povolene_vektory = figurka.vektory_utoku if je_utok else figurka.vektory
        nazev = figurka.nazev.lower()

        # 1. Pěšák, Kůň a Král se hýbou jen o jeden definovaný vektor
        if nazev in ["pěšák", "kůň", "král"]:
            if (dx, dy) not in povolene_vektory:
                # Výjimka: Dvojitý posun pěšáka ze startovní pozice (Pěšák nemá tento vektor v základu)
                if nazev == "pěšák" and not je_utok and dx == 0:
                    if figurka.barva == 1 and start_y == 6 and dy == -2:
                        pass  # Bílý pěšák ze startu
                    elif figurka.barva == -1 and start_y == 1 and dy == 2:
                        pass  # Černý pěšák ze startu
                    else:
                        return False
                else:
                    return False

        # 2. Věž, Střelec a Dáma se hýbou jako násobky základního směrového vektoru
        else:
            smer_x = 0 if dx == 0 else dx // abs(dx)
            smer_y = 0 if dy == 0 else dy // abs(dy)

            if (smer_x, smer_y) not in povolene_vektory:
                return False

            # Kontrola pro střelce a dámu (zabrání podivným L skokům)
            if abs(dx) != abs(dy) and abs(dx) > 0 and abs(dy) > 0:
                return False

        # 3. Kontrola překážek v cestě pro figury, které nemají bool vlastnost skok=True (všechny kromě koně)
        if not figurka.skok:
            krok_x = 0 if dx == 0 else dx // abs(dx)
            krok_y = 0 if dy == 0 else dy // abs(dy)

            aktualni_x = start_x + krok_x
            aktualni_y = start_y + krok_y

            while (aktualni_x, aktualni_y) != (cil_x, cil_y):
                # Pokud po cestě narazíme na jakoukoliv figurku, tah je neplatný
                if self.herni_plocha.vrat_obsah((aktualni_x, aktualni_y)) is not None:
                    return False
                aktualni_x += krok_x
                aktualni_y += krok_y

        return True

    def check_Sach(self) -> bool:
        return False

    def check_Mat(self) -> bool:
        return False

    def check_Pat(self) -> bool:
        return False