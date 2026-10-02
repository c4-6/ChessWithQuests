import tkinter as tk
from model.game_manager import GameManager
from model.tah import Tah
from model.questy import MathQuest
from view.game_view import GameView


class GameManagerController:
    def __init__(self, root: tk.Tk, app_controller, mod: str, cas_minuty: int):
        self.root = root
        self.app_controller = app_controller

        # OPRAVA: Pošleme čas z menu do GameManageru
        self.game_manager = GameManager(limit_minut=cas_minuty)
        self.timer = self.game_manager.casovac

        self.aktualni_quest = None
        self.cekajici_tah = None
        self.vybrane_pole = None

        self.game_view = GameView(root, self)
        self.game_view.aktualizuj_plochu()

        self.odpocet_bezi = True
        self.aktualizuj_ui()
        self.odpocet_casu()

    def vyber_pole(self, x: int, y: int):
        if self.cekajici_tah is not None:
            return

        obsah = self.game_manager.plocha.vrat_obsah((x, y))

        if self.vybrane_pole is None:
            if obsah and self.game_manager.je_vlastni_figurka((x, y)):
                self.vybrane_pole = (x, y)
                self.game_view.oznac_pole(x, y)
        else:
            start_x, start_y = self.vybrane_pole
            figurka = self.game_manager.plocha.vrat_obsah((start_x, start_y))
            tah = Tah((start_x, start_y), (x, y), figurka)

            if self.game_manager.revizor_tahu.simulate_Move(tah):
                cilova_fig = self.game_manager.plocha.vrat_obsah((x, y))

                if cilova_fig is not None:
                    self.cekajici_tah = tah
                    self.aktualni_quest = MathQuest()
                    self.game_view.ukaz_quest(self.aktualni_quest.zadani)
                else:
                    self.proved_tah(tah)

            self.vybrane_pole = None
            if not self.cekajici_tah:
                self.game_view.aktualizuj_plochu()

    def zkontroluj_quest(self, odpoved: str):
        if self.aktualni_quest and self.aktualni_quest.over_odpoved(odpoved):
            self.game_view.skryj_quest()
            self.proved_tah(self.cekajici_tah)
            self.cekajici_tah = None
            self.aktualni_quest = None
            self.game_view.aktualizuj_plochu()
        else:
            print("Špatná odpověď!")

    def proved_tah(self, tah):
        self.game_manager.plocha.posun_figurky(tah)
        self.game_manager.aktivni_hrac *= -1
        self.aktualizuj_ui()

    def odpocet_casu(self):
        if not self.odpocet_bezi:
            return

        if not self.timer.odecti_vterinu(self.game_manager.aktivni_hrac):
            print("Konec času!")
            self.odpocet_bezi = False
            return

        self.aktualizuj_ui()
        self.root.after(1000, self.odpocet_casu)

    def aktualizuj_ui(self):
        cas1 = self.timer.formatuj_cas(1)
        cas2 = self.timer.formatuj_cas(-1)
        vyhozene_b = " ".join([f.znak for f in self.game_manager.plocha.vyhozene_figurky_b])
        vyhozene_c = " ".join([f.znak for f in self.game_manager.plocha.vyhozene_figurky_c])
        self.game_view.aktualizuj_stav(cas1, cas2, vyhozene_c, vyhozene_b)