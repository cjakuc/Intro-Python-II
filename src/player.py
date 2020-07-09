# Import Room
from room import Room
# Import Item
from item import Item

# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__ (self, rooms:dict):
        self.all_rooms = rooms
        self.location: Room = list(rooms.values())[0]
        self.items: list = [Item(name="Flashlight")]

    # Modify __str__ method to return current location and description
    def __str__ (self):
        current_room = self.location
        items_in_room = [item.name for item in current_room.items]
        return f"Current location: {current_room.getLocation()}\nDescription: {current_room.getDescription()}\nItems in room: {items_in_room}"

    # Move in a cardinal direction if possible; update self.location
    def move(self, direction:str):
        outcome = self.location.check_move(direction=direction)
        if outcome != None:
            self.location = outcome
            return "Success"
        else:
            return f"Error: there is not a room towards the {direction}"

    # Get item from current room function
    def getItem(self, names: list):
        items_in_room = self.location.items
        message = ""
        for name in names:
            item_names = [item.name.lower() for item in items_in_room]
            if name in item_names:
                item_index = item_names.index(name)
                self.items.append(items_in_room.pop(item_index))
                message = message + f"{name} has been added to your inventory! "
            else:
                message = message + f"{name} is not in this room. This room contains: {item_names} "
        return message

    # Drop items in current room function
    def dropItem(self, names: list):
        items_on_player = self.items
        message = ""
        for name in names:
            item_names = [item.name.lower() for item in items_on_player]
            if name in item_names:
                item_index = item_names.index(name)
                self.location.items.append(items_on_player.pop(item_index))
                message = message + f"{name} has been dropped! Your inventory has: {items_on_player}"
            else:
                message = message + f"{name} is not in your inventory. Your inventory has: {items_on_player}"
        return message