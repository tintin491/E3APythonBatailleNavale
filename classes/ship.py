from operator import truediv


class Ship :

    def __init__(self, size, isHorizontal):
        self.size = size
        self.listPosition = []
        self.isHorizontal = isHorizontal
        self.isSiked = False
        self.cptTouch = 0

    def set_listPosition(self, listposition):
        self.listPosition = listposition

    def get_listPosition(self):
        return self.listPosition

    def set_direction(self, direction):
        return self.direction

    def getLenght(self):
        return self.size

    def get_isHorizontal(self):
        return self.isHorizontal

    def set_isSiked(self):
        if not self.isSiked:
            self.isSiked = True
        else:
            self.isSiked = False

    def hit(self, x, y):
        for i in range(self.size):
            if x == self.listPosition[0] and y == self.listPosition[1]:
                print('Touché')
                self.cptTouch
            else:
                print('Manqué')

            if self.isHorizontal:
                x += 1
            else:
                y += 1

    #Vérifie si toutes les cases du bateau ont été touché
    def isSunk(self):
        if self.size == self.cptTouch:
            return True
        return False
