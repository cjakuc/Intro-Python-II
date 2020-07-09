# Import Item
from item import Item

# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__ (self, name: str, description: str, items: list):
        self.name = name
        self.description = description
        self.items = [Item(name=item) for item in items]
        self.n_to: Room = None
        self.e_to: Room = None
        self.s_to: Room = None
        self.w_to: Room = None 

    def getLocation(self):
        return self.name

    def getDescription(self):
        return self.description

    # def n_to(self, new_room):
    #     self.north = new_room
    # def e_to(self, new_room):
    #     self.east = new_room
    # def s_to(self, new_room):
    #     self.south = new_room
    # def w_to(self, new_room):
    #     self.west = new_room

    def check_move(self, direction: str):
        if direction == "north":
            return self.n_to
        elif direction == "east":
            return self.e_to
        elif direction == "south":
            return self.s_to
        elif direction == "west":
            return self.w_to