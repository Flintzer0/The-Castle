import world, items, magic, skills
from utilities import *
import pickle, sys, time, random

class Player():
    spcl = []
    inventory = []
    compendium = []
    spells = []
    skills = []
    equipped = {
        'weapon': items.Fists(),
        'armor': items.unarmored(),
        'shield': items.open_hand(),
        'accessory_1': items.empty(),
        'accessory_2': items.empty(),
        'accessory_3': items.empty(),
        'accessory_4': items.empty(),
    }
    status = {
        'poison': False,
        'paralysis': False,
        'blind': False,
        'silence': False,
        'sleep': False,
        'confusion': False,
        'charm': False,
        'crippled': False,
        'water_breathing': False
        }
    materials = {
        items.wood_plank(0).name: 0,
        items.wood_crossguard(0).name: 0,
        items.stone(0).name: 0,
        items.iron_ore(0).name: 0,
        items.amethyst(0).name: 0,
        items.garnet(0).name: 0,
        items.opal(0).name: 0,
        items.ruby(0).name: 0,
        items.sapphire(0).name: 0,
        items.emerald(0).name: 0,
        items.topaz(0).name: 0,
        items.diamond(0).name: 0,
        items.spider_silk(0).name: 0,
        items.spider_leg(0).name: 0,
        items.goblin_fingernail(0).name: 0,
        items.goblin_ear(0).name: 0,
        items.bone(0).name: 0,
        items.femur_bone(0).name: 0,
        items.rat_fur(0).name: 0,
        items.rat_tail(0).name: 0,
        items.bat_wing(0).name: 0,
        items.rotting_flesh(0).name: 0,
        items.centipede_carapace(0).name: 0
    }

    def __init__(self, name, mHP, cHP, mMP, cMP, STR, DEF, MAG, RES, SPD, SKL, LUCK, LVL, cash, char_class):
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
        self.AVO = (self.SPD + self.SKL) + ((self.SPD + self.SKL) * (self.LUCK / random.randint(1, 100)))
        self.char_class = char_class
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
        return "{}    Class: {}\n======================\nLevel: {}    EXP: {}\nHP: {}/{} MP: {}/{}\nSTR: {}    DEF: {}\nMAG: {}    RES: {}\nSPD: {}    SKL: {}\nLUCK: {}\n".format(self.name, self.char_class, self.LVL, self.EXP, self.cHP, self.mHP, self.cMP, self.mMP, self.STR, self.DEF, self.MAG, self.RES, self.SPD, self.SKL, self.LUCK)
    
    def __repr__(self):
        return self.name
 
    def is_alive(self):
        return self.cHP > 0
    
    def chk_stat_roll(self, growth, stat):
        if random.randint(1,100) <= (100 * (growth + (stat * .1))):
            return 1
        else:
            return 0
        
    def view_character(self):
        print("\n" + self.__str__())

    def level_up(self):
        if self.EXP >= 100:
            self.LVL += 1
            self.EXP -= 100
            self.mHP += 5 + self.chk_stat_roll(self.mHPgrowth, self.mHP)
            self.cHP = self.mHP
            self.mMP += 2 + self.chk_stat_roll(self.mMPgrowth, self.mMP)
            self.cMP = self.mMP
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

    def menu(self):
        print("1. View Character  2. View Inventory  3. View Compendium  4. View Spells  5. View Skills  6. Equip  7. Exit\n")
        text_speed("What would you like to do?\n", .05)
        choice = input()
        if choice == "1":
            self.view_character()
        elif choice == "2":
            self.print_inventory()
        elif choice == "3":
            self.view_compendium()
        elif choice == "4":
            self.print_spells()
        elif choice == "5":
            self.print_skills()
        elif choice == "6":
            self.equip()
        elif choice == "7":
            pass

    def print_inventory(self):
        print(self.cash, "gold\n")
        for item in self.inventory:
            print(item, '\n')

    def print_spells(self):
        for spell in self.spells:
            print(spell, '\n')

    def print_skills(self):
        for skill in self.skills:
            print(skill, '\n')

    def equip(self):
        print("Weapon: {}  Shield: {}  Armor: {}\n".format(self.equipped['weapon'].name, self.equipped['shield'].name, self.equipped['armor'].name))
        print("Accessory 1: {}  Accessory 2: {}  Accessory 3: {}  Accessory 4: {}\n".format(self.equipped['accessory_1'].name, self.equipped['accessory_2'].name, self.equipped['accessory_3'].name, self.equipped['accessory_4'].name))
        text_speed("What would you like to equip?\n", .05)
        text_speed("1. Weapon\n", .05)
        text_speed("2. Armor\n", .05)
        text_speed("3. Accessory\n", .05)
        text_speed("4. Exit\n", .05)
        choice = input()
        if choice == "1":
            self.equip_weapon()
        elif choice == "2":
            self.equip_armor()
        elif choice == "3":
            self.equip_accessory_slots()
        elif choice == "4":
            pass

    def unequip(self):
        print("Weapon: {}  Shield: {}  Armor: {}\n".format(self.equipped['weapon'].name, self.equipped['shield'].name, self.equipped['armor'].name))
        print("Accessory 1: {}  Accessory 2: {}  Accessory 3: {}  Accessory 4: {}\n".format(self.equipped['accessory_1'].name, self.equipped['accessory_2'].name, self.equipped['accessory_3'].name, self.equipped['accessory_4'].name))
        text_speed("What would you like to unequip?\n", .05)
        text_speed("1. Weapon\n", .05)
        text_speed("2. Armor\n", .05)
        text_speed("3. Accessory\n", .05)
        text_speed("4. Exit\n", .05)
        choice = input()
        if choice == "1":
            self.unequip_weapon()
        elif choice == "2":
            self.unequip_armor()
        elif choice == "3":
            self.unequip_accessory_slots()
        elif choice == "4":
            pass

    def list_weapons(self):
        weapons = []
        for item in self.inventory:
            if isinstance(item, items.Weapon):
                weapons.append(item)
        return weapons
    
    def list_armor(self):
        armor = []
        for item in self.inventory:
            if isinstance(item, items.Armor):
                armor.append(item)
        return armor
    
    def list_shields(self):
        shields = []
        for item in self.inventory:
            if isinstance(item, items.Shield):
                shields.append(item)
        return shields
    
    def list_accessories(self):
        accessories = []
        for item in self.inventory:
            if isinstance(item, items.Accessory):
                accessories.append(item)
        return accessories
    
    def equip_weapon(self):
        weapons = self.list_weapons()
        if len(weapons) != 0:
            n = range(int(len(weapons)))
            for i in n:
                print(f'{i}: {weapons[i].name}')
            print(f'{len(weapons)}: Exit')
            weapon = input("Which weapon do you want to equip? ")
            if weapon.isdigit():
                weapon = int(weapon)
                if weapon < len(weapons):
                    if self.equipped['weapon'] != items.Fists():
                        self.unequip_weapon()
                    self.equipped['weapon'] = weapons[weapon]
                    self.inventory.remove(weapons[weapon])
                    text_speed("You equipped the {}!\n".format(weapons[weapon].name), .05)
                elif weapon == len(weapons):
                    pass
                else:
                    print("Invalid choice.")
            elif weapon == len(weapons):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            text_speed("You don't have any weapons!", .05)

    def unequip_weapon(self):
        if self.equipped['weapon'] != items.Fists():
            self.inventory.append(self.equipped['weapon'])
            self.equipped['weapon'] = items.Fists()
            text_speed("You unequipped your weapon!\n", .05)
        else:
            text_speed("You don't have a weapon equipped!\n", .05)

    def equip_armor(self):
        armor = self.list_armor()
        if len(armor) != 0:
            n = range(int(len(armor)))
            for i in n:
                print(f'{i}: {armor[i].name}')
            print(f'{len(armor)}: Exit')
            armor = input("Which armor do you want to equip? ")
            if armor.isdigit():
                armor = int(armor)
                if armor < len(armor):
                    if self.equipped['armor'] != items.unarmored():
                        self.unequip_armor()
                    self.equipped['armor'] = armor[armor]
                    self.inventory.remove(armor[armor])
                    text_speed("You equipped the {}!\n".format(armor[armor].name), .05)
                elif armor == len(armor):
                    pass
                else:
                    print("Invalid choice.")
            elif armor == len(armor):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            text_speed("You don't have any armor!", .05)

    def unequip_armor(self):
        if self.equipped['armor'] != items.unarmored():
            self.inventory.append(self.equipped['armor'])
            self.equipped['armor'] = items.unarmored()
            text_speed("You unequipped your armor!\n", .05)
        else:
            text_speed("You don't have any armor equipped!\n", .05)

    def equip_shield(self):
        shields = self.list_shields()
        if len(shields) != 0:
            n = range(int(len(shields)))
            for i in n:
                print(f'{i}: {shields[i].name}')
            print(f'{len(shields)}: Exit')
            shield = input("Which shield do you want to equip? ")
            if shield.isdigit():
                shield = int(shield)
                if shield < len(shields):
                    if self.equipped['shield'] != items.open_hand():
                        self.unequip_shield()
                    self.equipped['shield'] = shields[shield]
                    self.inventory.remove(shields[shield])
                    text_speed("You equipped the {}!\n".format(shields[shield].name), .05)
                elif shield == len(shields):
                    pass
                else:
                    print("Invalid choice.")
            elif shield == len(shields):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            text_speed("You don't have any shields!", .05)

    def unequip_shield(self):
        if self.equipped['shield'] != items.open_hand():
            self.inventory.append(self.equipped['shield'])
            self.equipped['shield'] = items.open_hand()
            text_speed("You unequipped your shield!\n", .05)
        else:
            text_speed("You don't have a shield equipped!\n", .05)

    def equip_accessory_slots(self):
        print("Accessory 1: {}  Accessory 2: {}  Accessory 3: {}  Accessory 4: {}\n".format(self.equipped['accessory_1'].name, self.equipped['accessory_2'].name, self.equipped['accessory_3'].name, self.equipped['accessory_4'].name))
        text_speed("Which accessory slot do you want to equip?\n", .05)
        text_speed("1. Accessory 1\n", .05)
        text_speed("2. Accessory 2\n", .05)
        text_speed("3. Accessory 3\n", .05)
        text_speed("4. Accessory 4\n", .05)
        text_speed("5. Exit\n", .05)
        choice = input()
        if choice == "1":
            self.equip_accessory_1()
        elif choice == "2":
            self.equip_accessory_2()
        elif choice == "3":
            self.equip_accessory_3()
        elif choice == "4":
            self.equip_accessory_4()
        elif choice == "5":
            pass

    def equip_accessory_1(self):
        accessories = self.list_accessories()
        if len(accessories) != 0:
            n = range(int(len(accessories)))
            for i in n:
                print(f'{i}: {accessories[i].name}')
            print(f'{len(accessories)}: Exit')
            accessory = input("Which accessory do you want to equip? ")
            if accessory.isdigit():
                accessory = int(accessory)
                if accessory < len(accessories):
                    if self.equipped['accessory_1'] != items.empty():
                        self.unequip_accessory_1()
                    self.equipped['accessory_1'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.STR += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.DEF += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.MAG += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.RES += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.SPD += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.SKL += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.LUCK += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    self.inventory.remove(accessories[accessory])
                elif accessory == len(accessories):
                    pass
                else:
                    print("Invalid choice.")
            elif accessory == len(accessories):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            text_speed("You don't have any accessories!", .05)

    def equip_accessory_2(self):
        accessories = self.list_accessories()
        if len(accessories) != 0:
            n = range(int(len(accessories)))
            for i in n:
                print(f'{i}: {accessories[i].name}')
            print(f'{len(accessories)}: Exit')
            accessory = input("Which accessory do you want to equip? ")
            if accessory.isdigit():
                accessory = int(accessory)
                if accessory < len(accessories):
                    if self.equipped['accessory_2'] != items.empty():
                        self.unequip_accessory_2()
                    self.equipped['accessory_2'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.STR += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.DEF += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.MAG += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.RES += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.SPD += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.SKL += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.LUCK += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    self.inventory.remove(accessories[accessory])
                elif accessory == len(accessories):
                    pass
                else:
                    print("Invalid choice.")
            elif accessory == len(accessories):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            text_speed("You don't have any accessories!", .05)

    def equip_accessory_3(self):
        accessories = self.list_accessories()
        if len(accessories) != 0:
            n = range(int(len(accessories)))
            for i in n:
                print(f'{i}: {accessories[i].name}')
            print(f'{len(accessories)}: Exit')
            accessory = input("Which accessory do you want to equip? ")
            if accessory.isdigit():
                accessory = int(accessory)
                if accessory < len(accessories):
                    if self.equipped['accessory_3'] != items.empty():
                        self.unequip_accessory_3()
                    self.equipped['accessory_3'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.STR += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.DEF += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.MAG += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.RES += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.SPD += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.SKL += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.LUCK += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    self.inventory.remove(accessories[accessory])
                elif accessory == len(accessories):
                    pass
                else:
                    print("Invalid choice.")
            elif accessory == len(accessories):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            text_speed("You don't have any accessories!", .05)

    def equip_accessory_4(self):
        accessories = self.list_accessories()
        if len(accessories) != 0:
            n = range(int(len(accessories)))
            for i in n:
                print(f'{i}: {accessories[i].name}')
            print(f'{len(accessories)}: Exit')
            accessory = input("Which accessory do you want to equip? ")
            if accessory.isdigit():
                accessory = int(accessory)
                if accessory < len(accessories):
                    if self.equipped['accessory_4'] != items.empty():
                        self.unequip_accessory_4()
                    self.equipped['accessory_4'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.STR += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.DEF += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.MAG += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.RES += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.SPD += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.SKL += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.LUCK += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    self.inventory.remove(accessories[accessory])
                elif accessory == len(accessories):
                    pass
                else:
                    print("Invalid choice.")
            elif accessory == len(accessories):
                pass
            else:
                text_speed("Invalid choice.", .05)
        else:
            text_speed("You don't have any accessories!", .05)

    def unequip_accessory_slots(self):
        print("Accessory 1: {}  Accessory 2: {}  Accessory 3: {}  Accessory 4: {}\n".format(self.equipped['accessory_1'].name, self.equipped['accessory_2'].name, self.equipped['accessory_3'].name, self.equipped['accessory_4'].name))
        text_speed("Which accessory slot do you want to unequip?\n", .05)
        text_speed("1. Accessory 1\n", .05)
        text_speed("2. Accessory 2\n", .05)
        text_speed("3. Accessory 3\n", .05)
        text_speed("4. Accessory 4\n", .05)
        text_speed("5. Exit\n", .05)
        choice = input()
        if choice == "1":
            self.unequip_accessory_1()
        elif choice == "2":
            self.unequip_accessory_2()
        elif choice == "3":
            self.unequip_accessory_3()
        elif choice == "4":
            self.unequip_accessory_4()
        elif choice == "5":
            pass

    def unequip_accessory_1(self):
        if self.equipped['accessory_1'] != items.empty():
            self.inventory.append(self.equipped['accessory_1'])
            if self.equipped['accessory_1'].stat == "STR":
                self.STR -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "DEF":
                self.DEF -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "MAG":
                self.MAG -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "RES":
                self.RES -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SPD":
                self.SPD -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SKL":
                self.SKL -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "LUCK":
                self.LUCK -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            self.equipped['accessory_1'] = None
            text_speed("You unequipped your accessory!\n", .05)
        else:
            text_speed("You don't have an accessory equipped!\n", .05)

    def unequip_accessory_2(self):
        if self.equipped['accessory_2'] != None:
            self.inventory.append(self.equipped['accessory_2'])
            if self.equipped['accessory_1'].stat == "STR":
                self.STR -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "DEF":
                self.DEF -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "MAG":
                self.MAG -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "RES":
                self.RES -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SPD":
                self.SPD -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SKL":
                self.SKL -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "LUCK":
                self.LUCK -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            self.equipped['accessory_2'] = None
            text_speed("You unequipped your accessory!\n", .05)
        else:
            text_speed("You don't have an accessory equipped!\n", .05)

    def unequip_accessory_3(self):
        if self.equipped['accessory_3'] != None:
            self.inventory.append(self.equipped['accessory_3'])
            if self.equipped['accessory_1'].stat == "STR":
                self.STR -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "DEF":
                self.DEF -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "MAG":
                self.MAG -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "RES":
                self.RES -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SPD":
                self.SPD -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SKL":
                self.SKL -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "LUCK":
                self.LUCK -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            self.equipped['accessory_3'] = None
            text_speed("You unequipped your accessory!\n", .05)
        else:
            text_speed("You don't have an accessory equipped!\n", .05)

    def unequip_accessory_4(self):
        if self.equipped['accessory_4'] != None:
            self.inventory.append(self.equipped['accessory_4'])
            if self.equipped['accessory_1'].stat == "STR":
                self.STR -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "DEF":
                self.DEF -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "MAG":
                self.MAG -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "RES":
                self.RES -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SPD":
                self.SPD -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SKL":
                self.SKL -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "LUCK":
                self.LUCK -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            self.equipped['accessory_4'] = None
            text_speed("You unequipped your accessory!\n", .05)
        else:
            text_speed("You don't have an accessory equipped!\n", .05)
    
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
        if room.flooded == True and self.status['water_breathing'] == False:
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

    def save_and_exit(self):
        pickle.dump(self, open( "saved_self.p", "wb" ))
        pickle.dump(world._world, open( "saved_world.p", "wb" ))
        print("Game saved!")
        time.sleep(.5)
        exit()
    
    def apply_poison(self):
        if self.status['poison'] == True:
            damage = random.randint(1, 5)
            self.cHP -= damage
            text_speed("You took {} damage from poison!\n".format(damage), .03)
            time.sleep(.2)
            if self.is_alive() == False:
                text_speed("You died.\n", .05)
                time.sleep(1)
                print("Game over.\n")
                time.sleep(1)
                sys.exit()

    def roll_paralyze(self):
        if self.status['paralysis'] == True:
            text_speed("You are paralyzed!\n", .03)
            time.sleep(.2)
            roll = random.randint(1, 10)
            if roll == 1 or 2 or 3:
                return True
            else:
                return False
        else:
            return False
        
    def roll_confusion(self):
        if self.status['confusion'] == True:
            text_speed("You are confused!\n", .03)
            time.sleep(.2)
            roll = random.randint(1, 10)
            if roll == 1 or 2:
                return True
            else:
                return False
        else:
            return False

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
        return self.equipped['armor'].armor + self.equipped['shield'].armor

    def chk_SPD(self, enemy):
        return self.SPD >= enemy.SPD

    def pfight(self, enemy):
        text_speed("You attack!\n", .03)
        time.sleep(.3)
        weapon = self.equipped['weapon']
        if self.roll_paralyze() == True:
            text_speed("You are paralyzed and cannot move!\n", .03)
            time.sleep(.3)
            self.apply_poison()
        elif self.roll_paralyze() == False:
            if self.roll_confusion() == True:
                text_speed("You trip over your own feet!\n", .03)
                time.sleep(.3)
                self.cHP -= 1
                self.apply_poison()
            elif self.roll_confusion() == False:
                if calculate_hit(self, enemy):
                    cCRIT = chk_CRIT(self)
                    text_speed("You use {}!\n".format(weapon.name), .03)
                    time.sleep(.2)
                    pdamage = self.generate_damage(self.STR, weapon, enemy)
                    if cCRIT == True:
                        pdamage *= 2
                        text_speed("Critical hit!\n", .01)
                        time.sleep(.3)
                    text_speed("You dealt {} damage to the {}.\n".format(pdamage, enemy.name), .03)
                    enemy.hp -= (pdamage - enemy.DEF)
                    time.sleep(.3)
                    self.apply_poison()
                else:
                    text_speed("You use {}!\n".format(weapon.name), .03)
                    time.sleep(.2)
                    text_speed("You missed!\n", .03)
                    time.sleep(.3)
                    self.apply_poison()

    def chk_edamage(self, enemy):
        edamage = None
        armor = self.chk_armor()
        pdef = (self.DEF + armor)
        cCRIT = chk_CRIT(enemy)
        if cCRIT == True:
            text_speed("The {} scores a Critical Hit!\n".format(enemy.name), .01)
            time.sleep(.2)
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
            time.sleep(.2)
            if calculate_hit(enemy, self):
                edamage = self.chk_edamage(enemy)
                self.cHP -= edamage
                text_speed("The {} dealt {} damage to you.\n".format(enemy.name, edamage), .03)
                time.sleep(.2)
                if self.is_alive() == True:
                    if enemy.roll_status():
                        if enemy.statusatk in self.status:
                            text_speed("The {} inflicts {} on you!\n".format(enemy.name, enemy.statusatk), .03)
                            time.sleep(.2)
                            self.status[enemy.statusatk] = True
                    text_speed("You have {} HP remaining.\n".format(self.cHP), .03)
                    time.sleep(.2)
                    enemy.apply_poison()
            else:
                text_speed("The {} missed!\n".format(enemy.name), .03)
                time.sleep(.2)
                enemy.apply_poison()
    
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
            print(f'{i}: {spell[i].name} Cost: {spell[i].cost}MP')

    def cast_spell(self, enemy):
        self.list_spells()
        text_speed("Which spell do you want to cast? ", .05)
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(self.chk_spells()):
                if self.cMP >= self.chk_spells()[choice].cost:
                    return self.chk_spells()[choice]
                else:
                    text_speed("You don't have enough MP!\n", .05)
                    time.sleep(.5)
                    self.combat(enemy)

    def pmagatk(self, enemy, spell):
        spell.cast_spell(self, enemy)

    def chk_skills(self):
        skill = []
        for i in self.skills:
            if isinstance(i, skills.Skill):
                skill.append(i)
        return skill
    
    def list_skills(self):
        skill = self.chk_skills()
        n = range(int(len(skill)))
        for i in n:
            print(f'{i}: {skill[i].name} Cost: {skill[i].cost}MP')

    def use_skill(self, enemy):
        self.list_skills()
        text_speed("Which skill do you want to use? ", .05)
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(self.chk_skills()):
                if self.cMP >= self.chk_skills()[choice].cost:
                    return self.chk_skills()[choice]
                else:
                    text_speed("You don't have enough MP!\n", .05)
                    time.sleep(.2)
                    self.combat(enemy)
            
    def pskillatk(self, enemy, skill):
        skill.use_ability(self, enemy)

    def generate_damage(self, stat, attack, enemy):
        adamage = attack.damage
        eweak = chk_weakness(enemy)
        if attack.damage_type == eweak:
            text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
            return random.randrange(stat, stat + (adamage * 2))
        else:
            return random.randrange(stat, stat + adamage)

    def combat(self, enemy):
        # Something odd is happening with damage calculations. It seems that regular, magic, and skill attacks aren't combining in decreasing the enemy's HP.
        text_speed("What will you do?\n", .03)
        time.sleep(.2)
        choice = input("1. Attack\n2. Cast Spell\n3. Use Skill\n")
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
            if self.status['silence'] == True:
                text_speed("You can't cast spells while silenced!\n", .03)
                time.sleep(.2)
                self.combat(enemy)
            chkSPD = self.chk_SPD(enemy)
            spell = self.cast_spell(enemy)
            if chkSPD == True:
                self.pmagatk(enemy, spell)
                if enemy.is_alive() == True:
                    self.efight(enemy)
            else:
                self.efight(enemy)
                if self.is_alive() == True:
                    self.pmagatk(enemy, spell)
        elif choice == "3":
            if self.status['crippled'] == True:
                text_speed("You can't use skills while crippled!\n", .03)
                time.sleep(.2)
                self.combat(enemy)
            elif len(self.skills) == 0:
                text_speed("You don't have any skills!\n", .03)
                time.sleep(.2)
                self.combat(enemy)
            else:
                chkSPD = self.chk_SPD(enemy)
                skill = self.use_skill(enemy)
                if chkSPD == True:
                    self.pskillatk(enemy, skill)
                    if enemy.is_alive() == True:
                        self.efight(enemy)
                else:
                    self.efight(enemy)
                    if self.is_alive() == True:
                        self.pskillatk(enemy, skill)

    def fight(self, enemy):
        # for item in self.inventory:
        #     self.add_statval(item)
        self.combat(enemy)
        if not enemy.is_alive():
            exp = round(enemy.EXP * (((10-self.LVL)+1)/10))
            self.EXP += exp
            self.cash += enemy.gold
            text_speed("You killed the {}!\n".format(enemy.name), .03)
            time.sleep(.5)
            text_speed("You gained {} EXP!\n".format(exp), .03)
            time.sleep(.5)
            self.level_up()
            text_speed("You gained {} gold!\n".format(enemy.gold), .03)
            time.sleep(.5)
            if enemy.drop_part():
                self.materials[enemy.part.name] += 1
                text_speed("You obtained a {}!\n".format(enemy.part.name), .03)
                time.sleep(.5)
            if self.chk_compendium(enemy) == False:
                self.add_monster(enemy)
            # self.monster_part_drop(enemy)
        elif not self.is_alive():
            text_speed("You died.\n", .05)
            time.sleep(1)
            text_speed("Game over.\n", .05)
            time.sleep(1)
            sys.exit()

# Character Classes
class Fighter(Player):
    def __init__(self):
        super().__init__(self, LVL=1, mHP=20, cHP=20, mMP=15, cMP=15, STR=5, DEF=1, MAG=0, RES=0, SPD=2, SKL=4, LUCK=3, cash=10, char_class="Fighter")
        self.equipped['weapon'] = items.rusty_axe()
        self.equipped['shield'] = items.rusty_shield()
        self.skills.append(skills.cleave())
        self.skills.append(skills.heavy_swing())
        self.mHPgrowth = .7
        self.mMPgrowth = .3
        self.STRgrowth = .7
        self.DEFgrowth = .4
        self.MAGgrowth = .2
        self.RESgrowth = .1
        self.SPDgrowth = .3
        self.SKLgrowth = .5
        self.LUCKgrowth = .3

class Mage(Player):
    def __init__(self):
        super().__init__(self, LVL=1, mHP=10, cHP=10, mMP=25, cMP=25, STR=1, DEF=0, MAG=5, RES=3, SPD=3, SKL=2, LUCK=1, cash=10, char_class="Mage")
        self.inventory.append(items.small_blue_potion(3))
        self.spells.append(magic.fire())
        self.spells.append(magic.ice())
        self.spells.append(magic.shock())
        self.mHPgrowth = .2
        self.mMPgrowth = .7
        self.STRgrowth = .1
        self.DEFgrowth = .2
        self.MAGgrowth = .8
        self.RESgrowth = .5
        self.SPDgrowth = .4
        self.SKLgrowth = .3
        self.LUCKgrowth = .3
        self.equipped['weapon'] = items.wooden_staff()
        self.equipped['armor'] = items.cloth_armor()

class Rogue(Player):
    def __init__(self):
        super().__init__(self, LVL=1, mHP=10, cHP=10, mMP=20, cMP=20, STR=2, DEF=1, MAG=1, RES=1, SPD=3, SKL=3, LUCK=4, cash=15, char_class="Rogue")
        self.spells.append(magic.poison())
        self.skills.append(skills.sneak_attack())
        self.skills.append(skills.steal())
        self.mHPgrowth = .3
        self.mMPgrowth = .4
        self.STRgrowth = .4
        self.DEFgrowth = .2
        self.MAGgrowth = .2
        self.RESgrowth = .1
        self.SPDgrowth = .7
        self.SKLgrowth = .7
        self.LUCKgrowth = .5
        self.equipped['weapon'] = items.rusty_dagger()
        self.equipped['accessory_1'] = items.luck_1_ring()

class Cleric(Player):
    def __init__(self):
        super().__init__(self, LVL=1, mHP=15, cHP=15, mMP=20, cMP=20, STR=3, DEF=2, MAG=3, RES=3, SPD=1, SKL=1, LUCK=2, cash=10, char_class="Cleric")
        self.inventory.append(items.small_red_potion(3))
        self.spells.append(magic.smite())
        self.spells.append(magic.turn())
        self.mHPgrowth = .5
        self.mMPgrowth = .5
        self.STRgrowth = .3
        self.DEFgrowth = .2
        self.MAGgrowth = .4
        self.RESgrowth = .7
        self.SPDgrowth = .2
        self.SKLgrowth = .3
        self.LUCKgrowth = .4
        self.equipped['weapon'] = items.rusty_hammer()
        self.equipped['armor'] = items.cloth_armor()

class Paladin(Player):
    def __init__(self):
        super().__init__(self, LVL=1, mHP=20, cHP=20, mMP=20, cMP=20, STR=3, DEF=4, MAG=1, RES=2, SPD=1, SKL=2, LUCK=2, cash=5, char_class="Paladin")
        self.spells.append(magic.smite())
        self.skills.append(skills.heavy_swing())
        self.skills.append(skills.retribution())
        self.mHPgrowth = .5
        self.mMPgrowth = .4
        self.STRgrowth = .6
        self.DEFgrowth = .6
        self.MAGgrowth = .2
        self.RESgrowth = .3
        self.SPDgrowth = .1
        self.SKLgrowth = .5
        self.LUCKgrowth = .3
        self.equipped['weapon'] = items.rusty_sword()
        self.equipped['armor'] = items.rusty_armor()

class Ranger(Player):
    def __init__(self):
        super().__init__(self, LVL=1, mHP=15, cHP=15, mMP=15, cMP=15, STR=2, DEF=1, MAG=1, RES=1, SPD=5, SKL=4, LUCK=1, cash=15, char_class="Ranger")
        self.spells.append(magic.wind())
        self.skills.append(skills.precision_strike())
        self.skills.append(skills.double_strike())
        self.mHPgrowth = .4
        self.mMPgrowth = .4
        self.STRgrowth = .6
        self.DEFgrowth = .3
        self.MAGgrowth = .2
        self.RESgrowth = .1
        self.SPDgrowth = .6
        self.SKLgrowth = .5
        self.LUCKgrowth = .4
        self.equipped['weapon'] = items.wooden_bow()
        self.equipped['accessory_1'] = items.speed_1_ring()