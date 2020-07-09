from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     ["Stone", "Stick"]),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty
                     passages run north and east.""",
                     ["Candlestick", "Clock"]),

    'overlook': Room("Grand Overlook",
                     """A steep cliff appears before you, falling
                     into the darkness. Ahead to the north, a light flickers in
                     the distance, but there is no way across the chasm.""",
                     ["Rope", "Gravel"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                     to north. The smell of gold permeates the air.""",
                     ["Dirt", "Shoe"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                     chamber! Sadly, it has already been completely emptied by
                     earlier adventurers. The only exit is to the south.""",
                     ["Broken Glass", "Torch"]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

game_on = True
player_name = input("What is your name? ")
current_player = Player(name=player_name, rooms=room)
cardinal_directions = ["n", "e", "s", "w"]
# Print current room and description
print(current_player)

while game_on:
    # Get user's input
    user_input = input("What's next? ").lower()
    split_input = user_input.split(" ")

    # If user enters "q", end the game
    if user_input == "q":
        game_on = False
        print("Thanks for playing!")
        break

    # User enters direction, move direction if possible
    elif user_input in cardinal_directions:
        msg = current_player.move(direction=user_input)

        if msg == "Success":
            # Print current room and description
            print(current_player)
        else:
            print(msg)

    elif (split_input[0].lower() == "get") or (split_input[0].lower() == "take"):
        get_items = split_input[1:]
        msg = current_player.getItem(get_items)
        print(msg)

    elif (split_input[0].lower() == "drop"):
        drop_items = split_input[1:]
        msg = current_player.dropItem(drop_items)
        print(msg)

    elif (split_input[0].lower() == "i") or (split_input[0].lower() == "inventory"):
        print(f"Your inventory: {[item.name for item in current_player.items]}")

    else:
        print("Command not found. Input 'q' to quit or a cardinal direction (N,E,S,W) to try to move. Or input get, take, drop ITEM_NAMES.")