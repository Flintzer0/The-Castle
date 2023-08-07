import world, sys, time, magic, skills
from player import *
from utilities import text_speed
from pathlib import Path
import os

# This file is for debugging purposes only. It is not part of the game.
# It skips the intro and removes the call for room.intro_text() in game_loop().
# The Debug Player class also removes the intro text for every room.
def play(saved_world=None, saved_player=None):
    if saved_world and saved_player:
        world._world = saved_world
        player = saved_player
    else:
        world.load_tiles()
        player = Debug()
        player.name = "Debug"
    game_loop(player)

def save_game(player):
    pickle.dump(player, open("saved_games\{}.p".format(player.name), "wb"))
    pickle.dump(world._world, open("saved_games\{}_saved_world.p".format(player.name), "wb"))
    print("Game saved.")
    time.sleep(.5)
    exit()

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
            print('x: Save and Exit Game')
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
                elif action_input == 'x':
                    save_game(player)
                    break

def chk_save():
    saves = []
    worlds = []
    filename = None
    if Path('saved_games/').rglob('*.p'):
        i = 0
        for file in os.listdir("saved_games/"):
            if file.endswith(".p"):
                if file.endswith("world.p"):
                    worlds.append(file)
                else:
                    i = i + 1
                    saves.append(file)
                    filename = os.path.splitext(file)[0]
                    print('{}. {}'.format(str(i), filename))
        text_speed("Which save file do you want to load?\n", .05)
        choice = input()
        if choice.isdigit() == True:
            choice = int(choice) - 1
            if choice < len(saves):
                saved_player = pickle.load(open("saved_games\{}".format(saves[choice]), "rb"))
                filename = os.path.splitext(saves[choice])[0]
                for a in worlds:
                    if a == filename + '_saved_world.p':
                        saved_world = pickle.load(open("saved_games\{}".format(a), "rb"))
                        play(saved_world, saved_player)
            else:
                print("Invalid choice.")
                chk_save()

if __name__ == "__main__":
    chk_save()