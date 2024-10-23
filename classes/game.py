from classes.player import Player
from classes.ship import Ship


class Game:

    def __init__(self):

        self.playerOne = None
        self.playerTwo = None
        self.isFinished = False
        self.turnOf = None
        self.startGame()

    def startGame(self):

        nameOfP1 = input("Saisir le nom du joueur 1 : ")
        nameOfP2 = input("Saisir le nom du joueur 2 : ")

        playerOne = Player(nameOfP1)
        playerTwo = Player(nameOfP2)

        self.turnOf = playerOne


    def checkGameOver(self):
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

    def switchTurn(self):
        self.turnOf = self.playerTwo if self.turnOf == self.playerOne else self.playerOne

    def getCurrentPlayer(self):
        return self.turnOf

    def playTurn(self, x, y):
