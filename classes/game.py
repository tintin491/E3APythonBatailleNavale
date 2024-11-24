from classes.player import Player
from classes.ship import Ship
import random
from classes.board import Board

class Game:

    def __init__(self, root):
        self.start_y = None
        self.start_x = None
        self.root = root
        self.board = None
        self.playerOne = None
        self.playerTwo = None
        self.isFinished = False
        self.current_player = None
        self.not_current_player = None
        self.selected_boat = None
        self.placing_phase = True

    def start_game(self):
        name_p1 = input("Saisir le nom du joueur 1 : ")
        name_p2 = input("Saisir le nom du joueur 2 : ")

        ship1 = Ship(5, True, self.root, "Carrier")
        ship2 = Ship(4, True, self.root, "Battleship")
        ship3 = Ship(3, True, self.root, "Cruiser")
        ship4 = Ship(3, True, self.root, "Submarine")
        ship5 = Ship(2, True, self.root, "Destroyer")

        ship6 = Ship(5, True, self.root, "Carrier")
        ship7 = Ship(4, True, self.root, "Battleship")
        ship8 = Ship(3, True, self.root, "Cruiser")
        ship9 = Ship(3, True, self.root, "Submarine")
        ship10 = Ship(2, True, self.root, "Destroyer")

        fleet1 = [
            ship1,
            ship2,
            ship3,
            ship4,
            ship5
        ]

        fleet2 = [
            ship6,
            ship7,
            ship8,
            ship9,
            ship10
        ]

        self.playerOne = Player(name_p1, fleet1)
        self.playerTwo = Player(name_p2, fleet2)

        self.board = Board(self.root,self.playerOne, self.playerTwo, self.select_boat)

        self.current_player = self.playerOne
        self.not_current_player = self.playerTwo

        for i in range(3):
            self.playerOne.canvas[i].bind("<Button-1>",self.select_cell)
            self.playerOne.canvas[i].bind("<ButtonRelease-1>",  self.drop_boat)

    def check_game_over(self):
        cpt = 0
        for i in range(len(self.playerOne.fleet)):
            if self.playerOne.fleet[i].isSiked :
                cpt += 1

        if cpt == len(self.playerOne.fleet):
            return True

        cpt = 0
        for i in range(len(self.playerTwo.fleet)):
            if self.playerOne.fleet[i].isSiked:
                cpt += 1

        if cpt == len(self.playerTwo.fleet):
            return True
        return False

    def select_boat(self, boat):
        """Sélectionner le bateau à placer, si possible."""
        if boat.isPlaced:
            print(f"Le {boat[1]} a déjà été placé !")
            return False
        else:
            self.selected_boat = boat
            print(f"Bateau sélectionné: {boat.name} de taille {boat.size}")
            self.root.bind("<r>", lambda event: self.selected_boat.rotate_boat())
            return True

    def select_cell(self, event):
        if self.placing_phase:
            self.start_x = event.x // self.board.cell_size
            self.start_y = event.y // self.board.cell_size
            print(f"Cellule sélectionnée: ({self.start_x}, {self.start_y})")

    def all_boat_placed(self):
                if all(ship.isPlaced for ship in self.playerOne.fleet) and all(
                        ship.isPlaced for ship in self.playerTwo.fleet):
                    for i in range(3):
                        self.current_player.canvas[i].bind("<Button-1>", self.tirer_ship)
                        self.current_player.canvas[i].unbind("ButtonRelease")
                    self.root.unbind("<r>")
                    print("Tous les joueurs on posé leurs pions")

    def tirer_ship(self,event):
        self.select_cell(event)
        self.board.update_case(self.not_current_player,self.start_x, self.start_y, self.not_current_player.canvas_actif)

    def player_change(self):
        tmp = self.current_player
        self.current_player = self.not_current_player
        self.not_current_player = tmp

    def run(self):
        self.start_game()
        self.board.run()

    def can_place_boat(self, x, y, length, is_horizontal):
        """Vérifie si le bateau peut être placé sur la grille selon son orientation."""
        if is_horizontal:
            if x + length <= self.board.grid_size:
                for i in range(length):
                    if self.playerOne.player_board[y][x + i] != 0:
                        return False
                return True
            print("Le bateaux ne peut pas être positionné ici")
            return False
        else:
            if y + length <= self.board.grid_size:
                for i in range(length):
                    if self.current_player.player_board[y + i][x] != 0:
                        return False
                    return True
                print("Le bateaux ne peut pas être positionné ici")
            return False

    def drop_boat(self,event):
        if self.selected_boat:
            # Vérifer que le bateau tient sur la grille (en fonction de l'orientation)
            if self.can_place_boat(self.start_x, self.start_y, self.selected_boat.size, self.selected_boat.isHorizontal):
                print(f"Bateau {self.selected_boat.name} placé en ({self.start_x}, {self.start_y}), orientation {self.selected_boat}")
                self.place_boat()
                index = [boat for boat in self.playerOne.fleet].index(self.selected_boat)
                self.board.boat_buttons[index].config(state="disabled")
                self.selected_boat = None
                self.root.unbind("<r>")
                self.player_change()
                self.drop_boat_ia()

    def place_boat(self):
        self.board.place_ship(self.current_player, self.selected_boat, self.start_x, self.start_y, self.playerOne.canvas_actif)

    # ----------------------------------------------
    # Fonction pour le joueur 2 qui est un bot
    # ----------------------------------------------

    def place_boat_ia(self,x,y):
        self.selected_boat.move_boat(x,y)
        num_canvas = random.choice([0,1,2])
        self.board.place_ship(self.current_player,self.selected_boat,x,y,num_canvas)
        self.selected_boat = None

    def drop_boat_ia(self):
        tmp_liste = []
        while True:
            while True:
                x = random.randint(0, self.board.grid_size - 1)
                y = random.randint(0, self.board.grid_size - 1)
                if not (x,y) in self.playerTwo.liste_position_select:
                    self.playerTwo.liste_position_select.append((x,y))
                    break

            while True:
                i = random.randint(0, len(self.current_player.fleet) - 1)
                if i not in self.playerTwo.liste_boat_placed:
                    tmp_liste.append(i)
                    break

            boat = self.current_player.fleet[i]
            self.select_boat(boat)
            self.selected_boat.isHorizontal = random.choice([True, False])

            if self.can_place_boat(x, y, self.selected_boat.size, self.selected_boat.isHorizontal):
                break

        self.playerTwo.liste_boat_placed.append(i)
        tmp_liste = self.playerTwo.liste_boat_placed
        print(f"Bateau {self.selected_boat.name} placé en ({x}, {y}), orientation {self.selected_boat}")
        self.place_boat_ia(x,y)
        self.all_boat_placed()
        self.player_change()




