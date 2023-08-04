import world, sys, time, magic, skills
from player import *

# This file is for debugging purposes only. It is not part of the game.
# It skips the intro and removes the call for room.intro_text() in game_loop().
# The Debug Player class also removes the intro text for every room.
def play():
    world.load_tiles()
    player = Debug()
    player.name = "Debug"
    game_loop(player)

def game_loop(player):
    room = world.tile_exists(player.location_x, player.location_y)
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
if __name__ == "__main__":
    play()