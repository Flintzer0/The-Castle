import world, sys, time, magic, skills
from player import *

# This file is for debugging purposes only. It is not part of the game.
# It skips the intro and removes the call for room.intro_text() in game_loop().
# Due to the nature of player move actions, the player file must also be edited to remove the intro text call from the move action.
def play():
    world.load_tiles()
    import items
    # player = Player(name="Debug", LVL=1, mHP=100, cHP=100, mMP=200, cMP=200, STR=100, DEF=100, MAG=100, RES=100, SPD=100, SKL=100, LUCK=100, cash=5000, char_class="Debug")
    # player.inventory.append(items.cold_iron_sword())
    # player.inventory.append(items.water_ring())
    # player.spells.append(magic.quake())
    # player.spells.append(magic.wind())
    # player.spells.append(magic.smite())
    # player.skills.append(skills.cleave())
    # player.skills.append(skills.sneak_attack())
    # player.skills.append(skills.precision_strike())
    # player.equipped['weapon'] = items.cold_iron_sword()
    # player.equipped['accessory_1'] = items.water_ring()
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