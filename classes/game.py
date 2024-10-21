from classes.player import Player
from classes.ship import Ship


class Game:

    def __init__(self):

        nameOfP1 = input("Saisir le nom du joueur 1 : ")
        nameOfP2 = input("Saisir le nom du joueur 2 : ")

        playerOne = Player(nameOfP1)
        playerTwo = Player(nameOfP2)
        self.isFinished = False

