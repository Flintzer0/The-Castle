import items, world, magic
from utilities import *
import pickle, sys, time, random

class Player():
    spcl = []
    inventory = []
    compendium = []
    spells = []

    def __init__(self, name, mHP, cHP, mMP, cMP, STR, DEF, MAG, RES, SPD, SKL, LUCK, LVL, cash):
        self.mHP = mHP
        self.cHP = cHP
        self.name = name
        self.mMP = mMP
        self.cMP = cMP
        self.LVL = LVL
        self.EXP = 0
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
        self.mMPgrowth = .5
        self.STRgrowth = .5
        self.DEFgrowth = .4
        self.MAGgrowth = .3
        self.RESgrowth = .2
        self.SPDgrowth = .4
        self.SKLgrowth = .4
        self.LUCKgrowth = .3
    
    def __str__(self):
        return "{}\n=====\n{}\nLevel: {}\nEXP: {}\nMaximum HP: {}\nStrength: {}\nDefense: {}\nMagic: {}\nResistance: {}\nSpeed: {}\nSkill: {}\nLuck: {}\n".format(self.name, self.LVL, self.EXP, self.mHP, self.STR, self.DEF, self.MAG, self.RES, self.SPD, self.SKL, self.LUCK)
 
    def is_alive(self):
        return self.cHP > 0
    
    def chk_stat_roll(self, growth, stat):
        if random.randint(1,100) <= (100 * (growth + (stat * .1))):
            return 1
        else:
            return 0
        
    def view_character(self):
        print(self.__str__())
        print("Current HP: {}\n".format(self.cHP))

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

    def add_spcl(self):
        for item in self.inventory:
            self.spcl.append(item.spcl)

    def add_statval(self, stat):
        stat = [self.STR, self.DEF, self.MAG, self.RES, self.SPD, self.SKL, self.LUCK]
        for item in self.inventory:
            if item.stat == stat:
                stat += item.value
    
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def move(self, dx, dy):
        import tiles
        self.location_x += dx
        self.location_y += dy
        # print(world.tile_exists(self.location_x, self.location_y).intro_text())
        location = world.tile_exists(self.location_x, self.location_y)
        if isinstance(location, tiles.stairs):
            location.end_demo(self)

    def chk_spcl(self, spcl):
        self.add_spcl()
        if spcl in self.spcl:
            return True
        else:
            return False

    def move_north(self):
        room = world.tile_exists(self.location_x, (self.location_y-1))
        if room.flooded == True and self.chk_spcl("Water Breathing") == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                self.move(dx=0, dy=-1)
            else:
                print(room.locked_text())
                self.move(dx=0, dy=0)
    
    def move_south(self):
        room = world.tile_exists(self.location_x, (self.location_y+1))
        if room.flooded == True and self.chk_spcl("Water Breathing") == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                self.move(dx=0, dy=1)
            else:
                print(room.locked_text())
                self.move(dx=0, dy=0)
    
    def move_east(self):
        room = world.tile_exists((self.location_x+1), self.location_y)
        if room.flooded == True and self.chk_spcl("Water Breathing") == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                self.move(dx=1, dy=0)
            else:
                print(room.locked_text())
                self.move(dx=0, dy=0)
    
    def move_west(self):
        room = world.tile_exists((self.location_x-1), self.location_y)
        if room.flooded == True and self.chk_spcl("Water Breathing") == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                self.move(dx=-1, dy=0)
            else:
                print(room.locked_text())
                self.move(dx=0, dy=0)

    def buy(self, shopkeep):
        shopkeep.display_shop(self)
        item = input("Which item would you like to buy? ")
        if item.isdigit():
            item = int(item)
            if item < len(shopkeep.inventory):
                purchase = shopkeep.inventory[item]
                if self.cash >= purchase.value:
                    self.inventory.append(purchase)
                    self.cash -= purchase.value
                    text_speed("You bought the {}!\n".format(purchase.name), .05)
                    time.sleep(.5)
                    shopkeep.inventory.remove(purchase)
                    text_speed("You now have {} gold!\n".format(self.cash), .05)
                    time.sleep(.5)
                else:
                    text_speed("You don't have enough gold!\n", .05)
                    time.sleep(.5)
            else:
                print("Invalid choice.")
                time.sleep(.2)

    def chk_compendium(self, enemy):
        if len(self.compendium) != 0:
            for m in self.compendium:
                if enemy.__class__ == m.__class__:
                    return True
                else:
                    return False
        else:
            return False

    def add_monster(self, enemy):
        if self.chk_compendium(enemy) == False:
            self.compendium.append(enemy)
            text_speed("You encountered a {} for your first time!\n".format(enemy.name), .03)
            time.sleep(.5)
            text_speed("You added the {} to your Monster Compendium!\n".format(enemy.name), .03)
            time.sleep(.5)
        else:
            pass

    def view_compendium(self):
        if len(self.compendium) != 0:
            r = range(int(len(self.compendium)))
            for i in r:
                print(f'{i}: {self.compendium[i].name}')
            print(f'{len(self.compendium)}: Exit')
            monster = input("Which monster would you like to view? \n")
            if monster.isdigit():
                if int(monster) < len(self.compendium):
                    print("\n" + self.compendium[int(monster)].__str__())
                elif int(monster) == len(self.compendium):
                    pass
                else:
                    print("Invalid choice.")
            elif monster == len(self.compendium):
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
            elif isinstance(item, items.cold_iron_sword):
                if room.choice == "1":
                    text_speed("You offer your blood to the altar.\n", .05)
                    time.sleep(1)
                    self.cHP -= 20
                    if self.is_alive() == True:
                        self.inventory.append(item)
                        text_speed("You've obtained the {}!\n".format(item.name), .05)
                    else:
                        text_speed("You died.\n", .05)
                        time.sleep(1)
                        print("Game over.\n")
                        time.sleep(1)
                        sys.exit()
                elif room.choice == "2":
                    text_speed("You leave the altar alone.\n", .05)
                    time.sleep(1)
            else:
                self.inventory.append(item)
                text_speed("You found a {}!\n".format(item.name), .05)
            room.item = None
        else:
            return room.searched_text()
        
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
                print(f'{i}: {items[i].name} x{items[i].qty}\n{i}: Exit')
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
            if self.check_inventory(items.Potion) is not False:
                self.list_inventory(items.Potion)
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

    def save_and_exit(self):
        pickle.dump(self, open( "saved_self.p", "wb" ))
        pickle.dump(world._world, open( "saved_world.p", "wb" ))
        print("Game saved!")
        time.sleep(.5)
        exit()

    # def chk_monster_part(self, enemy):
    #     enemy_part = None
    #     for enemy in enemies.Enemy.__subclasses__():
    #         for p in items.monster_part.__subclasses__():
    #             if enemy == p.epart:
    #                 enemy_part = p
    #     return enemy_part
    
    # def monster_part_drop(self, enemy):
    #     enemy_part = self.chk_monster_part(enemy)
    #     if enemy_part is not None:
    #         if random.randint(1,100) <= ((((enemy_part.drop_rate) * 100) - (enemy_part.rarity * 2)) + (self.LUCK * 2)):
    #             self.inventory.append(enemy_part)
    #             text_speed("The {} dropped a {}!\n".format(enemy.name, enemy_part.name), .05)
    #             time.sleep(.5)
    #         else:
    #             pass
    #     else:
    #         pass

    def fight(self, enemy):
        # for item in self.inventory:
        #     self.add_statval(item)
        self.combat(enemy)
        if not enemy.is_alive():
            exp = round(enemy.EXP * (((10-self.LVL)+1)/10))
            self.EXP += exp
            self.cash += enemy.gold
            text_speed("You killed the {}!\n".format(enemy.name), .03)
            time.sleep(1)
            text_speed("You gained {} EXP!\n".format(exp), .03)
            time.sleep(1)
            self.level_up()
            text_speed("You gained {} gold!\n".format(enemy.gold), .03)
            time.sleep(1)
            if self.chk_compendium(enemy) == False:
                self.add_monster(enemy)
            # self.monster_part_drop(enemy)

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
                    max_armor += i.armor
                    armor = max_armor
        return armor

    def chk_SPD(self, enemy):
        return self.SPD >= enemy.SPD

    def pfight(self, enemy):
        text_speed("You attack!\n", .03)
        best_weapon = self.chk_Weapon()
        cCRIT = chk_CRIT(self)
        pdamage = self.generate_damage(self.STR, best_weapon, enemy)
        text_speed("You use {}!\n".format(best_weapon.name), .03)
        time.sleep(.5)
        if cCRIT == True:
            pdamage *= 2
            text_speed("Critical hit!\n", .01)
            time.sleep(.5)
        text_speed("You dealt {} damage to the {}.\n".format(pdamage, enemy.name), .03)
        enemy.hp -= (pdamage - enemy.DEF)

    def chk_edamage(self, enemy):
        edamage = None
        armor = self.chk_armor()
        pdef = (self.DEF + armor.armor)
        cCRIT = chk_CRIT(enemy)
        if cCRIT == True:
            text_speed("The {} scores a Critical Hit!\n".format(enemy.name), .01)
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
            text_speed("The {} attacks!\n".format(enemy.name), .03)
            time.sleep(.5)
            edamage = self.chk_edamage(enemy)
            self.cHP -= edamage
            text_speed("The {} dealt {} damage to you.\n".format(enemy.name, edamage), .03)
            time.sleep(.5)
            if self.is_alive() == True:
                text_speed("You have {} HP remaining.\n".format(self.cHP), .03)
                time.sleep(.5)

    def combat(self, enemy):
        text_speed("What will you do?\n", .05)
        time.sleep(.5)
        choice = input("1. Attack\n2. Cast Spell\n")
        if choice == "1":
            chkSPD = self.chk_SPD(enemy)
            if chkSPD == True:
                self.pfight(enemy)
                if enemy.is_alive() == True:
                    self.efight(enemy)
            else:
                self.efight(enemy)
                if self.is_alive() == True:
                    self.pfight(enemy)
        elif choice == "2":
            chkSPD = self.chk_SPD(enemy)
            spell = self.cast_spell()
            if chkSPD == True:
                self.pmagatk(enemy, spell)
                if enemy.is_alive() == True:
                    self.efight(enemy)
            else:
                self.efight(enemy)
                if self.is_alive() == True:
                    self.pmagatk(enemy, spell)

    def chk_spells(self):
        spell = []
        for i in self.spells:
            if isinstance(i, magic.Spell):
                spell.append(i)
        return spell
    
    def list_spells(self):
        spell = self.chk_spells()
        n = range(int(len(spell)))
        for i in n:
            print(f'{i}: {spell[i].name}')

    def cast_spell(self):
        self.list_spells()
        text_speed("Which spell do you want to cast? ", .05)
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(self.chk_spells()):
                return self.chk_spells()[choice]

    def generate_damage(self, stat, attack, enemy):
        adamage = attack.damage
        eweak = chk_weakness(enemy)
        if attack.damage_type == eweak:
            text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
            return random.randrange(1 + stat, stat + (adamage * 2))
        else:
            return random.randrange(1 + stat, stat + adamage)

    def pmagatk(self, enemy, spell):
        text_speed("You cast {}!\n".format(spell.name), .05)
        time.sleep(.5)
        pdamage = self.generate_damage(self.MAG, spell, enemy)
        if chk_CRIT(self) == True:
            pdamage *= 2
            text_speed("Critical hit!\n", .01)
            time.sleep(.5)
        text_speed("You dealt {} damage to the {}.\n".format(pdamage, enemy.name), .05)
        enemy.hp -= (pdamage - enemy.RES)

