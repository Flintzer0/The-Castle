import world, sys, time, items, magic, skills
from player import *
from utilities import text_speed
from pathlib import Path
import os
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
            print('x: Save and Exit')
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break
                elif action_input == 'x':
                    save_game(player)
                    break
        else:
            text_speed("You died.\n", .05)
            time.sleep(2)
            text_speed("Game over.\n", .05)
            time.sleep(2)
            sys.exit()

def save_game(player):
    pickle.dump(player, open("saved_games\{}.p".format(player.name), "wb"))
    pickle.dump(world._world, open("saved_games\{}_saved_world.p".format(player.name), "wb"))
    print("Game saved.")
    time.sleep(.5)
    exit()

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
        print('{}. Back'.format(str(i + 1)))
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
            elif choice == len(saves):
                menu()
            else:
                print("Invalid choice.")
                chk_save()

def menu():
    print("1. New Game    2. Load Game    3. Exit")
    choice = input()
    if choice == '1':
        play()
    elif choice == '2':
        chk_save()
    elif choice == '3':
        text_speed("Farewell!\n", .05)
        sys.exit()

if __name__ == "__main__":
    text_speed("The Castle\n", .05)
    time.sleep(1)
    text_speed("A text-based adventure game\n", .05)
    time.sleep(1)
    menu()