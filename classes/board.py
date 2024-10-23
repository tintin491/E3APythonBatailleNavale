import tkinter as tk

class Board:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.buttonsPlayerTour = []  # Stocker les boutons du joueur dont c'est le tour
        self.buttonsPlayerNonTour = []  # Stocker les boutons du joueur dont ce n'est pas le tour
        self.create_widgets()
        self.ship = [] # Stocker les bateaux et leurs positions
        self.player = 1
        self.start = False
        self.buttonframe1 = None
        self.buttonframe2 = None

    def create_widgets(self):
        # Ajouter un label
        self.fenetre.geometry("500x600")
        labelTitre = tk.Label(self.fenetre, text="Bataille Navale", font=("Helvetica", 16))
        labelTitre.pack()
        self.buttonframe1 = tk.Frame(self.fenetre)
        self.buttonframe2 = tk.Frame(self.fenetre)

        label1 = tk.Label(self.fenetre, text="Plateau adverse", font=("Helvetica", 16))
        label1.pack(pady=(25,0))

        for i in range(5):
            row = []
            for j in range(10):
                btn2 = tk.Button(self.buttonframe2, text="", command=lambda a=i, b=j: self.button_change(a, b), height=self.fenetre.winfo_height() * 2, width=self.fenetre.winfo_width() * 5)
                btn2.grid(row=i, column=j)
                row.append(btn2)
            self.buttonsPlayerNonTour.append(row)
        self.buttonframe2.pack(padx = (25, 0), fill='x')

        label2 = tk.Label(self.fenetre, text="Vos navire", font=("Helvetica", 16))
        label2.pack(pady=(25,0))

        for i in range(5):
            row = []
            for j in range(10):
                btn1 = tk.Button(self.buttonframe1, text="", command=lambda a=i, b=j: self.button_change(a, b), height=self.fenetre.winfo_height() * 2, width=self.fenetre.winfo_width() * 5)
                btn1.grid(row=i, column=j)
                row.append(btn1)
            self.buttonsPlayerTour.append(row)
        self.buttonframe1.pack(padx = (25, 0), fill='x')

    def updateWidget(self):
        for i in range(5):
            for j in range(10):
                self.buttonsPlayerTour[i][j].grid_forget()
                self.buttonsPlayerNonTour[i][j].grid_forget()

        # Placer les boutons de buttonsPlayerTour dans buttonframe2 (plateau adverse)
        for i in range(5):
            for j in range(10):
                self.buttonsPlayerNonTour[i][j].grid(row=i, column=j, in_=self.buttonframe2)
                if self.buttonsPlayerNonTour[i][j].cget("bg") == "red":
                    self.buttonsPlayerNonTour[i][j].config(bg="red", activebackground="red")

        # Placer les boutons de buttonsPlayerNonTour dans buttonframe1 (votre plateau)
        for i in range(5):
            for j in range(10):
                self.buttonsPlayerTour[i][j].grid(row=i, column=j, in_=self.buttonframe1)
                if self.buttonsPlayerTour[i][j].cget("bg") == "blue":
                    self.buttonsPlayerTour[i][j].config(bg="blue", activebackground="blue")

    def button_change(self, row, col): # Au moment ou une case de plateau est choisie
            button = self.buttonsPlayerTour[row][col]
            button.config(bg="blue", activebackground="blue")
            if self.player == 1:
                self.player+=1
            else :
                self.player-=1

            self.joueurChanged()
            self.updateWidget()

    def disabledButton(self):
        for i in self.buttonsPlayerNonTour:
            for element in i:
                element["state"] = tk.DISABLED
        for i in self.buttonsPlayerTour:
            for element in i:
                element["state"] = tk.NORMAL
            self.start = True

    def joueurChanged(self):
        tmp = self.buttonsPlayerNonTour
        self.buttonsPlayerNonTour = self.buttonsPlayerTour
        self.buttonsPlayerTour = tmp

    def run(self):
        # Lancer la boucle principale de Tkinter
        self.disabledButton()
        self.fenetre.mainloop()



app = Board()
app.run()
