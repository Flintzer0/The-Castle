import items, world, combat
import pickle, sys, time

def text_speed(text):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(.05)

class Player():
    def __init__(self, name, mHP, cHP, STR, DEF, MAG, RES, SPD, SKL, LUCK, cash):
        self.mHP = mHP
        self.cHP = cHP
        self.name = name
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
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.HP, self.name, self.inventory, self.STR, self.DEF, self.MAG, self.RES, self.SPD, self.SKL, self.LUCK)
 
    def is_alive(self):
        return self.cHP > 0
 
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
        self.move(dx=0, dy=-1)
    
    def move_south(self):
        self.move(dx=0, dy=1)
    
    def move_east(self):
        self.move(dx=1, dy=0)
    
    def move_west(self):
        self.move(dx=-1, dy=0)

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
                print("Invalid choice.")
        else:
            print("You haven't encountered any monsters yet!")

    def search(self):
        room = world.tile_exists(self.location_x, self.location_y)
        item = room.item
        if item is not None:
            print(room.search_text())
            if isinstance(item, items.gold):
                self.cash += item.amt
                text_speed("You found {} {}!\n".format(item.amt, item.name))
                time.sleep(1)
                text_speed("You now have {} gold!\n".format(self.cash))
            elif isinstance(item, items.Potion):
                self.inventory.append(item)
                text_speed("You found {} {}(s)!\n".format(item.qty, item.name))
            else:
                self.inventory.append(item)
                text_speed("You found a {}!\n".format(item.name))
            room.item = None
        else:
            return room.searched_text()
        
    def fight(self, enemy):
        if self.check_SPD(self, enemy) == True:
            combat.pfight(self, enemy)
            if enemy.is_alive() == True:
                combat.efight(enemy, self)
        else:
            combat.efight(enemy, self)
            if self.is_alive() == True:
                combat.pfight(self, enemy)
    
    def unlock(self, unlock):
        print(world.tile_exists(self.location_x, self.location_y).unlock(unlock))

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

    def use_potion(self):
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
                    print("You drink the {}!\n".format(p[potion].name))
                    print("You heal {} HP!\n".format(p[potion].heal))
                    print("Your HP is now {}.".format(self.cHP))
                    p[potion].qty -= 1
                    if p[potion].qty == 0:
                        self.inventory.remove(p[potion])
                    for item in self.inventory:
                        print(item, '\n')
                else:
                    print("Invalid choice.")
            else:
                print("Invalid choice.")
        else:
            print("You don't have any potions!")
    
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