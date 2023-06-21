import time, sys, items
from Player import player
from jail_start import jail_start

the_player = player
the_player(HP = 10,
           name = None,
           inventory = [items.gold(15)],
           STR = 5,
           DEF = 5,
           MAG = 5,
           RES = 5,
           SPD = 5,
           SKL = 5,
           LUCK = 5)
def game_start():
    print("Excellent! We just need to know who you are.")
    time.sleep(1)
    print("What is your name? ")
    _name = input()
    the_player.name = _name
    print("Well then, " + the_player.name + ". Let us start where you belong...")
    time.sleep(5)
    print("THE ", end=" ", flush=True)
    sys.stdout.flush()
    time.sleep(1)
    print("DUNGEON\n")
    time.sleep(1)
    jail_start()