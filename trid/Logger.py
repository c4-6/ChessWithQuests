#export + notation + metadata writer v jedne tride


class ExportWriter:
    def __init__(self):
        self.field = None


class MetadataWriter(ExportWriter):
    def method(self, typ):
        pass


class ChessNotationWriter(ExportWriter):
    def method(self, typ):
        pass

    def item(self):
        pass


class GameLogger:
    def __init__(self):
        self.soubor = None

    def uloz_tah(self, tah):
        pass

    def vytvor_soubor(self, string):
        pass