class Fighter(Player):
    def __init__(self):
        super.__init__(self, mHP=20, cHP=20, mMP=10, cMP=10, STR=3, DEF=2, MAG=0, RES=0, SPD=1, SKL=2, LUCK=1, cash=5)
        self.inventory.append(items.rusty_sword)
        self.inventory.append(items.rusty_armor)
        self.spells.append(magic.quake)
        self.mHPgrowth = .7
        self.mMPgrowth = .3
        self.STRgrowth = .7
        self.DEFgrowth = .5
        self.MAGgrowth = .2
        self.RESgrowth = .1
        self.SPDgrowth = .3
        self.SKLgrowth = .4
        self.LUCKgrowth = .3

class Mage(Player):
    def __init__(self):
        super.__init__(self, mHP=10, cHP=10, mMP=25, cMP=25, STR=1, DEF=0, MAG=3, RES=2, SPD=2, SKL=2, LUCK=1, cash=5)
        self.inventory.append(items.wooden_staff)
        self.inventory.append(items.cloth_armor)
        self.spells.append(magic.fire)
        self.spells.append(magic.ice)
        self.spells.append(magic.shock)
        self.mHPgrowth = .2
        self.mMPgrowth = .7
        self.STRgrowth = .1
        self.DEFgrowth = .2
        self.MAGgrowth = .8
        self.RESgrowth = .5
        self.SPDgrowth = .4
        self.SKLgrowth = .3
        self.LUCKgrowth = .3

class Rogue(Player):
    def __init__(self):
        super.__init__(self, mHP=15, cHP=15, mMP=15, cMP=15, STR=2, DEF=1, MAG=1, RES=1, SPD=3, SKL=3, LUCK=2, cash=15)
        self.inventory.append(items.rusty_dagger)
        self.inventory.append(items.luck_1_ring)
        self.spells.append(magic.poison)
        self.mHPgrowth = .3
        self.mMPgrowth = .4
        self.STRgrowth = .4
        self.DEFgrowth = .2
        self.MAGgrowth = .2
        self.RESgrowth = .1
        self.SPDgrowth = .7
        self.SKLgrowth = .7
        self.LUCKgrowth = .5