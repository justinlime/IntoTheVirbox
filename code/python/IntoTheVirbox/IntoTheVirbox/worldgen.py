from random import Random,randrange 
from IntoTheVirbox.models.room import Room
from IntoTheVirbox.models.world import World
from IntoTheVirbox.models.container import Container

class WorldGenerator:
    def __init__(self, seed=randrange(0,300000)):
        self.random = Random(seed)
        self.max_rooms = 25
        self.max_items = 10
        self.max_container = 15
        self.max_enemies = 10
        self.max_npc = 10

    def genWorld(self):
        world = World(self.getRooms())
        return world

    def genPlayer(self):
        return player

    def genContainers(self,items):
        containers = []
        while len(rooms) < self.max_containers:
            containers.append(Container(items))


    def genItems(self):
        items = []
        while len(rooms) < self.max_containers:
            items.append(Item())

    def genRooms(self):
        rooms = []
        while len(rooms) < self.max_rooms:
            if len(rooms) == 0:
                # First room is always 0,0
                rooms.append(Room((0,0)))
            else:
                #Random exiting room to base new random coordinates off of
                random_room = rooms[self.random.randint(0,len(rooms))-1] 

                # Ensures only x, or y is random
                random_cord = self.random.randint(0, 1)
                if random_cord == 0:
                    new_random_coords = (random_room.coordinates[0],random_room.coordinates[1]-self.random.randint(-1,1))
                else:
                    new_random_coords = (random_room.coordinates[0]-self.random.randint(-1,1),random_room.coordinates[1])
                # Appends if coords dont exist
                if new_random_coords not in [r.coordinates for r in rooms]:
                    rooms.append(Room(new_random_coords))

        def getRoom(coords):
            for room in rooms:
                if coords == room.coordinates:
                    return room

        # Maps direct neighbors (left,right,up,down) to each room
        existing_coordinates = [r.coordinates for r in rooms]
        for room in rooms:
            if (room.coordinates[0]+1,room.coordinates[1]) in existing_coordinates:
                room.right_door = getRoom((room.coordinates[0]+1,room.coordinates[1]))
            if (room.coordinates[0]-1,room.coordinates[1]) in existing_coordinates:
                room.left_door = getRoom((room.coordinates[0]-1,room.coordinates[1]))
            if (room.coordinates[0],room.coordinates[1]+1) in existing_coordinates:
                room.up_door = getRoom((room.coordinates[0],room.coordinates[1]+1))
            if (room.coordinates[0],room.coordinates[1]-1) in existing_coordinates:
                room.down_door = getRoom((room.coordinates[0],room.coordinates[1]-1))

        return rooms



    
