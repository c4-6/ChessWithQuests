import tkinter as tk


class QuestView(tk.Frame):
    def __init__(self, parent, callback):
        super().__init__(parent, bg="#111111", bd=2, relief="ridge")
        self.callback = callback

        self.lbl_titulek = tk.Label(self, text="Boj o figurku!", bg="#111111", fg="#f6f669", font=("Arial", 12, "bold"))
        self.lbl_titulek.pack(pady=5)

        self.lbl_otazka = tk.Label(self, text="", bg="#111111", fg="white", font=("Arial", 14))
        self.lbl_otazka.pack(pady=5)

        self.entry_odpoved = tk.Entry(self, font=("Arial", 14), width=10)
        self.entry_odpoved.pack(pady=5)

        self.btn_potvrdit = tk.Button(self, text="Potvrdit", command=self.odeslat)
        self.btn_potvrdit.pack(pady=5)

    def zobraz_quest(self, otazka):
        self.lbl_otazka.config(text=f"Kolik je {otazka}?")
        self.entry_odpoved.delete(0, tk.END)

    def odeslat(self):
        # Odešle odpověď do controlleru k ověření
        self.callback(self.entry_odpoved.get())