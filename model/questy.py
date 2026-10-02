class MathQuest:
    def __init__(self):
        self.zadani = "2 + 2"
        self.spravna_odpoved = "4"

    def over_odpoved(self, odpoved: str) -> bool:
        return odpoved.strip() == self.spravna_odpoved