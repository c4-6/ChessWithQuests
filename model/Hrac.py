from model.Umanager import Uzivatel

class Hrac:
    def __init__(self, barva: int, uzivatel: Uzivatel):
        self.barva = barva  # 1 (Bílá) nebo -1 (Černá)
        self.uzivatel = uzivatel

    def getEloRating(self) -> int:
        return self.uzivatel.elo if self.uzivatel else 1000