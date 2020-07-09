from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
current_player = Player(rooms=room)
cardinal_directions = ["north", "east", "south", "west"]
# Print current room and description
print(current_player)

while game_on:
    # Save current location to a variable
    # location = current_player.getLocation()

    # Print the current room
    # print(f"The current room is: {location}")
    # # Print description of current room
    # print(f"Description: {room[location].getDescription()}")

    # Get user's input
    user_input = input("What's next? ").lower()

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

    else:
        print("Command not found. Input 'q' to quit or a cardinal direction to try to move.")