class Room:
    def __init__(self, coordinates):
        self.coordinates = coordinates # List of tuples, (x,y)
        self.left_door = False
        self.right_door = False
        self.up_door = False
        self.down_door = False
        self.discovered=False
        self.containers = []
        self.enemies = []
        self.npcs = []
     
