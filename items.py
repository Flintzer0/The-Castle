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

class dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small, clean dagger. It glints in the light.",
                         value=5,
                         damage=5)

# Sword Items
# Polearm Items
# Axe Items
# Bow Items
# Staff Items
# Tome Items
# Rod Items
# Thrown Items

# These are all items used for defending against enemy attacks.
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

# Armor Items
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
        
# These items are all materials used for item upgrades and repairs.
# Wood Items
# Ore Items
# Gem Items
# Cloth Items
# Monster Parts