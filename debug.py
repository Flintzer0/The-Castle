import world, sys, time, items
from player import Player
from utilities import text_speed
from pathlib import Path
import pickle

# This file is for debugging purposes only. It is not part of the game.
# It skips the intro and removes the call for room.intro_text() in game_loop().
def play():
    world.load_tiles()
    player = Player(name="Debug", LVL=2, mHP=10, cHP=10, STR=2, DEF=1, MAG=1, RES=0, SPD=2, SKL=100, LUCK=1, cash=5)
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
        else:
            print("You died.\n")
            time.sleep(2)
            print("Game over.\n")
            time.sleep(2)
            sys.exit()

if __name__ == "__main__":
    play()