import world, sys, time, items, magic, skills
from player import *
from utilities import text_speed
from pathlib import Path
import pickle


def play(saved_world=None, saved_player=None):
    if saved_world and saved_player:
        world._world = saved_world
        player = saved_player
    else:
        world.load_tiles()
        text_speed("What is your name?\n", .05)
        name=input()
        text_speed("Alright, " + name + ". What is your class?\n", .05)
        text_speed("1. Fighter\n", .05)
        text_speed("2. Mage\n", .05)
        text_speed("3. Rogue\n", .05)
        text_speed("4. Cleric\n", .05)
        text_speed("5. Paladin\n", .05)
        text_speed("6. Ranger\n", .05)
        class_choice = input()
        if class_choice == '1':
            player = Fighter()
            player.name = name
        elif class_choice == '2':
            player = Mage()
            player.name = name
        elif class_choice == '3':
            player = Rogue()
            player.name = name
        elif class_choice == '4':
            player = Cleric()
            player.name = name
        elif class_choice == '5':
            player = Paladin()
            player.name = name
        elif class_choice == '6':
            player = Ranger()
            player.name = name
    game_loop(player)

def game_loop(player):
    room = world.tile_exists(player.location_x, player.location_y)
    room.intro_text()
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
            text_speed("You died.\n", .05)
            time.sleep(2)
            text_speed("Game over.\n", .05)
            time.sleep(2)
            sys.exit()

def check_for_save():
    if Path("saved_player.p").is_file() and Path("saved_world.p").is_file():
        saved_world = pickle.load(open("saved_world.p", "rb"))
        saved_player = pickle.load(open("saved_player.p", "rb"))
        save_exists = True
    else:
        save_exists = False

    if save_exists:
        valid_input = False
        while not valid_input:
            load = input("Saved game found! Do you want to load the game? Y/N ")
            if load in ['Y','y']:
                play(saved_world, saved_player)
                valid_input = True
            elif load in ['N','n']:
                play()
                valid_input = True
            else:
                print("Invalid choice.")
    else:
        play()

if __name__ == "__main__":
    text_speed("The Castle\n", .05)
    time.sleep(1)
    text_speed("A text-based adventure game\n", .05)
    time.sleep(1)
    check_for_save()