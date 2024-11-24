import tkinter as tk

class Board:
    def __init__(self, root, player1, player2, fonction):
        self.boat_buttons = None
        self.root = root
        self.root.title("Bataille Navale")

        # Paramètres de la grille
        self.grid_size = 10
        self.cell_size = 50  # Agrandissement des cellules pour une meilleure visibilité
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        self.not_current_Player = player2
        player1.player_board = [[0] * self.grid_size for _ in range(self.grid_size)]
        player2.player_board = [[0] * self.grid_size for _ in range(self.grid_size)]

        self.create_grids()
        self.select_boat = fonction
        self.create_boat_buttons()
        self.add_side_buttons()

    def create_grids(self):
        """Crée trois grilles identiques pour chaque joueur et configure leurs canvases."""
        # Initialisation des données des joueurs
        self.player1.canvas = []
        self.player2.canvas = []

        # Grilles Player 1
        for i in range(3):
            canvas = tk.Canvas(self.root, width=self.grid_size * self.cell_size,
                               height=self.grid_size * self.cell_size, bg="white")
            canvas.grid(row=1, column=1, padx=20, sticky="n")
            self.draw_grid(canvas)
            self.player1.canvas.append(canvas)
            canvas.grid_remove()  # Cacher tous les canvases au départ
        self.player1.canvas[0].grid()  # Afficher canvas1 par défaut

        # Grilles Player 2
        for i in range(3):
            canvas = tk.Canvas(self.root, width=self.grid_size * self.cell_size,
                               height=self.grid_size * self.cell_size, bg="white")
            canvas.grid(row=1, column=3, padx=20, sticky="n")
            self.draw_grid(canvas)
            self.player2.canvas.append(canvas)
            canvas.grid_remove()  # Cacher tous les canvases au départ
        self.player2.canvas[0].grid()  # Afficher canvas1 par défaut


    def draw_grid(self, canvas):
        """Dessine la grille pour le joueur."""
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                x1 = x0 + self.cell_size
                y1 = y0 + self.cell_size
                canvas.create_rectangle(x0, y0, x1, y1, fill="white")

    def create_boat_buttons(self):
        """Créer les boutons pour que le joueur 1 puisse choisir les bateaux à placer."""
        self.boat_buttons = []
        for index, boat in enumerate(self.player1.fleet):
            button = tk.Button(self.root, text=boat.name, command=lambda b=boat: self.select_boat(b))
            button.grid(row=index+2, column=1)  # Alignement à gauche de la grille
            self.boat_buttons.append(button)

    def add_side_buttons(self):
        """Ajoute les boutons '-100', '-200', '-300' à gauche et à droite des grilles."""
        # Boutons à gauche de la grille de gauche
        for i, label in enumerate(["-100", "-200", "-300"]):
            button = tk.Button(self.root, text=label, command=lambda a=i: self.change_canvas(self.player2, a))
            button.grid(row=i+2, column=4, sticky="w")  # Alignement à gauche dans la colonne

        # Boutons à droite de la grille de droite
        for i, label in enumerate(["-100", "-200", "-300"]):
            button = tk.Button(self.root, text=label,command=lambda a=i: self.change_canvas(self.player1, a))
            button.grid(row=i+2, column=0, padx=5, pady=2, sticky="e")  # Alignement à droite dans la colonneqdsgv

    def change_canvas(self, player, canvas_index):
        """Change le canvas affiché pour le joueur donné."""
        # Cacher tous les canvases du joueur
        for canvas in player.canvas:
            canvas.grid_remove()

        # Afficher le canvas sélectionné
        player.canvas[canvas_index].grid()
        player.canvas_actif = canvas_index

        # Mettre à jour l'état des boutons
        self.update_button_state(player.buttons, canvas_index)

    def update_button_state(self, buttons, active_index):
        """Désactive le bouton actif et active les autres."""
        for i, button in enumerate(buttons):
            if i == active_index:
                button.config(state="disabled")
            else:
                button.config(state="normal")

    def run(self):
        # Agrandir la fenêtre principale
        self.root.mainloop()

    def place_ship(self, player, boat, x, y, canvas_actif):
        if boat.isHorizontal:
            boat.move_boat(x, y)
            for i in range(boat.size):
                player.player_board[x + i][y] = 1
                player.canvas[canvas_actif].create_rectangle((x + i) * self.cell_size,
                                               y * self.cell_size,
                                               (x + i + 1) * self.cell_size,
                                               (y + 1) * self.cell_size, fill="gray")

        else:
            boat.move_boat(x, y)
            for i in range(boat.size):
                player.player_board[x][y + i] = 1
                player.canvas[canvas_actif].create_rectangle(x * self.cell_size,
                                               (y + i) * self.cell_size,
                                               (x + 1) * self.cell_size,
                                               (y + i + 1) * self.cell_size, fill="gray")

    # Fonction pour mettre à jour les cases sur le plateau en fonction d'où on tire les joueurs
    def update_case(self, player, x, y, canvas_actif):
        etat_case = player.take_shot(x, y)
        if etat_case == -1:
            player.canvas[canvas_actif].create_rectangle(x * self.cell_size,
                                           y * self.cell_size,
                                           (x + 1) * self.cell_size,
                                           (y + 1) * self.cell_size, fill="blue")
        if etat_case == 2:
            rect_id_tuple = player.canvas[canvas_actif].find_overlapping(x * self.cell_size,
                                                           y * self.cell_size,
                                                           (x + 1) * self.cell_size,
                                                           (y + 1) * self.cell_size)
            rect_id = rect_id_tuple[4]
            player.canvas[canvas_actif].itemconfig(rect_id, fill="red")
