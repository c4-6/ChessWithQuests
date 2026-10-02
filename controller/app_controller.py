import tkinter as tk
from view.menu_view import MainMenuView
from controller.game_controller import GameManagerController

class AppController:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Šachy S Questy")
        self.root.geometry("1000x650")
        self.root.configure(bg="#222222")

        self.aktualni_view = None
        self.zobraz_menu()

    def zobraz_menu(self):
        if self.aktualni_view:
            self.aktualni_view.destroy()
        self.aktualni_view = MainMenuView(self.root, self.spust_hru)

    def spust_hru(self, mod: str, cas_minuty: int):
        if self.aktualni_view:
            self.aktualni_view.destroy()
        # Přenechá řízení hernímu controlleru
        self.game_controller = GameManagerController(self.root, self, mod, cas_minuty)