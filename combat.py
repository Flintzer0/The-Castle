import items
import random
import sys

def chk_Weapon(player):
    best_weapon = items.Fists()
    max_dmg = 0
    for i in player.inventory:
        if isinstance(i, items.Weapon):
            if i.damage > max_dmg:
                max_dmg = i.damage
                best_weapon = i
    return best_weapon

def chk_armor(player):
    armor = items.unarmored()
    max_armor = 0
    for i in player.inventory:
        if isinstance(i, items.Armor):
            if i.armor > max_armor:
                max_armor = i.armor
                armor = i
    return armor

def chk_SPD(player, enemy):
    if player.SPD > enemy.SPD:
        return True
    elif player.SPD == enemy.SPD:
        return True
    else:
        return False

def chk_CRIT(object):
    critical = False
    if random.randint(1,100) <= ((object.SKL*2) + object.LUCK):
        critical = True
    else:
        critical = False
    return critical

def pfight(player, enemy):
    print("You attack!")
    best_weapon = chk_Weapon(player)
    chkCRIT = chk_CRIT(player)
    if chkCRIT == True:
        pdamage = (((best_weapon.damage + player.STR) * 2) - enemy.DEF)
        print("You use {} against {}!".format(best_weapon.name, enemy.name))
        print("Critical hit!")
        enemy.hp -= pdamage
        print("You dealt {} damage to the {}.".format(pdamage, enemy.name))
        if enemy.is_alive() == False:
            print("You killed the {}!".format(enemy.name))
        else:
            print("The {} has {} HP remaining.".format(enemy.name, enemy.hp))
    else:
        pdamage = ((best_weapon.damage + player.STR) - enemy.DEF)
        enemy.hp -= pdamage
        print("You dealt {} damage to the {}.".format(pdamage, enemy.name))


def chk_edamage(player, enemy):
    edamage = None
    armor = chk_armor(player)
    pdef = (player.DEF + armor.armor)
    chkCrit = chk_CRIT(enemy)
    if chkCrit == True:
        print("The {} scores a Critical Hit!".format(enemy.name))
        edamage = (enemy.damage * 2)
        if edamage < pdef:
            edamage = 1
            return edamage
        elif edamage == pdef:
            edamage = 1
            return edamage
        else:
            edamage = edamage - pdef
            return edamage
    else:
        edamage = (enemy.damage - pdef)
        if enemy.damage < pdef:
            edamage = 1
            return edamage
        
        elif enemy.damage == pdef:
            edamage = 1
            return edamage
        else:
            edamage = (enemy.damage - pdef)
            return edamage

def efight(player, enemy):
        print("The {} attacks!".format(enemy.name))
        edamage = chk_edamage(player, enemy)
        player.cHP -= edamage
        print("The {} dealt {} damage to you.".format(enemy.name, edamage))
        if player.is_alive() == True:
            print("You have {} HP remaining.".format(player.cHP))

def combat(player, enemy):
    chkSPD = chk_SPD(player, enemy)
    if chkSPD == True:
        pfight(player, enemy)
        if enemy.is_alive() == True:
            efight(player, enemy)
        else:
            print("You killed the {}!".format(enemy.name))
    else:
        efight(player, enemy)
        if player.is_alive() == True:
            pfight(player, enemy)
        else:
            print("You died.")
            sys.exit()