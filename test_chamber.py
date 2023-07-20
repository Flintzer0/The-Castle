from player import Player
import items

player = Player(name="Debug", LVL=1, mHP=100, cHP=100, STR=10, DEF=10, MAG=10, RES=10, SPD=10, SKL=100, LUCK=100, cash=5000)
player.inventory.append(items.water_ring())
player.add_spcl()

print(player.chk_spcl("Water Breathing"))