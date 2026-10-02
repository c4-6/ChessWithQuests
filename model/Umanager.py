from typing import List
from model.KWmanager import Quest


class Uzivatel:
    def __init__(self, uzivatelske_jmeno: str, jmeno: str, email: str, elo: int):
        self.uzivatelske_jmeno = uzivatelske_jmeno
        self.jmeno = jmeno
        self.email = email
        self.elo = elo
        self.splnene_kwesty: List[Quest] = []

    def pridej_quest(self, quest: Quest):
        self.splnene_kwesty.append(quest)


class UserManager:
    def __init__(self):
        self.log_uzivatelu = ""
        self.historie_uzivatele = ""

    def proved_tah(self) -> bool:
        return True