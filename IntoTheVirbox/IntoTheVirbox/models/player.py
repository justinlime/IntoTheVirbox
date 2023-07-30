class Player:
    def __init__(self,startingroom):
        # self.name = name
        # self.strength = strength
        # self.dexterity = dexterity
        # self.charisma = charisma 
        # self.intelligence = intelligence
        # self.luck = luck
        self.health = 100
        self.inventory = []
        self.weight = 0 
        self.room = startingroom


    def useItem(self,item):
        pass

    def moveUp(self):
        if not self.room.up_door:
            return "You hit a wall, dumbass"
        else:
            self.room = self.room.up_door
            return "You moved up"

    def moveDown(self):
        if not self.room.down_door:
            return "You hit a wall, dumbass"
        else:
            self.room = self.room.down_door
            return "You moved down"

    def moveLeft(self):
            if not self.room.left_door:
                return "You hit a wall, dumbass"
            else:
                self.room = self.room.left_door
                return "You moved left"

    def moveRight(self):
            if not self.room.right_door:
                return "You hit a wall, dumbass"
            else:
                self.room = self.room.up_door
                return "You moved right"


