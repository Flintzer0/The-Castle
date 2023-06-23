import items, world
from utilities import text_speed
import pickle, sys, time, random
import combat

class Player():
    def __init__(self, name, mHP, cHP, STR, DEF, MAG, RES, SPD, SKL, LUCK, LVL, cash):
        self.mHP = mHP
        self.cHP = cHP
        self.name = name
        self.LVL = LVL
        self.EXP = 0
        self.inventory = []
        self.compendium = []
        self.STR = STR
        self.DEF = DEF
        self.MAG = MAG
        self.RES = RES
        self.SPD = SPD
        self.SKL = SKL
        self.LUCK = LUCK
        self.cash = cash
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.mHPgrowth = .6
        self.STRgrowth = .5
        self.DEFgrowth = .4
        self.MAGgrowth = .3
        self.RESgrowth = .2
        self.SPDgrowth = .4
        self.SKLgrowth = .4
        self.LUCKgrowth = .3
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.HP, self.name, self.inventory, self.STR, self.DEF, self.MAG, self.RES, self.SPD, self.SKL, self.LUCK)
 
    def is_alive(self):
        return self.cHP > 0
    
    def chk_stat_roll(self, growth, stat):
        if random.randint(1,100) <= (100 * (growth + (stat * .1))):
            return 1
        else:
            return 0

    def level_up(self):
        if self.EXP >= 100:
            self.LVL += 1
            self.EXP -= 100
            self.mHP += 2 + self.chk_stat_roll(self.mHPgrowth, self.mHP)
            self.cHP = self.mHP
            self.STR += self.chk_stat_roll(self.STRgrowth, self.STR)
            self.DEF += self.chk_stat_roll(self.DEFgrowth, self.DEF)
            self.MAG += self.chk_stat_roll(self.MAGgrowth, self.MAG)
            self.RES += self.chk_stat_roll(self.RESgrowth, self.RES)
            self.SPD += self.chk_stat_roll(self.SPDgrowth, self.SPD)
            self.SKL += self.chk_stat_roll(self.SKLgrowth, self.SKL)
            self.LUCK += self.chk_stat_roll(self.LUCKgrowth, self.LUCK)
            print("You leveled up!\n")
            time.sleep(1)
            print("You are now level {}!\n".format(self.LVL))
            time.sleep(1)
            print("Your max HP is now {}!\n".format(self.mHP))
            time.sleep(1)
            print("Your STR is now {}!\n".format(self.STR))
            time.sleep(1)
            print("Your DEF is now {}!\n".format(self.DEF))
            time.sleep(1)
            print("Your MAG is now {}!\n".format(self.MAG))
            time.sleep(1)
            print("Your RES is now {}!\n".format(self.RES))
            time.sleep(1)
            print("Your SPD is now {}!\n".format(self.SPD))
            time.sleep(1)
            print("Your SKL is now {}!\n".format(self.SKL))
            time.sleep(1)
            print("Your LUCK is now {}!\n".format(self.LUCK))
            time.sleep(1)
        else:
            pass

    def print_inventory(self):
        print(self.cash, "gold\n")
        for item in self.inventory:
            print(item, '\n')
    
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy
        print(world.tile_exists(self.location_x, self.location_y).intro_text())

    def move_north(self):
        room = world.tile_exists(self.location_x, (self.location_y-1))
        if room.unlocked == True:
            self.move(dx=0, dy=-1)
        else:
            print(room.locked_text())
            self.move(dx=0, dy=0)
    
    def move_south(self):
        room = world.tile_exists(self.location_x, (self.location_y+1))
        if room.unlocked == True:
            self.move(dx=0, dy=1)
        else:
            print(room.locked_text())
            self.move(dx=0, dy=0)
    
    def move_east(self):
        room = world.tile_exists((self.location_x+1), self.location_y)
        if room.unlocked == True:
            self.move(dx=1, dy=0)
        else:
            print(room.locked_text())
            self.move(dx=0, dy=0)
    
    def move_west(self):
        room = world.tile_exists((self.location_x-1), self.location_y)
        if room.unlocked == True:
            self.move(dx=-1, dy=0)
        else:
            print(room.locked_text())
            self.move(dx=0, dy=0)

    def add_monster(self):
        monster = world.tile_exists(self.location_x, self.location_y).enemy
        self.compendium.append(monster)

    def view_compendium(self):
        if len(self.compendium) != 0:
            r = range(int(len(self.compendium)))
            for i in r:
                print(f'{i}: {self.compendium[i].name}')
            print(f'{len(self.compendium)}: Exit')
            input("Which monster would you like to view? ")
            if input.isdigit():
                if int(input) < len(self.compendium):
                    print(self.compendium[int(input)].__str__())
                else:
                    print("Invalid choice.")
            elif input == len(self.compendium):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            print("You haven't encountered any monsters yet!")

    def search(self):
        room = world.tile_exists(self.location_x, self.location_y)
        item = room.item
        if item is not None:
            print(room.search_text())
            if isinstance(item, items.gold):
                self.cash += item.amt
                text_speed("You found {} {}!\n".format(item.amt, item.name), .05)
                time.sleep(1)
                text_speed("You now have {} gold!\n".format(self.cash), .05)
            elif isinstance(item, items.Potion):
                self.inventory.append(item)
                text_speed("You found {} {}(s)!\n".format(item.qty, item.name), .05)
            else:
                self.inventory.append(item)
                text_speed("You found a {}!\n".format(item.name), .05)
            room.item = None
        else:
            return room.searched_text()
        
    def fight(self, enemy):
        self.combat(enemy)
        if not enemy.is_alive():
            text_speed("You killed {}!\n".format(enemy.name), .05)
        else:
            text_speed("{} HP is {}.\n".format(enemy.name, enemy.hp), .05)

    def check_inventory(self, item):
        a=[]
        items = []
        if len(self.inventory) != a:
            for i in self.inventory:
                if isinstance(i, item):
                    items.append(i)
                    return items
        return False

    def list_inventory(self, item):
        if self.check_inventory(item) is not False:
            items = self.check_inventory(item)
            n = range(int(len(items)))
            for i in n:
                print(f'{i}: {items[i].name} x{items[i].qty}')
        return False

    def unlock(self, room):
        if self.check_inventory(items.Key) is not False:
            self.list_inventory(items.Key)
            key = input("Which key do you want to use? ")
            if key.isdigit():
                key = int(key)
                if key < len(self.check_inventory(items.Key)):
                    k = self.check_inventory(items.Key)
                    print("You unlocked the door!\n")
                    k[key].unlock -= 1
                    if k[key].unlock == 0:
                        text_speed("The {} broke!\n".format(k[key].name), .05)
                        self.inventory.remove(k[key])
                    room.unlocked = True
                else:
                    print("Invalid choice.")
            else:
                print("Invalid choice.")
        else:
            print("You don't have a key!")

    def use_potion(self):
        if self.cHP != self.mHP:
            if self.list_inventory(items.Potion) is not False:
                potion = input("Which potion do you want to use? ")
                if potion.isdigit():
                    potion = int(potion)
                    if potion < len(self.check_inventory(items.Potion)):
                        p = self.check_inventory(items.Potion)
                        if self.cHP + p[potion].heal > self.mHP:
                            self.cHP = self.mHP
                        if self.cHP + p[potion].heal <= self.mHP:
                            self.cHP += p[potion].heal
                        text_speed("You drink the {}!\n".format(p[potion].name), .05)
                        time.sleep(.5)
                        text_speed("You heal {} HP!\n".format(p[potion].heal), .05)
                        time.sleep(.5)
                        text_speed("Your HP is now {}.".format(self.cHP), .05)
                        time.sleep(.5)
                        p[potion].qty -= 1
                        if p[potion].qty == 0:
                            self.inventory.remove(p[potion])
                    else:
                        print("Invalid choice.")
                        time.sleep(.2)
                else:
                    print("Invalid choice.")
                    time.sleep(.2)
            else:
                text_speed("You don't have any potions!", .05)
        else:
            text_speed("You are already at full health!", .05)
    
    def check_SPD(self, enemy):
        if self.SPD > enemy.SPD:
            return True
        else:
            return False

    def attack(self, enemy):
        best_weapon = None
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
            else:
                if isinstance(i, items.Unarmed):
                    if i.damage > max_dmg:
                        max_dmg = i.damage
                        best_weapon = i

        text_speed("You use {} against {}!\n".format(best_weapon.name, enemy.name))
        damage = best_weapon.damage + self.STR - enemy.DEF
        enemy.hp -= damage
        text_speed("You do {} damage to {}!\n".format(damage, enemy.name))
        if not enemy.is_alive():
            text_speed("You killed {}!\n".format(enemy.name))
        else:
            text_speed("{} HP is {}.\n".format(enemy.name, enemy.hp))

    def save_and_exit(self):
        pickle.dump(self, open( "saved_self.p", "wb" ))
        pickle.dump(world._world, open( "saved_world.p", "wb" ))
        print("Game saved!")
        time.sleep(.5)
        exit()

    def chk_Weapon(self):
        best_weapon = items.Fists()
        max_dmg = 0
        for i in self.inventory:
            if isinstance(i, items.Weapon):
                if i.damage > max_dmg:
                    max_dmg = i.damage
                    best_weapon = i
        return best_weapon

    def chk_armor(self):
        armor = items.unarmored()
        max_armor = 0
        for i in self.inventory:
            if isinstance(i, items.Armor):
                if i.armor > max_armor:
                    max_armor = i.armor
                    armor = i
        return armor

    def chk_SPD(self, enemy):
        if self.SPD > enemy.SPD:
            return True
        elif self.SPD == enemy.SPD:
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

    def pfight(self, enemy):
        text_speed("You attack!", .03)
        best_weapon = self.chk_Weapon()
        chkCRIT = self.chk_CRIT()
        if chkCRIT == True:
            pdamage = (((best_weapon.damage + self.STR) * 2) - enemy.DEF)
            text_speed("You use {} against {}!".format(best_weapon.name, enemy.name), .03)
            time.sleep(.5)
            print("Critical hit!")
            time.sleep(.5)
            enemy.hp -= pdamage
            text_speed("You dealt {} damage to the {}.".format(pdamage, enemy.name), .03)
            time.sleep(.5)
            if enemy.is_alive() == False:
                text_speed("You killed the {}!".format(enemy.name), .03)
                time.sleep(.5)
            else:
                text_speed("The {} has {} HP remaining.".format(enemy.name, enemy.hp), .03)
                time.sleep(.5)
        else:
            pdamage = ((best_weapon.damage + self.STR) - enemy.DEF)
            enemy.hp -= pdamage
            text_speed("You dealt {} damage to the {}.".format(pdamage, enemy.name), .03)
            time.sleep(.5)


    def chk_edamage(self, enemy):
        edamage = None
        armor = self.chk_armor()
        pdef = (self.DEF + armor.armor)
        chkCrit = combat.chk_CRIT(enemy)
        if chkCrit == True:
            text_speed("The {} scores a Critical Hit!".format(enemy.name), .03)
            time.sleep(.5)
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

    def efight(self, enemy):
            text_speed("The {} attacks!".format(enemy.name), .03)
            time.sleep(.5)
            edamage = self.chk_edamage(enemy)
            self.cHP -= edamage
            text_speed("The {} dealt {} damage to you.".format(enemy.name, edamage), .03)
            time.sleep(.5)
            if self.is_alive() == True:
                text_speed("You have {} HP remaining.".format(self.cHP), .03)
                time.sleep(.5)

    def combat(self, enemy):
        chkSPD = self.chk_SPD(enemy)
        if chkSPD == True:
            self.pfight(enemy)
            if enemy.is_alive() == True:
                self.efight(enemy)
            else:
                self.EXP += enemy.EXP
                self.cash += enemy.gold
                text_speed("You killed the {}!".format(enemy.name), .05)
                time.sleep(1)
                text_speed("You gained {} EXP!".format(enemy.EXP), .05)
                time.sleep(1)
                self.level_up()
                text_speed("You gained {} gold!".format(enemy.gold), .05)
                time.sleep(1)
        else:
            self.efight(enemy)
            if self.is_alive() == True:
                self.pfight(enemy)