import world, items, magic, skills, pickle, sys, time, random, enemy_ai
from utilities import *

class Player():
    starting_turns = 0
    turns = 1
    pchoice = None

    def __init__(self, name, mHP, cHP, mMP, cMP, STR, DEF, MAG, RES, SPD, SKL, LUCK, cash, char_class):
        self.name = name
        self.LVL = 1
        self.EXP = 0
        self.stats = {
            'mHP' : {'value' : mHP},
            'cHP' : {'value' : cHP},
            'mMP' : {'value' : mMP},
            'cMP' : {'value' : cMP},
            'STR' : {'value' : STR},
            'DEF' : {'value' : DEF},
            'MAG' : {'value' : MAG},
            'RES' : {'value' : RES},
            'SPD' : {'value' : SPD},
            'SKL' : {'value' : SKL},
            'LUCK' : {'value' : LUCK}
        }
        self.char_class = char_class
        self.cash = cash
        self.char_class = char_class
        self.location_x, self.location_y = world.starting_position
        self.victory = False
        self.growthmHP = .6
        self.growthmMP = .5
        self.growthSTR = .5
        self.growthDEF = .4
        self.growthMAG = .3
        self.growthRES = .2
        self.growthSPD = .4
        self.growthSKL = .4
        self.growthLUCK = .3
        self.spcl = []
        self.inventory = []
        self.compendium = []
        self.spells = []
        self.skills = []
        self.equipped = {
            'weapon' : items.Fists(),
            'armor' : items.unarmored(),
            'shield' : items.open_hand(),
            'accessory_1' : items.empty(),
            'accessory_2' : items.empty(),
            'accessory_3' : items.empty(),
            'accessory_4' : items.empty(),
        }
        self.statbonus = {
            'STR' : {'value' : 0},
            'DEF' : {'value' : 0},
            'MAG' : {'value' : 0},
            'RES' : {'value' : 0},
            'SPD' : {'value' : 0},
            'SKL' : {'value' : 0},
            'LUCK' : {'value' : 0}
        }
        self.status = {
            'poisoned': {'flag' : False, 'potency' : 0, 'duration' : 0},
            'paralyzed': {'flag' : False, 'potency' : 0, 'duration' : 0},
            'blinded': {'flag' : False, 'duration' : 0},
            'silenced': {'flag' : False, 'duration' : 0},
            'asleep': {'flag' : False, 'duration' : 0},
            'confused': {'flag' : False, 'duration' : 0},
            'charmed': {'flag' : False, 'potency' : 0, 'duration' : 0},
            'crippled': {'flag' : False, 'duration' : 0},
            'slowed': {'flag' : False, 'potency' : 0, 'duration' : 0}
        }
        self.buffs = {
            'water_breathing' : {'flag' : False},
            'regen' : {'flag' : False, 'potency' : 0},
            'heightened_senses' : {'flag' : False, 'potency' : 0},
            'hexbreak' : {'flag' : False, 'potency' : 0},
            'physical_resist' : {'flag' : False, 'potency' : 0},
            'magical_resist' : {'flag' : False, 'potency' : 0},
            'fire_resist' : {'flag' : False, 'potency' : 0},
            'cold_resist' : {'flag' : False, 'potency' : 0},
            'lightning_resist' : {'flag' : False, 'potency' : 0},
            'water_resist' : {'flag' : False, 'potency' : 0},
            'earth_resist' : {'flag' : False, 'potency' : 0},
            'wind_resist' : {'flag' : False, 'potency' : 0},
            'holy_resist' : {'flag' : False, 'potency' : 0},
            'demonic_resist' : {'flag' : False, 'potency' : 0},
            'poison_resist' : {'flag' : False, 'potency' : 0},
            'paralyzed_resist' : {'flag' : False, 'potency' : 0},
            'blind_resist' : {'flag' : False, 'potency' : 0},
            'silence_resist' : {'flag' : False, 'potency' : 0},
            'sleep_resist' : {'flag' : False, 'potency' : 0},
            'confusion_resist' : {'flag' : False, 'potency' : 0},
            'charm_resist' : {'flag' : False, 'potency' : 0},
            'crippled_resist' : {'flag' : False, 'potency' : 0},
            'mana_rage' : {'flag' : False, 'potency' : 0},
            'fortune' : {'flag' : False},
            }
        self.materials = {
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
        self.tempboosts = {
            'STR' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'DEF' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'MAG' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'RES' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'SPD' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'SKL' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'LUCK' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'AVO' : {'flag' : False, 'duration' : 0, 'value' : 0},
            'invisible' : {'flag' : False, 'duration' : 0},
            'heightened_senses' : {'flag' : False, 'duration' : 0},
            'regen' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'hexbreak' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'physical_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'magical_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'fire_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'cold_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'lightning_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'water_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'earth_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'wind_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'holy_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'demonic_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'poison_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'paralyzed_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'blind_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'silence_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'sleep_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'confusion_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'charm_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'crippled_resist' : {'flag' : False, 'duration' : 0, 'potency' : 0},
            'mana_rage' : {'flag' : False, 'duration' : 0}
            }
        self.save_data = {}
    
    def AVO(self):
        return round((self.stats['SPD']['value'] + self.stats['SKL']['value']) * (random.randint(self.stats['LUCK']['value'], 100) / 100))
    
    def __str__(self):
        return "\n{}    Class: {}\n======================\nLevel: {}    EXP: {}\nHP: {}/{} MP: {}/{}\nSTR: {}    DEF: {}\nMAG: {}    RES: {}\nSPD: {}    SKL: {}\nLUCK: {}\n".format(
            self.name,
            self.char_class,
            self.LVL,
            self.EXP,
            self.stats['cHP']['value'],
            self.stats['mHP']['value'],
            self.stats['cMP']['value'],
            self.stats['mMP']['value'],
            (self.stats['STR']['value'] + self.statbonus['STR']['value']),
            (self.stats['DEF']['value'] + self.statbonus['DEF']['value']),
            (self.stats['MAG']['value'] + self.statbonus['MAG']['value']),
            (self.stats['RES']['value'] + self.statbonus['RES']['value']),
            (self.stats['SPD']['value'] + self.statbonus['SPD']['value']),
            (self.stats['SKL']['value'] + self.statbonus['SKL']['value']),
            (self.stats['LUCK']['value'] + self.statbonus['LUCK']['value'])
            )
    
    def __repr__(self):
        return self.name
 
    def is_alive(self):
        return self.stats['cHP']['value'] > 0
    
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def chk_stat_roll(self, growth):
        growth1 = random.randint(1,100) <= (growth * 100)
        growth2 = random.randint(1,100) <= (growth * 100)
        if growth1 or growth2:
            return True
        
    def view_character(self):
        return self.__str__()

    def level_up(self):
        self.LVL += 1
        # print("You are now level {}!".format(self.LVL))
        # time.sleep(.5)
        self.EXP -= 100
        # print('You fully recover your HP!')
        # time.sleep(.5)
        if self.chk_stat_roll(self.growthmHP):
            if isinstance(self, Mage):
                print
                self.stats['mHP']['value'] += 3 + (random.randint(2, 3))
            else:
                self.stats['mHP']['value'] += 5 + (random.randint(2, 5))
        else:
            if isinstance(self, Mage):
                self.stats['mHP']['value'] += random.randint(1, 2)
            else:
                self.stats['mHP']['value'] += random.randint(2, 4)
        # print("Your max HP is now {}!".format(self.stats['mHP']['value']))
        # time.sleep(.5)
        self.stats['cHP']['value'] = self.stats['mHP']['value']
        # print('You fully recover your MP!')
        if self.chk_stat_roll(self.growthmMP):
            if isinstance(self, Mage):
                self.stats['mMP']['value'] += 5 + (random.randint(2, 5))
            else:
                self.stats['mMP']['value'] += 3 + (random.randint(2, 3))
        else:
            if isinstance(self, Mage):
                self.stats['mMP']['value'] += random.randint(2, 4)
            else:
                self.stats['mMP']['value'] += random.randint(1, 2) 
        # print("Your max MP is now {}!".format(self.stats['mMP']['value']))
        # time.sleep(.5)
        self.stats['cMP']['value'] = self.stats['mMP']['value']
        if self.chk_stat_roll(self.growthSTR):
            if self.growthSTR >= .5:
                self.stats['STR']['value'] += random.randint(2, 3)
            else:
                self.stats['STR']['value'] += 1
            # print("Your STR is now {}!".format(self.stats['STR']['value']))
            # time.sleep(.5)
        if self.chk_stat_roll(self.growthDEF):
            if self.growthDEF >= .5:
                self.stats['DEF']['value'] += random.randint(2, 3)
            else:
                self.stats['DEF']['value'] += 1
            # print("Your DEF is now {}!".format(self.stats['DEF']['value']))
            # time.sleep(.5)
        if self.chk_stat_roll(self.growthMAG):
            if self.growthMAG >= .5:
                self.stats['MAG']['value'] += random.randint(2, 3)
            else:
                self.stats['MAG']['value'] += 1
            # print("Your MAG is now {}!".format(self.stats['MAG']['value']))
            # time.sleep(.5)
        if self.chk_stat_roll(self.growthRES):
            if self.growthRES >= .5:
                self.stats['RES']['value'] += random.randint(2, 3)
            else:
                self.stats['RES']['value'] += 1
            # print("Your RES is now {}!".format(self.stats['RES']['value']))
            # time.sleep(.5)
        if self.chk_stat_roll(self.growthSPD):
            if self.growthSPD >= .5:
                self.stats['SPD']['value'] += random.randint(2, 3)
            else:
                self.stats['SPD']['value'] += 1
            # print("Your SPD is now {}!".format(self.stats['SPD']['value']))
            # time.sleep(.5)
        if self.chk_stat_roll(self.growthSKL):
            if self.growthSKL >= .5:
                self.stats['SKL']['value'] += random.randint(2, 3)
            else:
                self.stats['SKL']['value'] += 1
            # print("Your SKL is now {}!".format(self.stats['SKL']['value']))
            # time.sleep(.5)
        if self.chk_stat_roll(self.growthLUCK):
            if self.growthLUCK >= .5:
                self.stats['LUCK']['value'] += random.randint(2, 3)
            else:
                self.stats['LUCK']['value'] += 1
            # print("Your LUCK is now {}!".format(self.stats['LUCK']['value']))
            # time.sleep(.5)

    def menu(self):
        print("1. View Character  2. View Inventory  3. View Compendium  4. View Spells  5. View Skills  6. Equipment  7. Exit\n")
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
            self.equips()
        elif choice == "7":
            self.unequip()
        elif choice == "8":
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

    def equips(self):
        print("1. View Equipped  2. Equip  3. Unequip  4. Exit")
        text_speed("What would you like to do?\n", .05)
        choice = input()
        if choice == "1":
            self.view_equipped()
        elif choice == "2":
            self.equip()
        elif choice == "3":
            self.unequip()
        elif choice == "4":
            pass

    def view_equipped(self):
        print("\nWeapon: {}  Shield: {}  Armor: {}".format(self.equipped['weapon'].name, self.equipped['shield'].name, self.equipped['armor'].name))
        print("Accessory 1: {}  Accessory 2: {}  Accessory 3: {}  Accessory 4: {}\n".format(self.equipped['accessory_1'].name, self.equipped['accessory_2'].name, self.equipped['accessory_3'].name, self.equipped['accessory_4'].name))
        text_speed("What would you like to do?\n", .05)
        print("1. View Weapon  2. View Shield  3. View Armor  4. View Accessories  5. Exit")
        choice = input()
        if choice == "1":
            print(self.equipped['weapon'].__str__())
        elif choice == "2":
            print(self.equipped['shield'].__str__())
        elif choice == "3":
            print(self.equipped['armor'].__str__())
        elif choice == "4":
            self.view_accessories()
        elif choice == "5":
            pass

    def view_accessories(self):
        print("Accessory 1: {}  Accessory 2: {}  Accessory 3: {}  Accessory 4: {}".format(self.equipped['accessory_1'].name, self.equipped['accessory_2'].name, self.equipped['accessory_3'].name, self.equipped['accessory_4'].name))
        text_speed("What would you like to do?\n", .05)
        print("1. View Accessory 1  2. View Accessory 2  3. View Accessory 3  4. View Accessory 4  5. Exit")
        choice = input()
        if choice == "1":
            print(self.equipped['accessory_1'].__str__())
        elif choice == "2":
            print(self.equipped['accessory_2'].__str__())
        elif choice == "3":
            print(self.equipped['accessory_3'].__str__())
        elif choice == "4":
            print(self.equipped['accessory_4'].__str__())
        elif choice == "5":
            pass

    def equip(self):
        text_speed("What would you like to equip?", .05)
        print("1. Weapon\n2. Shield\n3. Armor\n4. Accessories\n5. Exit\n")
        choice = input()
        if choice == "1":
            self.equip_weapon()
        elif choice == "2":
            self.equip_shield()
        elif choice == "3":
            self.equip_armor()
        elif choice == "4":
            self.equip_accessory_slots()
        elif choice == "5":
            pass

    def unequip(self):
        text_speed("What would you like to unequip?\n", .05)
        print("1. Weapon\n2. Shield\n3. Armor\n4. Accessories\n5. Exit\n")
        choice = input()
        if choice == "1":
            self.unequip_weapon()
        elif choice == "2":
            self.unequip_shield()
        elif choice == "3":
            self.unequip_armor()
        elif choice == "4":
            self.unequip_accessory_slots()
        elif choice == "5":
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
                    if isinstance(armor[armor], items.Magic_Armor):
                        if armor[armor].property in self.buffs:
                            self.buffs[armor[armor].property]['flag'] = True
                            self.buffs[armor[armor].property]['potency'] = armor[armor].propercent
                        if armor[armor].resistance in self.buffs:
                            self.buffs[armor[armor].resistance]['flag'] = True
                            self.buffs[armor[armor].resistance]['potency'] = armor[armor].resamt
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
                    if isinstance(shields[shield], items.Spellshield):
                        if shields[shield].property in self.buffs:
                            self.buffs[shield[shield].property]['flag'] = True
                            self.buffs[shield[shield].property]['potency'] = shields[shield].propercent
                        if shields[shield].resistance:
                            self.buffs[shields[shield].resistance]['flag'] = True
                            self.buffs[shields[shield].resistance]['potency'] = shields[shield].resamt
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
            if isinstance(self.equipped['shield'], items.Spellshield):
                if self.equipped['shield'].property in self.buffs:
                    self.buffs[self.equipped['shield'].property]['flag'] = False
                    self.buffs[self.equipped['shield'].property]['potency'] = 0
                if self.equipped['shield'].resistance:
                    self.buffs[self.equipped['shield'].resistance]['flag'] = False
                    self.buffs[self.equipped['shield'].resistance]['potency'] = 0
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
                    if self.equipped['accessory_1'].name != "Empty":
                        self.unequip_accessory_1()
                    self.equipped['accessory_1'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.stats['STR']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.stats['DEF']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.stats['MAG']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.stats['RES']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.stats['SPD']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.stats['SKL']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.stats['LUCK']['value'] += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    else:
                        pass
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
                    if self.equipped['accessory_2'].name != "Empty":
                        self.unequip_accessory_2()
                    self.equipped['accessory_2'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.stats['STR']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.stats['DEF']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.stats['MAG']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.stats['RES']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.stats['SPD']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.stats['SKL']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.stats['LUCK']['value'] += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    else:
                        pass
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
                    if self.equipped['accessory_3'].name != "Empty":
                        self.unequip_accessory_3()
                    self.equipped['accessory_3'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.stats['STR']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.stats['DEF']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.stats['MAG']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.stats['RES']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.stats['SPD']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.stats['SKL']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.stats['LUCK']['value'] += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    else:
                        pass
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
                    if self.equipped['accessory_4'].name != "Empty":
                        self.unequip_accessory_4()
                    self.equipped['accessory_4'] = accessories[accessory]
                    text_speed("You equipped the {}!\n".format(accessories[accessory].name), .05)
                    if accessories[accessory].stat == "STR":
                        self.stats['STR']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "DEF":
                        self.stats['DEF']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "MAG":
                        self.stats['MAG']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "RES":
                        self.stats['RES']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SPD":
                        self.stats['SPD']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "SKL":
                        self.stats['SKL']['value'] += accessories[accessory].statval
                    elif accessories[accessory].stat == "LUCK":
                        self.stats['LUCK']['value'] += accessories[accessory].statval
                    elif accessories[accessory].spcl == "water_breathing":
                        self.status['water_breathing'] = True
                    else:
                        pass
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
        if self.equipped['accessory_1'].name != "Empty":
            self.inventory.append(self.equipped['accessory_1'])
            if self.equipped['accessory_1'].stat == "STR":
                self.stats['STR']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "DEF":
                self.stats['DEF']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "MAG":
                self.stats['MAG']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "RES":
                self.stats['RES']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SPD":
                self.stats['SPD']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "SKL":
                self.stats['SKL']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].stat == "LUCK":
                self.stats['LUCK']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_1'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            else:
                pass
            text_speed("You unequipped the {}!\n".format(self.equipped['accessory_1'].name), .05)
            self.equipped['accessory_1'] = items.empty()
        else:
            text_speed("You don't have an accessory equipped!\n", .05)

    def unequip_accessory_2(self):
        if self.equipped['accessory_2'].name != "Empty":
            self.inventory.append(self.equipped['accessory_2'])
            if self.equipped['accessory_2'].stat == "STR":
                self.stats['STR']['value'] -= self.equipped['accessory_2'].statval
            elif self.equipped['accessory_2'].stat == "DEF":
                self.stats['DEF']['value'] -= self.equipped['accessory_2'].statval
            elif self.equipped['accessory_2'].stat == "MAG":
                self.stats['MAG']['value'] -= self.equipped['accessory_2'].statval
            elif self.equipped['accessory_2'].stat == "RES":
                self.stats['RES']['value'] -= self.equipped['accessory_2'].statval
            elif self.equipped['accessory_2'].stat == "SPD":
                self.stats['SPD']['value'] -= self.equipped['accessory_2'].statval
            elif self.equipped['accessory_2'].stat == "SKL":
                self.stats['SKL']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_2'].stat == "LUCK":
                self.stats['LUCK']['value'] -= self.equipped['accessory_2'].statval
            elif self.equipped['accessory_2'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            else:
                pass
            text_speed("You unequipped the {}!\n".format(self.equipped['accessory 2'].name), .05)
            self.equipped['accessory_2'] = items.empty()
        else:
            text_speed("You don't have an accessory equipped!\n", .05)

    def unequip_accessory_3(self):
        if self.equipped['accessory_3'].name != "Empty":
            self.inventory.append(self.equipped['accessory_3'])
            if self.equipped['accessory_3'].stat == "STR":
                self.stats['STR']['value'] -= self.equipped['accessory_3'].statval
            elif self.equipped['accessory_3'].stat == "DEF":
                self.stats['DEF']['value'] -= self.equipped['accessory_3'].statval
            elif self.equipped['accessory_3'].stat == "MAG":
                self.stats['MAG']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_3'].stat == "RES":
                self.stats['RES']['value'] -= self.equipped['accessory_3'].statval
            elif self.equipped['accessory_3'].stat == "SPD":
                self.stats['SPD']['value'] -= self.equipped['accessory_1'].statval
            elif self.equipped['accessory_3'].stat == "SKL":
                self.stats['SKL']['value'] -= self.equipped['accessory_3'].statval
            elif self.equipped['accessory_2'].stat == "LUCK":
                self.stats['LUCK']['value'] -= self.equipped['accessory_3'].statval
            elif self.equipped['accessory_3'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            else:
                pass
            text_speed("You unequipped the {}!\n".format(self.equipped['accessory 3'].name), .05)
            self.equipped['accessory_3'] = items.empty()
        else:
            text_speed("You don't have an accessory equipped!\n", .05)

    def unequip_accessory_4(self):
        if self.equipped['accessory_4'].name != "Empty":
            self.inventory.append(self.equipped['accessory_4'])
            if self.equipped['accessory_4'].stat == "STR":
                self.stats['STR']['value'] -= self.equipped['accessory_4'].statval
            elif self.equipped['accessory_4'].stat == "DEF":
                self.stats['DEF']['value'] -= self.equipped['accessory_4'].statval
            elif self.equipped['accessory_4'].stat == "MAG":
                self.stats['MAG']['value'] -= self.equipped['accessory_4'].statval
            elif self.equipped['accessory_4'].stat == "RES":
                self.stats['RES']['value'] -= self.equipped['accessory_4'].statval
            elif self.equipped['accessory_4'].stat == "SPD":
                self.stats['SPD']['value'] -= self.equipped['accessory_4'].statval
            elif self.equipped['accessory_4'].stat == "SKL":
                self.stats['SKL']['value'] -= self.equipped['accessory_4'].statval
            elif self.equipped['accessory_4'].stat == "LUCK":
                self.stats['LUCK']['value'] -= self.equipped['accessory_4'].statval
            elif self.equipped['accessory_4'].spcl == "water_breathing":
                self.status['water_breathing'] = False
            else:
                pass
            text_speed("You unequipped the {}!\n".format(self.equipped['accessory 4'].name), .05)
            self.equipped['accessory_4'] = items.empty()
        else:
            text_speed("You don't have an accessory equipped!\n", .05)

    def move(self, dx, dy):
        import tiles
        self.location_x += dx
        self.location_y += dy
        # return world.tile_exists(self.location_x, self.location_y).intro_text()
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
        start = world.tile_exists(self.location_x, self.location_y)
        room = world.tile_exists(self.location_x, (self.location_y-1))
        if room.flooded == True and self.status['water_breathing'] == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                start.leave_tile()
                self.move(dx=0, dy=-1)
            else:
                return room.locked_text()
                self.move(dx=0, dy=0)
    
    def move_south(self):
        start = world.tile_exists(self.location_x, self.location_y)
        room = world.tile_exists(self.location_x, (self.location_y+1))
        if room.flooded == True and self.chk_spcl("Water Breathing") == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                start.leave_tile()
                self.move(dx=0, dy=1)
            else:
                return room.locked_text()
                self.move(dx=0, dy=0)
    
    def move_east(self):
        start = world.tile_exists(self.location_x, self.location_y)
        room = world.tile_exists((self.location_x+1), self.location_y)
        if room.flooded == True and self.chk_spcl("Water Breathing") == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                start.leave_tile()
                self.move(dx=1, dy=0)
            else:
                return room.locked_text()
                self.move(dx=0, dy=0)
    
    def move_west(self):
        start = world.tile_exists(self.location_x, self.location_y)
        room = world.tile_exists((self.location_x-1), self.location_y)
        if room.flooded == True and self.chk_spcl("Water Breathing") == False:
            text_speed("The water is too deep to cross!\n", .05)
            self.move(dx=0, dy=0)
        else:
            if room.unlocked == True:
                start.leave_tile()
                self.move(dx=-1, dy=0)
            else:
                return room.locked_text()
                self.move(dx=0, dy=0)

    def buy(self, shopkeep):
        shopkeep.shop_text()
        while True:
            shopkeep.display_shop()
            item = input("Which item would you like to buy? ")
            if item.isdigit():
                item = (int(item) - 1)
                if item < len(shopkeep.inventory):
                    purchase = shopkeep.inventory[item]
                    if isinstance(purchase, items.sold_out):
                        text_speed("This item is sold out!\n", .05)
                        time.sleep(.5)
                    elif self.cash >= purchase.value:
                        self.inventory.append(purchase)
                        self.cash -= purchase.value
                        text_speed("You bought the {}!\n".format(purchase.name), .05)
                        time.sleep(.5)
                        if isinstance(purchase, items.Potion):
                            purchase.qty -= 1
                            if purchase.qty == 0:
                                shopkeep.inventory[item] = items.sold_out()
                        else:
                            shopkeep.inventory[item] = items.sold_out()
                        text_speed("You now have {} gold!\n".format(self.cash), .05)
                        time.sleep(.5)
                    else:
                        text_speed("You don't have enough gold!\n", .05)
                        time.sleep(.5)
                elif item == (len(shopkeep.inventory)):
                    shopkeep.leave_shop()
                    break
                else:
                    print("Invalid choice.")
                    time.sleep(.2)
            else:
                text_speed("Invalid choice.", .05)
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
            room.search_text()
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
                    self.stats['cHP']['value'] -= 20
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
        else:
            return False

    def list_inventory(self, item):
        if self.check_inventory(item) is not False:
            items = self.check_inventory(item)
            n = range(int(len(items)))
            e = (int(len(items)))
            for i in n:
                print(f'{i}: {items[i].name} x{items[i].qty}')
            print(f'{e}: Exit')
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
        if self.starting_turns == 0:
            if self.check_inventory(items.Potion) is not False:
                self.list_inventory(items.Anytime)
                potion = input("Which potion do you want to use? ")
                if potion.isdigit():
                    potion = int(potion)
                    if potion < len(self.check_inventory(items.Anytime)):
                        p = self.check_inventory(items.Anytime)
                        if isinstance(p[potion], items.Recovery):
                            p[potion].heal(self)
                        elif isinstance(p[potion], items.PermBoost):
                            p[potion].boost(self)
                        p[potion].qty -= 1
                        if p[potion].qty == 0:
                            self.inventory.remove(p[potion])
                    elif potion == len(self.check_inventory(items.Anytime)):
                        pass
                    else:
                        print("Invalid choice.")
                        time.sleep(.2)
                else:
                    print("Invalid choice.")
                    time.sleep(.2)
            else:
                print("You don't have any potions!")
                time.sleep(.2)
        elif self.starting_turns > 0:
            self.list_inventory(items.Potion)
            potion = input("Which potion do you want to use? ")
            if potion.isdigit():
                potion = int(potion)
                if potion < len(self.check_inventory(items.Potion)):
                    p = self.check_inventory(items.Potion)
                    if isinstance(p[potion], items.Recovery):
                        p[potion].heal(self)
                    elif isinstance(p[potion], items.PermBoost):
                        p[potion].boost(self)
                    elif isinstance(p[potion], items.BoostPotion):
                        if self.tempboosts[p[potion].stat] != False:
                            p[potion].boost(self)
                        else:
                            self.starting_turns = self.turns
                            p[potion].boost(self)
                    p[potion].qty -= 1
                    if p[potion].qty == 0:
                        self.inventory.remove(p[potion])
                elif potion == len(self.check_inventory(items.Potion)):
                    pass
                else:
                    print("Invalid choice.")
                    time.sleep(.2)
            else:
                print("Invalid choice.")
                time.sleep(.2)
            time.sleep(.2)

    def apply_poison(self):
        if self.status['poisoned']['flag'] == True:
            damage = self.status['poisoned']['potency']
            self.stats['cHP']['value'] -= damage
            text_speed("You took {} damage from poison!\n".format(damage), .03)
            time.sleep(.2)
            if self.is_alive() == False:
                text_speed("You died.\n", .05)
                time.sleep(1)
                print("Game over.\n")
                time.sleep(1)
                sys.exit()

    def roll_paralyze(self):
        if self.status['paralyzed']['flag'] == True:
            if self.status['paralyzed']['duration'] > 0:
                text_speed("You are paralyzed!\n", .03)
                time.sleep(.2)
                roll = random.randint(1, 10)
                if roll == 1 or roll == 2 or roll == 3:
                    return True
                elif roll == 3 or roll == 4 or roll == 5 or roll == 6 or roll == 7 or roll == 8 or roll == 9 or roll == 10:
                    return False
        else:
            return False
        
    def roll_confusion(self):
        if self.status['confused'] == True:
            text_speed("You are confused!\n", .03)
            time.sleep(.2)
            roll = random.randint(1, 10)
            if roll == 1 or roll == 2:
                return True
            elif roll == 10:
                self.status['confused'] = False
                text_speed("You are no longer confused!\n", .03)
                time.sleep(.2)
                return False
            else:
                return False
        else:
            return False

    def chk_armor(self):
        armor = self.equipped['armor'].armor + self.equipped['shield'].armor
        return armor / 100
    
    def chk_marmor(self):
        if self.equipped['armor'].marmor:
            if self.equipped['shield'].marmor:
                marmor = self.equipped['armor'].marmor + self.equipped['shield'].marmor
            else:
                marmor = self.equipped['armor'].marmor
            return marmor / 100
        elif self.equipped['shield'].marmor:
            marmor = self.equipped['shield'].marmor
            return marmor / 100
        else:
            return 0

    def pfight(self, enemy):
        text_speed("You attack!\n", .03)
        time.sleep(.3)
        weapon = self.equipped['weapon']
        paralyzed = self.roll_paralyze()
        if paralyzed == True:
            text_speed("You are paralyzed and cannot move!\n", .03)
            time.sleep(.3)
            self.apply_poison()
        elif paralyzed == False:
            confusion = self.roll_confusion()
            if confusion == True:
                text_speed("You trip over your own feet!\n", .03)
                time.sleep(.2)
                text_speed("You take 1 damage!\n", .03)
                time.sleep(.2)
                self.stats['cHP']['value'] -= 1
                self.apply_poison()
            elif confusion == False:
                if calculate_hit(self, enemy):
                    cCRIT = chk_CRIT(self, enemy)
                    text_speed("You use {}!\n".format(weapon.name), .03)
                    time.sleep(.2)
                    bstat = (self.stats['STR']['value'] + self.statbonus['STR']['value'])
                    pdamage = generate_damage(self, bstat, weapon.damage, enemy)
                    if cCRIT == True:
                        pdamage *= 2
                        text_speed("Critical hit!\n", .01)
                        time.sleep(.3)
                    if (pdamage - enemy.stats['DEF']) < 0:
                        damage = 1
                    else:
                        damage = (pdamage - enemy.stats['DEF'])
                    text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
                    enemy.stats['HP'] -= damage
                    time.sleep(.2)
                    self.apply_poison()
                else:
                    text_speed("You use {}!\n".format(weapon.name), .03)
                    time.sleep(.2)
                    text_speed("You missed!\n", .03)
                    time.sleep(.2)
                    text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.hp), .03)
                    self.apply_poison()

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
        text_speed("Which spell do you want to cast? ", .03)
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(self.chk_spells()):
                if self.stats['cMP']['value'] >= self.chk_spells()[choice].cost:
                    return self.chk_spells()[choice]
                else:
                    text_speed("You don't have enough MP!\n", .03)
                    time.sleep(.2)
                    self.combat(enemy)
            else:
                text_speed("Invalid choice.\n", .03)
                time.sleep(.2)
                self.cast_spell(enemy)
        else:
            text_speed("Invalid choice.\n", .03)
            time.sleep(.2)
            self.cast_spell(enemy)

    def pmagatk(self, enemy, spell):
        paralyzed = self.roll_paralyze()
        confusion = self.roll_confusion()
        if paralyzed == True:
            text_speed("You are paralyzed and cannot move!\n", .03)
            time.sleep(.3)
            self.apply_poison()
        elif paralyzed == False:
            if confusion == True:
                text_speed("You lose your concentration and are damaged by your mana!\n", .03)
                time.sleep(.2)
                self.stats['cHP']['value'] -= 1
                self.apply_poison()
            elif confusion == False:
                spell.cast(self, enemy)

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
        text_speed("Which skill do you want to use? ", .03)
        choice = input()
        if choice.isdigit():
            choice = int(choice)
            if choice < len(self.chk_skills()):
                if self.stats['cMP']['value'] >= self.chk_skills()[choice].cost:
                    return self.chk_skills()[choice]
                else:
                    text_speed("You don't have enough MP!\n", .03)
                    time.sleep(.2)
                    self.combat(enemy)
            
    def pskillatk(self, enemy, skill):
        paralyzed = self.roll_paralyze()
        confusion = self.roll_confusion()
        if paralyzed == True:
            text_speed("You are paralyzed and cannot move!\n", .03)
            time.sleep(.3)
            self.apply_poison()
        elif paralyzed == False:
            if confusion == True:
                text_speed("You trip over your own feet!\n", .03)
                time.sleep(.2)
                self.stats['cHP']['value'] -= 1
                self.apply_poison()
            elif confusion == False:
                skill.use_ability(self, enemy)

    def use_item(self, enemy):
        print("1. Potion\n2. Scrolls\n3. Thrown Items\n4. Boost Items\n5. Back")
        choice = input("What would you like to use? ")
        if choice == "1":
            if self.check_inventory(items.Potion) is not False:
                self.use_potion()
            else:
                text_speed("You don't have any potions!\n", .03)
                time.sleep(.2)
                self.use_item(enemy)
        elif choice == "2":
            if self.check_inventory(items.Scroll) is not False:
                self.use_scroll(enemy)
            else:
                text_speed("You don't have any scrolls!\n", .03)
                time.sleep(.2)
                self.use_item(enemy)
        elif choice == "3":
            if self.check_inventory(items.Thrown) is not False:
                self.use_thrown(enemy)
            else:
                text_speed("You don't have any thrown items!\n", .03)
                time.sleep(.2)
                self.use_item(enemy)
        elif choice == "4":
            self.use_boost()
        elif choice == "5":
            self.combat(enemy)

    def use_scroll(self, enemy):
        if self.check_inventory(items.Scroll) is not False:
            self.list_inventory(items.Scroll)
            scroll = input("Which scroll do you want to use? ")
            if scroll.isdigit():
                scroll = int(scroll)
                if scroll < len(self.check_inventory(items.Scroll)):
                    s = self.check_inventory(items.Scroll)
                    s[scroll].spell.cast(enemy)
                    s[scroll].qty -= 1
                    if s[scroll].qty == 0:
                        self.inventory.remove(s[scroll])
                elif scroll == len(self.check_inventory(items.Scroll)):
                    pass
                else:
                    print("Invalid choice.")
                    time.sleep(.2)
            else:
                print("Invalid choice.")
                time.sleep(.2)

    def use_thrown(self, enemy):
        self.list_inventory(items.Thrown)
        thrown = input("Which thrown item do you want to use? ")
        if thrown.isdigit():
            thrown = int(thrown)
            if thrown < len(self.check_inventory(items.Thrown)):
                t = self.check_inventory(items.Thrown)
                t[thrown].throw(self, enemy)
                t[thrown].qty -= 1
                if t[thrown].qty == 0:
                    self.inventory.remove(t[thrown])
            elif thrown == len(self.check_inventory(items.Thrown)):
                pass
            else:
                print("Invalid choice.")
                time.sleep(.2)
        else:
            print("Invalid choice.")
            time.sleep(.2)

    def chk_equips(self):
        for slot, item in self.equipped.items():
            if item != 'weapon' :
                buff = getattr(item, 'buff', None)
                stat = getattr(item, 'stat', None)
                if buff:
                    buff_info = self.buffs.get(buff)
                    if buff_info:
                        buff_info['flag'] = True
                        if 'potency' in buff_info:
                            buff_info['potency'] += (item.propercent * 100)
                if stat:
                    print(stat)
                    stat_info = self.statbonus.get(stat)
                    if stat_info:
                        print(stat_info, item.statval)
                        stat_info['value'] += item.statval

    def chk_temps(self):
        for f in self.tempboosts:
            if self.tempboosts[f]['flag'] != False:
                if self.tempboosts[f]['duration'] > 0:
                    if self.tempboosts[f] == "STR":
                        self.stats['STR']['value'] = self.stats['STR']['value'] + self.tempboosts[f]
                    elif self.tempboosts[f] == "DEF":
                        self.stats['DEF']['value'] = self.stats['DEF']['value'] + self.tempboosts[f]
                    elif self.tempboosts[f] == "MAG":
                        self.stats['MAG']['value'] = self.stats['MAG']['value'] + self.tempboosts[f]
                    elif self.tempboosts[f] == "RES":
                        self.stats['RES']['value'] = self.stats['RES']['value'] + self.tempboosts[f]
                    elif self.tempboosts[f] == "SPD":
                        self.stats['SPD']['value'] = self.stats['SPD']['value'] + self.tempboosts[f]
                    elif self.tempboosts[f] == "SKL":
                        self.stats['SKL']['value'] = self.stats['SKL']['value'] + self.tempboosts[f]
                    elif self.tempboosts[f] == "LUCK":
                        self.stats['LUCK']['value'] = self.stats['LUCK']['value'] + self.tempboosts[f]
                    self.tempboosts[f]['duration'] -= 1
                else:
                    self.tempboosts[f]['flag'] = False
                    self.tempboosts[f]['duration'] = 0
                    self.tempboosts[f] = 0
                    text_speed("Your temporary boost to {} has worn off!\n".format(f), .03)
                    time.sleep(.2)
            else:
                pass

    def combat(self, enemy):
        eai = enemy_ai.EnemyAI(enemy)
        text_speed("What will you do?\n", .03)
        time.sleep(.2)
        choice = input("1. Attack\n2. Cast Spell\n3. Use Skill\n4. Use Item\n5. Stats\n")
        if choice == "1":
            self.pchoice = "attack"
            chkSPD = chk_SPD(self, enemy)
            if chkSPD == 'player':
                self.pfight(enemy)
                if enemy.is_alive() == True:
                    eai.decide(self)
            elif chkSPD == 'enemy':
                eai.decide(self)
                if self.is_alive() == True:
                    self.pfight(enemy)
        elif choice == "2":
            self.pchoice = "magic"
            if self.status['silenced'] == True:
                text_speed("You can't cast spells while silenced!\n", .03)
                time.sleep(.2)
                self.combat(enemy)
            elif len(self.spells) == 0:
                text_speed("You don't know any spells!\n", .03)
                time.sleep(.2)
                self.combat(enemy)
            else:
                chkSPD = chk_SPD(self, enemy)
                spell = self.cast_spell(enemy)
                if chkSPD == 'player':
                    self.pmagatk(enemy, spell)
                    if enemy.is_alive() == True:
                        eai.decide(self)
                elif chkSPD == 'enemy':
                    eai.decide(self)
                    if self.is_alive() == True:
                        self.pmagatk(enemy, spell)
        elif choice == "3":
            self.pchoice = "skill"
            if self.status['crippled'] == True:
                text_speed("You can't use skills while crippled!\n", .03)
                time.sleep(.2)
                self.combat(enemy)
            elif len(self.skills) == 0:
                text_speed("You don't have any skills!\n", .03)
                time.sleep(.2)
                self.combat(enemy)
            else:
                chkSPD = chk_SPD(self, enemy)
                skill = self.use_skill(enemy)
                if chkSPD == 'player':
                    self.pskillatk(enemy, skill)
                    if enemy.is_alive() == True:
                        eai.decide(self)
                elif chkSPD == 'enemy':
                    eai.decide(self)
                    if self.is_alive() == True:
                        self.pskillatk(enemy, skill)
        elif choice == "4":
            self.pchoice = "item"
            self.use_item(enemy)
            eai.decide(self)
        elif choice == "5":
            print(self.__str__())
            for s in self.status:
                if self.status[s] == True:
                    print(s)
            print("1. Back")
            choice = input("What would you like to do? ")
            if choice == "1":
                self.combat(enemy)
            else:
                text_speed("Invalid choice.\n", .03)
                time.sleep(.2)
                self.combat(enemy)
        else:
            text_speed("Invalid choice.\n", .03)
            time.sleep(.2)
            self.combat(enemy)

    def fight(self, enemy):
        self.starting_turns = 1
        self.chk_equips()
        while self.is_alive() and enemy.is_alive():
            self.chk_temps()
            self.combat(enemy)
            if self.buffs['regen']['flag'] == True:
                self.stats['cHP']['value'] += self.stats['mHP']['value'] * self.buffs['regen']['potency']
            self.turns += 1
            for s in self.status:
                if self.status[s]['flag'] == True:
                    if self.status[s]['duration'] > 0:
                        self.status[s]['duration'] -= 1
                    if self.status[s]['duration'] == 0:
                        self.status[s]['flag'] = False
                        self.status[s]['duration'] = 0
                        text_speed("You are no longer {}!\n".format(s), .03)
                        time.sleep(.2)
            for e in enemy.status:
                if enemy.status[e]['flag'] == True:
                    if enemy.status[e]['duration'] > 0:
                        enemy.status[e]['duration'] -= 1
                    if enemy.status[e]['duration'] == 0:
                        enemy.status[e]['flag'] = False
                        enemy.status[e]['duration'] = 0
                        text_speed("The {} is not longer {}!\n".format(enemy.name, e), .03)
                        time.sleep(.2)
        if not enemy.is_alive():
            self.pchoice = None
            self.starting_turns = 0
            self.turns = 1
            if enemy.tier == "Boss":
                exp = enemy.EXP
            else:
                diff = self.LVL - enemy.tier
                if diff >= 0:
                    exp = round(enemy.EXP * (((100-diff))/100))
                elif diff < 0:
                    diff = enemy.tier * 10
                    exp = round(enemy.EXP * (((100+diff))/100))
            self.EXP += exp
            self.cash += enemy.gold
            text_speed("You killed the {}!\n".format(enemy.name), .03)
            time.sleep(.2)
            text_speed("You gained {} EXP!\n".format(exp), .03)
            time.sleep(.2)
            loop = 1
            while self.EXP >= 100:
                if loop == 1:
                    text_speed("You leveled up!\n", .03)
                    time.sleep(.2)
                    self.level_up()
                    loop += 1
                else:
                    text_speed("You leveled up again!\n", .03)
                    time.sleep(.2)
                    self.level_up()
                    loop += 1
            loop = 1
            text_speed("You gained {} gold!\n".format(enemy.gold), .03)
            time.sleep(.2)
            if enemy.drop_part():
                self.materials[enemy.part.name] += 1
                text_speed("You obtained a {}!\n".format(enemy.part.name), .03)
                time.sleep(.5)
            if self.chk_compendium(enemy) == False:
                self.add_monster(enemy)
        elif not self.is_alive():
            self.turns = 0
            text_speed("You died.\n", .05)
            time.sleep(1)
            text_speed("Game over.\n", .05)
            time.sleep(1)
            sys.exit()

# Character Classes
class Fighter(Player):
    def __init__(self):
        super().__init__(self, mHP=20, cHP=20, mMP=15, cMP=15, STR=5, DEF=1, MAG=0, RES=0, SPD=2, SKL=4, LUCK=3, cash=10, char_class="Fighter")
        self.equipped['weapon'] = items.rusty_axe()
        self.equipped['shield'] = items.rusty_shield()
        self.skills.append(skills.cleave())
        self.skills.append(skills.heavy_swing())
        self.growthmHP = .7
        self.growthmMP = .3
        self.growthSTR = .7
        self.growthDEF = .4
        self.growthMAG = .1
        self.growthRES = .2
        self.growthSPD = .3
        self.growthSKL = .5
        self.growthLUCK = .3

class Mage(Player):
    def __init__(self):
        super().__init__(self, mHP=10, cHP=10, mMP=25, cMP=25, STR=1, DEF=0, MAG=5, RES=3, SPD=3, SKL=2, LUCK=1, cash=10, char_class="Mage")
        self.inventory.append(items.small_blue_potion(3))
        self.spells.append(magic.fire())
        self.spells.append(magic.ice())
        self.spells.append(magic.shock())
        self.growthmHP = .2
        self.growthmMP = .7
        self.growthSTR = .1
        self.growthDEF = .2
        self.growthMAG = .8
        self.growthRES = .5
        self.growthSPD = .4
        self.growthSKL = .3
        self.growthLUCK = .3
        self.equipped['weapon'] = items.wooden_staff()
        self.equipped['armor'] = items.cloth_armor()

class Rogue(Player):
    def __init__(self):
        super().__init__(
            self,
            mHP=10,
            cHP=10,
            mMP=20,
            cMP=20,
            STR=2,
            DEF=1,
            MAG=1,
            RES=1,
            SPD=3,
            SKL=3,
            LUCK=4,
            cash=15,
            char_class="Rogue"
            )
        self.spells.append(magic.poison_dart())
        self.skills.append(skills.sneak_attack())
        self.skills.append(skills.steal())
        self.growthmHP = .3
        self.growthmMP = .4
        self.growthSTR = .4
        self.growthDEF = .2
        self.growthMAG = .3
        self.growthRES = .2
        self.growthSPD = .6
        self.growthSKL = .7
        self.growthLUCK = .4
        self.equipped['weapon'] = items.rusty_dagger()
        self.equipped['accessory_1'] = items.luck_1_ring()

class Cleric(Player):
    def __init__(self):
        super().__init__(self, mHP=15, cHP=15, mMP=20, cMP=20, STR=3, DEF=2, MAG=3, RES=3, SPD=1, SKL=1, LUCK=2, cash=10, char_class="Cleric")
        self.inventory.append(items.small_red_potion(3))
        self.spells.append(magic.smite())
        self.spells.append(magic.turn())
        self.growthmHP = .5
        self.growthmMP = .5
        self.growthSTR = .3
        self.growthDEF = .2
        self.growthMAG = .4
        self.growthRES = .7
        self.growthSPD = .2
        self.growthSKL = .3
        self.growthLUCK = .4
        self.equipped['weapon'] = items.rusty_hammer()
        self.equipped['armor'] = items.cloth_armor()

class Paladin(Player):
    def __init__(self):
        super().__init__(self, mHP=20, cHP=20, mMP=20, cMP=20, STR=3, DEF=4, MAG=1, RES=2, SPD=1, SKL=2, LUCK=2, cash=5, char_class="Paladin")
        self.spells.append(magic.smite())
        self.skills.append(skills.heavy_swing())
        self.skills.append(skills.retribution())
        self.growthmHP = .5
        self.growthmMP = .4
        self.growthSTR = .6
        self.growthDEF = .6
        self.growthMAG = .2
        self.growthRES = .3
        self.growthSPD = .1
        self.growthSKL = .5
        self.growthLUCK = .3
        self.equipped['weapon'] = items.rusty_sword()
        self.equipped['armor'] = items.rusty_armor()

class Ranger(Player):
    def __init__(self):
        super().__init__(self, mHP=15, cHP=15, mMP=15, cMP=15, STR=2, DEF=1, MAG=1, RES=1, SPD=5, SKL=4, LUCK=1, cash=15, char_class="Ranger")
        self.spells.append(magic.wind())
        self.skills.append(skills.precision_strike())
        self.skills.append(skills.double_strike())
        self.growthmHP = .4
        self.growthmMP = .4
        self.growthSTR = .6
        self.growthDEF = .3
        self.growthMAG = .2
        self.growthRES = .1
        self.growthSPD = .6
        self.growthSKL = .5
        self.growthLUCK = .4
        self.equipped['weapon'] = items.wooden_bow()
        self.equipped['accessory_1'] = items.speed_1_ring()

class Debug(Player):
    def __init__(self):
        super().__init__(self, mHP=1000, cHP=1000, mMP=1000, cMP=1000, STR=2, DEF=1000, MAG=1000, RES=1000, SPD=1000, SKL=1000, LUCK=1000, cash=10000, char_class="Debug")
        self.inventory.append(items.elixir(99))
        self.inventory.append(items.STR_1_boost(99))
        self.inventory.append(items.DEF_1_boost(99))
        self.inventory.append(items.minor_strength_boost(99))
        self.inventory.append(items.throwing_knife(99))
        self.inventory.append(items.strength_1_ring())
        self.inventory.append(items.defense_1_ring())
        self.inventory.append(items.magic_1_ring())
        self.inventory.append(items.resistance_1_ring())
        self.inventory.append(items.speed_1_ring())
        self.inventory.append(items.skill_1_ring())
        self.inventory.append(items.luck_1_ring())
        self.skills.append(skills.cleave())
        self.skills.append(skills.heavy_swing())
        self.skills.append(skills.sneak_attack())
        self.skills.append(skills.steal())
        self.skills.append(skills.precision_strike())
        self.skills.append(skills.double_strike())
        self.skills.append(skills.poison_point())
        self.skills.append(skills.guard_breaker())
        self.spells.append(magic.fire())
        self.spells.append(magic.ice())
        self.spells.append(magic.shock())
        self.spells.append(magic.wind())
        self.spells.append(magic.quake())
        self.spells.append(magic.water())
        self.spells.append(magic.smite())
        self.spells.append(magic.turn())
        self.spells.append(magic.poison())
        self.spells.append(magic.curse())
        self.spells.append(magic.wither())
        self.equipped['weapon'] = items.obsidian_blade()
        self.equipped['shield'] = items.iron_curtain()
        self.equipped['armor'] = items.plate()
        self.equipped['accessory_1'] = items.water_ring()
        self.growthmHP = 1
        self.growthmMP = 1
        self.growthSTR = 1
        self.growthDEF = 1
        self.growthMAG = 1
        self.growthRES = 1
        self.growthSPD = 1
        self.growthSKL = 1
        self.growthLUCK = 1

    def move(self, dx, dy):
        import tiles
        self.location_x += dx
        self.location_y += dy
        location = world.tile_exists(self.location_x, self.location_y)
        if isinstance(location, tiles.stairs):
            location.end_demo(self)
