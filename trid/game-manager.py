
class GameManager:
    def __init__(self):
        self.plocha = HerniPlocha()
        self.aktivni_hrac = 0
        self.hraci = []
        self.aktualni_tah = None
        self.casovac = None
        self.game_logger = None
        self.revizor_tahu = None

    def proved_tah(self):
        pass

    def zacni_tah(self):
        pass

    def mozne_tahy(self, tah):
        pass

    def zrus_tah(self):
        pass

    def uloz_log(self):
        pass

    def get_stav(self):
        pass

    def najdi_uzivatele(self, id):
        pass