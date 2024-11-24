class Player:
    def __init__(self, name, fleet, liste_player_board = None, liste_canvas = None):
        self.name = name
        self.fleet = fleet
        self.player_board = liste_player_board # 0 = rien, -1 = touché mais rien, 1 = bateau, 2 = bateau touché
        self.canvas= liste_canvas
        self.liste_boat_placed = []
        self.liste_position_select = []
        self.liste_position_boat_placed = []
        self.canvas_actif = 0

    #Vérifier l'état des bateaux d'un joueur
    def is_all_ships_sunk(self):
        nb_ship_sike = 0
        for i in range(len(self.fleet)):
            if self.fleet[i].isSiked:
                nb_ship_sike+=1

        # Retourne Vrai si tous les bateaux sont coulés
        if nb_ship_sike == len(self.fleet):
            return True

        return False

    #Tiré sur une position donnée
    def take_shot(self, x, y):
        if self.player_board[x][y] == 1 :
            for element in self.fleet:
                liste = element.get_liste_position()
                if (x,y) in liste:
                    element.hit(x,y)
                    element.is_sunk()
            return 2
        if self.player_board[x][y] == 0:
            print('Manqué')
            return -1

    def get_fleet(self):
        return self.fleet

