from typing import List
from model.herni_plocha import HerniPlocha
from model.revizor import RevizorTahu
from model.Hrac import Hrac
from model.Timer import Timer
from model.Logger import GameLogger
from model.Umanager import Uzivatel
from model.tah import Tah


class GameManager:
    def __init__(self, limit_minut: int = 10):
        self.plocha = HerniPlocha()
        self.revizor_tahu = RevizorTahu(self.plocha)
        self.aktivni_hrac = 1
        self.hraci: List[Hrac] = []
        self.aktualni_tah = None
        # ZDE JE OPRAVA: Předáváme limit do Timeru
        self.casovac = Timer(limit_minut)
        self.game_logger = GameLogger()

    def zacni_tah(self) -> Tah:
        return None

    def mozne_tahy(self) -> List[Tah]:
        return []

    def zrus_tah(self):
        pass

    def uloz_log(self):
        pass

    def get_stav(self) -> int:
        return 0

    def najdi_uzivatele(self, id_uzivatele: int) -> Uzivatel:
        return None

    def je_vlastni_figurka(self, souradnice: tuple) -> bool:
        fig = self.plocha.vrat_obsah(souradnice)
        return fig is not None and fig.barva == self.aktivni_hrac