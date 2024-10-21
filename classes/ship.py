class Ship :

    def __init__(self, size, direction, isSiked):
        self.size = size
        self.listPosition = []
        self.direction = direction
        self.isSiked = False

    def set_listPosition(self, listposition):
        self.listPosition = listposition

    def get_listPosition(self):
        return self.listPosition

    def set_direction(self, direction):
        return self.direction

    def set_isSiked(self):
        if not self.isSiked:
            self.isSiked = True
        else:
            self.isSiked = False