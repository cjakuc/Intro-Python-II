# Import room
from room import Room

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__ (self, rooms:dict):
        self.all_rooms = rooms
        self.location: Room = list(rooms.values())[0]

    # Modify __str__ method to return current location and description
    def __str__ (self):
        return f"Current location: {self.location.getLocation()}\nDescription: {self.location.getDescription()}"

    # Move in a cardinal direction if possible; update self.location
    def move(self, direction:str):
        outcome = self.location.check_move(direction=direction)
        if outcome != None:
            self.location = outcome
            return "Success"
        else:
            return f"Error: there is not a room towards the {direction}"
        