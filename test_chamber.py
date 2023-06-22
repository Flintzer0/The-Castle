from player import Player
import items, world, actions, enemies, time, sys
from combat import combat

player = Player(name="Player", LVL=1, mHP=10, cHP=10, STR=2, DEF=1, MAG=1, RES=0, SPD=2, SKL=2, LUCK=1, cash=5)
enemy_1 = enemies.goblin()
enemy_1.EXP = 100
enemy_2 = enemies.giant_spider()
enemy_2.EXP = 100
enemy_3 = enemies.skeleton()
enemy_3.EXP = 100

def combat_loop_1():
    while player.is_alive() and enemy_1.is_alive() == True:
        combat(player, enemy_1)
        if player.is_alive() == False:
            print("You died.\n")
            time.sleep(2)
            print("Game over.\n")
            time.sleep(2)
            sys.exit()
        elif enemy_1.is_alive() == False:
            player.EXP += enemy_1.EXP
            player.cash += enemy_1.gold
            print("You gained {} EXP!\n".format(enemy_1.EXP))
            time.sleep(2)
            player.level_up()
            print("You gained {} gold!\n".format(enemy_1.gold))
            time.sleep(2)
            print("You have {} gold.\n".format(player.cash))
            time.sleep(2)
            break

def combat_loop_2():
    while player.is_alive() and enemy_2.is_alive() == True:
        combat(player, enemy_2)
        if player.is_alive() == False:
            print("You died.\n")
            time.sleep(2)
            print("Game over.\n")
            time.sleep(2)
            sys.exit()
        elif enemy_2.is_alive() == False:
            player.EXP += enemy_2.EXP
            player.cash += enemy_2.gold
            print("You gained {} EXP!\n".format(enemy_2.EXP))
            time.sleep(2)
            player.level_up()
            print("You gained {} gold!\n".format(enemy_2.gold))
            time.sleep(2)
            print("You have {} gold.\n".format(player.cash))
            time.sleep(2)
            break

def combat_loop_3():
    while player.is_alive() and enemy_3.is_alive() == True:
        combat(player, enemy_3)
        if player.is_alive() == False:
            print("You died.\n")
            time.sleep(2)
            print("Game over.\n")
            time.sleep(2)
            sys.exit()
        elif enemy_3.is_alive() == False:
            player.EXP += enemy_3.EXP
            player.cash += enemy_3.gold
            print("You gained {} EXP!\n".format(enemy_3.EXP))
            time.sleep(2)
            player.level_up()
            print("You gained {} gold!\n".format(enemy_3.gold))
            time.sleep(2)
            print("You have {} gold.\n".format(player.cash))
            time.sleep(2)
            break

combat_loop_1()
combat_loop_2()
combat_loop_3()