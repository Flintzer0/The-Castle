import enemies

class Item():
    """The base class for all items"""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
# These are all items used for purchasing and trading.
class gold(Item):
    def __init__(self, amt):
        self.amt = amt
        super().__init__(name="Gold",
                         description="A valuable coin used for purchasing.".format(str(self.amt)),
                         value=self.amt)

# These are all items used for damaging enemies.
class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)

# Unarmed/Fist Items
class Fists(Weapon):
    def __init__(self):
        super().__init__(name="Fists",
                         description="Your own fists. Not very effective.",
                         value=0,
                         damage=1) 

# Dagger Items
class rusty_dagger(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Dagger",
                         description="A small dagger with some rust.",
                         value=2,
                         damage=2)
        
class wooden_dagger(Weapon):
    def __init__(self):
        super().__init__(name="Wooden Dagger",
                         description="A small dagger made of wood. It may be wooden, but it's still better than \na rusty blade. It's surprisingly sturdy.",
                         value=3,
                         damage=3)

class iron_dagger(Weapon):
    def __init__(self):
        super().__init__(name="Iron Dagger",
                         description="A small, clean dagger. It glints in the light.",
                         value=10,
                         damage=5)

# Sword Items
class rusty_sword(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Sword",
                         description="A sword covered in rust.",
                         value=3,
                         damage=3)

class wooden_sword(Weapon):
    def __init__(self):
        super().__init__(name="Wooden Sword",
                         description="A wooden sword. It's not very sharp, but it's better than a rusty blade.",
                         value=10,
                         damage=5)

class iron_sword(Weapon):
    def __init__(self):
        super().__init__(name="Iron Sword",
                         description="A clean sword. It glints in the light.",
                         value=25,
                         damage=8)

# Polearm Items
# Axe Items
# Bow Items
# Staff Items
# Tome Items
# Rod Items
# Thrown Items

# These are all items used for defending against enemy attacks.
# Armor Items
class Armor(Item):
    def __init__(self, name, description, value, armor):
        self.armor = armor
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nArmor: {}".format(self.name, self.description, self.value, self.armor)
    
class unarmored(Armor):
    def __init__(self):
        super().__init__(name="Unarmored",
                         description="You're not wearing any armor. You're vulnerable to attacks.",
                         value=0,
                         armor=0)
        
class cloth_armor(Armor):
    def __init__(self):
        super().__init__(name="Cloth Armor",
                         description="A simple cloth armor. Provides minimal protection.",
                         value=5,
                         armor=1)

# Shield Items
class rusty_shield(Armor):
    def __init__(self):
        super().__init__(name="Rusty Shield",
                         description="A bent and rusty shield. Provides minimal protection.",
                         value=3,
                         armor=1)

# These items are all equipment used for increasing stats.
# Accessory Items
# Ring Items
class Ring(Item):
    def __init__(self, name, description, value, stat):
        self.stat = stat
        super().__init__(name, description, value)
    # Strength Rings
class strength_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Strength Ring",
                         description="A ring that increases strength by 1.",
                         value=10,
                         stat=1)
    # Defense Rings
class defense_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Defense Ring",
                         description="A ring that increases defense by 1.",
                         value=10,
                         stat=1)
    # Magic Rings
    # Resistance Rings
    # Speed Rings
    # Skill Rings
    # Luck Rings
# Necklace Items
# Bracelet Items
# Earring Items
# Belt Items
# Headgear Items
# Body Items
# Foot Items
# Hand Items
# Leg Items
# Arm Items

# These items are all consumables, such as keys, potions, etc.
# Keys Items
class Key(Item):
    def __init__(self, name, description, value, unlock):
        self.unlock = unlock
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nUnlock: {}".format(self.name, self.description, self.value, self.unlock)

class wooden_key(Key):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Wooden Key",
                         unlock=1,
                         description="{} simple wooden key(s). Good for one use.".format(str(self.qty)),
                         value=1)

class iron_key(Key):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Iron Key",
                         unlock=2,
                         description="An iron key. Good for" + str(self.unlock) + "uses.".format(str(self.qty)),
                         value=10)

# Potion Items
class Potion(Item):
    def __init__(self, name, description, value, heal):
        self.heal = heal
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nHeal: {}".format(self.name, self.description, self.value, self.heal)
    
class small_red_potion(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Small Red Potion",
                         description="A small red potion. Heals 5 HP. ({})".format(str(self.qty)),
                         value=5,
                         heal=5)

class large_red_potion(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Large Red Potion",
                         description="A large red potion. Heals 10 HP. ({})".format(str(self.qty)),
                         value=10,
                         heal=10)

class elixir(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Elixir",
                         description="A magical elixir. Fully restores HP. ({})".format(str(self.qty)),
                         value=15,
                         heal=999)

class small_blue_potion(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Small Blue Potion",
                         description="A small blue potion. Boosts MAG by 2 for 3 turns. ({})".format(str(self.qty)),
                         value=5,
                         heal=2)
        
# These items are all materials used for item upgrades.
class Material(Item):
    def __init__(self, name, description, value, rarity):
        self.rarity = rarity
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nRarity: {}".format

# Wood Items
class wood_plank(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Wood Plank",
                         description="A simple wood plank. Used for upgrading. ({})".format(str(self.qty)),
                         value=2,
                         rarity=1)

class wood_crossguard(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Wood Crossguard",
                         description="A simple wood crossguard. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1)

# Ore Items
class stone(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Stone",
                         description="A simple stone. Used for upgrading. ({})".format(str(self.qty)),
                         value=1,
                         rarity=1)
        
class iron_ore(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Iron Ore",
                         description="A simple iron ore. Used for upgrading. ({})".format(str(self.qty)),
                         value=10,
                         rarity=1)

# Gem Items
class ruby(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Ruby",
                         description="A simple ruby. Used for upgrading. ({})".format(str(self.qty)),
                         value=200,
                         rarity=5)

# Cloth Items
# Monster Parts
class monster_part(Material):
    def __init__(self, name, description, value, rarity, enemy, drop_rate):
        self.rarity = rarity
        self.enemy = enemy
        self.drop_rate = drop_rate
        super().__init__(name, description, value)

class spider_leg(monster_part):
    def __init__(self, qty):
        self.qty = qty
        enemy = enemies.giant_spider()
        super().__init__(name="Spider Leg",
                         description="A spider's leg. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)

class goblin_ear(monster_part):
    def __init__(self, qty):
        self.qty = qty
        enemy = enemies.goblin()
        super().__init__(name="Goblin Ear",
                         description="A goblin's ear. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)

class femur_bone(monster_part):
    def __init__(self, qty):
        self.qty = qty
        enemy = enemies.skeleton()
        super().__init__(name="Femur Bone",
                         description="A femur bone from a walking skeleton. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
class rat_tail(monster_part):
    def __init__(self, qty):
        self.qty = qty
        enemy = enemies.large_rat()
        super().__init__(name="Rat Tail",
                         description="A rat's tail. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
class bat_wing(monster_part):
    def __init__(self, qty):
        self.qty = qty
        enemy = enemies.demon_bat()
        super().__init__(name="Bat Wing",
                         description="A bat's wing. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)