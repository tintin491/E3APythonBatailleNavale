import tkinter as tk
from faulthandler import disable


class Board:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.buttons = []  # Stocker les boutons pour les identifier plus tard
        self.create_widgets()

    def create_widgets(self):
        # Ajouter un label
        self.fenetre.geometry("500x500")
        label = tk.Label(self.fenetre, text="Bataille Navale", font=("Helvetica", 16))
        label.pack()

        buttonframe = tk.Frame(self.fenetre)
        for i in range(10):
            row = []
            for j in range(10):
                btn1 = tk.Button(buttonframe, text="", command=lambda a=i, b=j: self.button_change(a, b), height=self.fenetre.winfo_height() * 2, width=self.fenetre.winfo_width() * 5)
                btn1.grid(row=i, column=j)
                row.append(btn1)
            self.buttons.append(row)
        buttonframe.pack(padx = (25, 0), fill='x')

    def button_change(self, row, col):
        button = self.buttons[row][col]
        button.config(bg="blue", activebackground="blue")
        button['state'] = tk.DISABLED

    def run(self):
        # Lancer la boucle principale de Tkinter
        self.fenetre.mainloop()


app = Board()
app.run()
