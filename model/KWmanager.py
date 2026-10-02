class Quest:
    def __init__(self, nazev: str, popis: str):
        self.nazev = nazev
        self.popis = popis

    def validate(self) -> bool:
        return False


class QuestManager:
    def __init__(self):
        self.field = None

    def method(self, type_param):
        pass