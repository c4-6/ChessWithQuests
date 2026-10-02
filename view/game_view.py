import tkinter as tk
from view.quest_view import QuestView


class GameView(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg="#222222")
        self.controller = controller
        self.pack(expand=True, fill="both")

        # Černobílá deska
        self.barva_svetla = "#F0F0F0"
        self.barva_tmava = "#666666"
        self.barva_vyber = "#f6f669"

        # Rozvržení do 3 sloupců: Jména, Deska, Časovače
        self.columnconfigure(0, weight=1, minsize=200)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1, minsize=150)
        self.rowconfigure(0, weight=1)

        # --- LEVÝ PANEL (Jména a Questy) ---
        self.levy_panel = tk.Frame(self, bg="#222222")
        self.levy_panel.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.lbl_hrac2 = tk.Label(self.levy_panel, text="Hráč 2 (Černá)\nVyhozeno: ", fg="white", bg="#222222",
                                  font=("Arial", 12), justify="left")
        self.lbl_hrac2.pack(anchor="nw")

        self.quest_panel = QuestView(self.levy_panel, controller.zkontroluj_quest)
        # Quest je zpočátku skrytý

        self.lbl_hrac1 = tk.Label(self.levy_panel, text="Hráč 1 (Bílá)\nVyhozeno: ", fg="white", bg="#222222",
                                  font=("Arial", 12), justify="left")
        self.lbl_hrac1.pack(side="bottom", anchor="sw")

        # --- STŘED (Deska) ---
        self.platno = tk.Canvas(self, width=600, height=600, bg="#222222", highlightthickness=0)
        self.platno.grid(row=0, column=1)
        self.platno.bind("<Button-1>", self.klik_na_desku)
        self.velikost_pole = 600 // 8

        # --- PRAVÝ PANEL (Časovače) ---
        self.pravy_panel = tk.Frame(self, bg="#222222")
        self.pravy_panel.grid(row=0, column=2, sticky="nsew", padx=10, pady=10)

        self.lbl_timer2 = tk.Label(self.pravy_panel, text="00:00", fg="white", bg="#312e2b", font=("Arial", 20, "bold"),
                                   width=5)
        self.lbl_timer2.pack(anchor="ne")

        self.lbl_timer1 = tk.Label(self.pravy_panel, text="00:00", fg="white", bg="#312e2b", font=("Arial", 20, "bold"),
                                   width=5)
        self.lbl_timer1.pack(side="bottom", anchor="se")

    def aktualizuj_plochu(self):
        self.platno.delete("all")
        plocha = self.controller.game_manager.plocha

        for y in range(8):
            for x in range(8):
                barva = self.barva_svetla if (x + y) % 2 == 0 else self.barva_tmava
                x1 = x * self.velikost_pole
                y1 = y * self.velikost_pole

                self.platno.create_rectangle(x1, y1, x1 + self.velikost_pole, y1 + self.velikost_pole, fill=barva,
                                             outline="")

                figurka = plocha.vrat_obsah((x, y))
                if figurka:
                    # Unicode šachové figurky samy řeší vzhled (prázdné vs. vyplněné), stačí je nakreslit černě.
                    self.platno.create_text(x1 + self.velikost_pole // 2, y1 + self.velikost_pole // 2,
                                            text=figurka.znak, font=("Arial", 40), fill="black")

    def aktualizuj_stav(self, cas1, cas2, vyhozene_c, vyhozene_b):
        self.lbl_timer1.config(text=cas1)
        self.lbl_timer2.config(text=cas2)
        # Hráč 1 vyhazuje černé figury, Hráč 2 bílé figury
        self.lbl_hrac1.config(text=f"Hráč 1 (Bílá)\nVyhozeno: {vyhozene_c}")
        self.lbl_hrac2.config(text=f"Hráč 2 (Černá)\nVyhozeno: {vyhozene_b}")

    def ukaz_quest(self, otazka):
        self.quest_panel.zobraz_quest(otazka)
        self.quest_panel.pack(pady=200, fill="x")

    def skryj_quest(self):
        self.quest_panel.pack_forget()

    def oznac_pole(self, x: int, y: int):
        self.aktualizuj_plochu()
        x1 = x * self.velikost_pole
        y1 = y * self.velikost_pole
        self.platno.create_rectangle(x1, y1, x1 + self.velikost_pole, y1 + self.velikost_pole, fill=self.barva_vyber,
                                     stipple="gray50", outline="")

        figurka = self.controller.game_manager.plocha.vrat_obsah((x, y))
        if figurka:
            self.platno.create_text(x1 + self.velikost_pole // 2, y1 + self.velikost_pole // 2, text=figurka.znak,
                                    font=("Arial", 40), fill="black")

    def klik_na_desku(self, event):
        x = event.x // self.velikost_pole
        y = event.y // self.velikost_pole
        self.controller.vyber_pole(x, y)