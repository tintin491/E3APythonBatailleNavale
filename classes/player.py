class Player:
    def __init__(self, name):

        ship1 = Ship(5, 'Horizontal')
        ship2 = Ship(4, 'Horizontal')
        ship3 = Ship(3, 'Horizontal')
        ship4 = Ship(3, 'Horizontal')
        ship5 = Ship(2, 'Horizontal')

        listOfShip = [
            ship1,
            ship2,
            ship3,
            ship4,
            ship5
        ]

            self.name = name
            self.listShip = listOfShip

    def placer_bateau(self, bateau):
        return

    def chercher_bateau(self, bateau):
        return