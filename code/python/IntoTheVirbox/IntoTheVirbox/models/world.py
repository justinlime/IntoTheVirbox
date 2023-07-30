class World:
    def __init__(self,rooms):
        self.rooms = rooms
        self.map = [room.coordinates for room in rooms]
