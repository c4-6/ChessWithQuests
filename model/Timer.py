class Timer:
    def __init__(self, limit_minut: int):
        # 1 = Bílý, -1 = Černý. Uložíme čas ve vteřinách
        self.cas_hrac = {1: limit_minut * 60, -1: limit_minut * 60}

    def formatuj_cas(self, hrac: int) -> str:
        vteriny = self.cas_hrac[hrac]
        m = vteriny // 60
        s = vteriny % 60
        return f"{m:02d}:{s:02d}"

    def odecti_vterinu(self, hrac: int) -> bool:
        if self.cas_hrac[hrac] > 0:
            self.cas_hrac[hrac] -= 1
            return True
        return False