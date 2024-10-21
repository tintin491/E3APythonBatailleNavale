class Ship :

    def __init__(self, size, direction):
        self.size = size
        self.listPosition = []
        self.direction = direction

    def set_listPosition(self, listposition):
        self.listPosition = listposition

    def get_listPosition(self):
        return self.listPosition