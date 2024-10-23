from classes.ship import Ship


class Player:
    def __init__(self, name):

        ship1 = Ship(5, True)
        ship2 = Ship(4, True)
        ship3 = Ship(3, True)
        ship4 = Ship(3, True)
        ship5 = Ship(2, True)

        fleet = [
            ship1,
            ship2,
            ship3,
            ship4,
            ship5
        ]

        self.name = name
        self.fleet = fleet

    #Vérifier l'état des bateaux d'un joueur
    def isAllShipsSunk(self):

        nbShipSike = 0

        for i in range(len(self.fleet)):
            if self.fleet[i].isSiked:
                nbShipSike+=1

        # Retourne Vrai si tous les bateaux sont coulés
        if nbShipSike == len(self.fleet):
            return True

        return False

    def placeShip(self, ship, x, y, isHorizontal, board):

        return

    #Tiré sur une position donnée
    def takeShot(self, x, y, board):

        return

    def getFleet(self):
        return self.fleet

