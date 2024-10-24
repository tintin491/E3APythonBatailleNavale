import tkinter as tk


class Board:

    def __init__(self):
        self.fenetre = tk.Tk()
        self.buttonsPlayerTour = []  # Stocker les boutons du joueur dont c'est le tour
        self.buttonsPlayerNonTour = []  # Stocker les boutons du joueur dont ce n'est pas le tour
        self.create_widgets()
        self.player = 1  # Débuter avec le joueur 1
        self.start = False

    def create_widgets(self):
        # Ajouter un label
        self.fenetre.geometry("500x600")
        labelTitre = tk.Label(self.fenetre, text="Bataille Navale", font=("Helvetica", 16))
        labelTitre.pack()

        # Création des frames pour les deux grilles
        self.buttonframe1 = tk.Frame(self.fenetre)  # Plateau du joueur
        self.buttonframe2 = tk.Frame(self.fenetre)  # Plateau adverse

        # Label pour le plateau adverse
        label1 = tk.Label(self.fenetre, text="Vos navires", font=("Helvetica", 16))
        label1.pack(pady=(25, 0))

        # Créer les boutons pour le plateau adverse
        for i in range(5):
            row = []
            for j in range(10):
                btn2 = tk.Button(self.buttonframe2, text="", command=lambda a=i, b=j: self.button_change(a, b), width=5,
                                 height=2)
                btn2.grid(row=i, column=j)
                row.append(btn2)
            self.buttonsPlayerNonTour.append(row)
        self.buttonframe2.pack(padx=(25, 0), fill='x')

        # Label pour vos navires
        label2 = tk.Label(self.fenetre, text="Plateau adverse", font=("Helvetica", 16))
        label2.pack(pady=(25, 0))

        # Créer les boutons pour le plateau du joueur
        for i in range(5):
            row = []
            for j in range(10):
                btn1 = tk.Button(self.buttonframe1, text="", command=lambda a=i, b=j: self.button_change(a, b), width=5,
                                 height=2)
                btn1.grid(row=i, column=j)
                row.append(btn1)
            self.buttonsPlayerTour.append(row)
        self.buttonframe1.pack(padx=(25, 0), fill='x')

    def updateWidget(self):
        # Permuter les propriétés des boutons (couleur uniquement) entre les deux grilles
        for i in range(5):
            for j in range(10):
                # Échanger les couleurs entre les deux grilles
                buttonTour = self.buttonsPlayerTour[i][j]
                buttonNonTour = self.buttonsPlayerNonTour[i][j]

                # Sauvegarder la couleur actuelle du bouton du plateau adverse
                tour_bg = buttonTour.cget("bg")

                # Sauvegarder la couleur actuelle du bouton du joueur
                nonTour_bg = buttonNonTour.cget("bg")

                # Échanger les propriétés des boutons
                buttonTour.config(bg=nonTour_bg)
                buttonNonTour.config(bg=tour_bg)

        self.fenetre.update_idletasks()

    def button_change(self, row, col):
        # Lorsque le joueur clique sur un bouton
        button = self.buttonsPlayerTour[row][col]
        if self.player == 1:
            button.config(bg="blue", activebackground="blue")  # Joueur 1
            self.player = 2  # Changer de joueur
        else:
            button.config(bg="red", activebackground="red")  # Joueur 2
            self.player = 1  # Revenir au joueur 1

        # Inverser les données entre les grilles après chaque clic
        self.updateWidget()

    def run(self):
        # Lancer la boucle principale de Tkinter
        self.fenetre.mainloop()


# Démarrer l'application
app = Board()
app.run()
