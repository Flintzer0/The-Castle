from player import Player
import items, world, actions, enemies, time, sys
from combat import combat, chk_Weapon, chk_armor

player = Player(name="Player", mHP=10, cHP=10, STR=2, DEF=1, MAG=1, RES=0, SPD=2, SKL=2, LUCK=1, cash=5)