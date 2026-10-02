import tkinter as tk
from tkinter import ttk


class MainMenuView(tk.Frame):
    def __init__(self, parent, start_callback):
        super().__init__(parent, bg="#312e2b")
        self.pack(expand=True, fill="both")

        tk.Label(self, text="Šachy S Questy", font=("Arial", 24, "bold"), bg="#312e2b", fg="#f6f669").pack(pady=40)

        # Výběr módu
        tk.Label(self, text="Herní mód:", bg="#312e2b", fg="white", font=("Arial", 14)).pack(pady=5)
        self.combo_mod = ttk.Combobox(self, values=["Hráč vs Hráč (Lokální)", "Hráč vs Bot"], state="readonly",
                                      font=("Arial", 12))
        self.combo_mod.current(0)
        self.combo_mod.pack(pady=5)

        # Výběr času
        tk.Label(self, text="Časový limit (minuty):", bg="#312e2b", fg="white", font=("Arial", 14)).pack(pady=5)
        self.combo_cas = ttk.Combobox(self, values=["3", "5", "10", "15"], state="readonly", font=("Arial", 12))
        self.combo_cas.current(2)  # Default 10 minut
        self.combo_cas.pack(pady=5)

        # Tlačítko start
        tk.Button(self, text="Hrát", font=("Arial", 16, "bold"), bg="#739552", fg="white",
                  command=lambda: start_callback(self.combo_mod.get(), int(self.combo_cas.get()))).pack(pady=30)