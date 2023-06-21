import world, sys, time, items
from player import Player
from pathlib import Path
import pickle


def play(saved_world=None, saved_player=None):
    if saved_world and saved_player:
        world._world = saved_world
        player = saved_player
    else:
        world.load_tiles()
        name=input("What is your name? ")
        player = Player(name=name, mHP=10, cHP=10, STR=2, DEF=1, MAG=1, RES=0, SPD=2, SKL=2, LUCK=1, cash=5)
    game_loop(player)

def game_loop(player):
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
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
    title = "The Castle\n"
    for l in title:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    subtitle = "A simple text-based adventure\n"
    for l in subtitle:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.05)
    time.sleep(2)
    check_for_save()