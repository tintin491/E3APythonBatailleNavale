class Ship :

    def __init__(self, size, is_horizontal, root, name):
        self.size = size
        self.current_x = None
        self.current_y = None
        self.isHorizontal = is_horizontal
        self.isSiked = False
        self.cpt_touch = 0
        self.isPlaced = False
        self.name = name
        self.root = root

    def get_position(self):
        return self.current_x ,  self.current_y

    def rotate_boat(self):
        self.isHorizontal = not self.isHorizontal
        print(f"Rotation effectuée: nouvelle orientation {'horizontal' if self.isHorizontal else 'vertical'}")

    def move_boat(self, x, y):
        """Déplacement du bateau sélectionné."""
        self.current_x = x
        self.current_y = y
        self.isPlaced = True

    def get_lenght(self):
        return self.size

    def get_liste_position(self):
        liste = []
        if self.isHorizontal:
            for i in range(self.size):
                liste.append((self.current_x + i, self.current_y))
        else:
            for i in range(self.size):
                liste.append((self.current_x, self.current_y + i))
        return liste

    def get_is_horizontal(self):
        return self.isHorizontal

    def set_is_siked(self):
        if not self.isSiked:
            self.isSiked = True
        else:
            self.isSiked = False

    def hit(self, x, y):
        if self.isHorizontal:
            for i in range(self.size):
                if (x+i) == self.current_x and y == self.current_y:
                    print('Touché')
                    self.cpt_touch+=1
        else:
            for i in range(self.size):
                if x == self.current_x and (y+i) == self.current_y:
                    print('Touché')
                    self.cpt_touch+=1

        return True

    #Vérifie si toutes les cases du bateau ont été touché
    def is_sunk(self):
        if self.size == self.cpt_touch:
            return True
        return False


