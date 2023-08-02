'''
Damage Types:
    Fire
    Cold
    Lightning
    Water
    Earth
    Wind
    Holy
    Demonic
    Necrotic
    Poison
    Turn Undead (labeled as Turn in-code)
'''

class Item():
    """The base class for all items"""
    damage_type = ""
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value
        self.spcl = ""
 
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
    def __repr__(self):
        return self.name
    
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
    
class Magic_Weapon(Weapon):
    def __init__(self, name, description, value, damage, damage_type):
        self.damage_type = damage_type
        super().__init__(name, description, value, damage)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDamage Type: {}".format(self.name, self.description, self.value, self.damage, self.damage_type)

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

# Magic Swords
class cold_iron_sword(Magic_Weapon):
    def __init__(self):
        self.damage_type = "Cold"
        super().__init__(name="Cold Iron Sword",
                         description="A solid blade of iron that glints a steely blue in the light. \nIt's cold to the touch. All damage dealt by this weapon is Cold damage.",
                         value=150,
                         damage=15,
                         damage_type="Cold")

class demonsbane(Magic_Weapon):
    def __init__(self):
        self.damage_type = "Holy"
        super().__init__(name="Demonsbane",
                         description="A blade of brightly shining, white steel. It fills you with warmth. \nAll damage dealt by this weapon is Holy damage.",
                         value=200,
                         damage=20,
                         damage_type="Holy")

class flamelash(Magic_Weapon):
    def __init__(self):
        self.damage_type = "Fire"
        super().__init__(name="Flamelash",
                         description="When drawn, the blade of this immediately ignites. The flames flicker wickedly. \nAll damage dealt by this weapon is Fire damage.",
                         value=120,
                         damage=12,
                         damage_type="Fire")
        
class sparktongue(Magic_Weapon):
    def __init__(self):
        self.damage_type = "Lightning"
        super().__init__(name="Sparktongue",
                         description="A blade of pure lightning. It crackles and sparks when drawn. \nAll damage dealt by this weapon is Lightning damage.",
                         value=120,
                         damage=12,
                         damage_type="Lightning")

class obsidian_blade(Magic_Weapon):
    def __init__(self):
        self.damage_type = "Necrotic"
        super().__init__(name="Obsidian Blade",
                         description="A blade of pure obsidian, once owned by the Underking.\nIt's pitch black and seems to absorb light. \nAll damage dealt by this weapon is Necrotic damage.",
                         value=2500,
                         damage=25,
                         damage_type="Necrotic")

# Polearm Items
class wooden_spear(Weapon):
    def __init__(self):
        super().__init__(name="Wooden Spear",
                         description="A simple wooden spear. It's not very sturdy, but it's better than nothing.",
                         value=10,
                         damage=3)
        
class iron_spear(Weapon):
    def __init__(self):
        super().__init__(name="Iron Spear",
                         description="A simple iron spear. It's not very sturdy, but it's better than nothing.",
                         value=25,
                         damage=6)
        
# Axe Items
class rusty_axe(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Axe",
                         description="An axe covered in rust.",
                         value=3,
                         damage=4)
# Hammer Items
class rusty_hammer(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Hammer",
                         description="A hammer covered in rust.",
                         value=3,
                         damage=3)
# Mace Items
class rusty_mace(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Mace",
                         description="A mace covered in rust.",
                         value=3,
                         damage=3)
# Bow Items
class wooden_bow(Weapon):
    def __init__(self):
        super().__init__(name="Wooden Bow",
                         description="A simple wooden bow. It's not very sturdy, but it's better than nothing.",
                         value=10,
                         damage=2)

# Weapons with Magic Damage
class Spellcaster(Weapon):
    def __init__(self, name, description, value, damage, mdamage):
        self.mdamage = mdamage
        super().__init__(name, description, value, damage)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}\nDamage Type: {}".format(self.name, self.description, self.value, self.damage, self.mdamage)

# Staff Items
class wooden_staff(Spellcaster):
    def __init__(self):
        super().__init__(name="Wooden Staff",
                         description="A simple wooden staff. It's not very sturdy, but it's better than nothing.",
                         value=10,
                         damage=1,
                         mdamage=3)
# Wand Items
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
        
class rusty_armor(Armor):
    def __init__(self):
        super().__init__(name="Rusty Armor",
                         description="Rusted iron armor. Provides minimal protection.",
                         value=5,
                         armor=2)

class leather_armor(Armor):
    def __init__(self):
        super().__init__(name="Leather Armor",
                         description="A simple leather armor. Provides minimal protection.",
                         value=10,
                         armor=2)
        
class chainmail(Armor):
    def __init__(self):
        super().__init__(name="Chainmail",
                         description="A simple chainmail. Provides minimal protection.",
                         value=15,
                         armor=3)

class iron_armor(Armor):
    def __init__(self):
        super().__init__(name="Iron Armor",
                         description="A simple iron armor. Provides minimal protection.",
                         value=20,
                         armor=4)
        
class plate(Armor):
    def __init__(self):
        super().__init__(name="Plate Armor",
                         description="Sturdy plate armor. Provides great protection",
                         value=25,
                         armor=10)

# Shield Items
class Shield(Item):
    def __init__(self, name, description, value, armor):
        self.armor = armor
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nArmor: {}".format(self.name, self.description, self.value, self.armor)
    
class open_hand(Shield):
    def __init__(self):
        super().__init__(name="Open Hand",
                         description="You're not using a shield.",
                         value=0,
                         armor=0)

class rusty_shield(Shield):
    def __init__(self):
        super().__init__(name="Rusty Shield",
                         description="A bent and rusty shield. Provides minimal protection.",
                         value=3,
                         armor=1)

# Magic Shields
class Spellshield(Shield):
    def __init__(self, name, description, value, armor, resistance):
        super().__init__(name, description, value, armor)
        self.resistance = resistance

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nArmor: {}\nMagic Damage: {}".format(self.name, self.description, self.value, self.armor, self.resistance)

class iron_curtain(Spellshield):
    def __init__(self):
        super().__init__(name="Iron Curtain",
                         description="The shield of a powerful warrior. It glints in the light. \nIt provides high protection against physical attacks, and resistance to Cold damage.",
                         value=200,
                         armor=10,
                         resistance="Cold")

# These items are all equipment used for increasing stats.
# Accessory Items
class Accessory(Item):
    def __init__(self, name, description, value):
        super().__init__(name, description, value)

    # Ring Items

class empty(Accessory):
    def __init__(self):
        super().__init__(name="Empty",
                         description="This slot is open.",
                         value=0)
        
    def __str__(self):
        return "\n=====\n{}\n".format(self.description)

class Ring(Accessory):
    def __init__(self, name, description, value, stat, statval, spcl):
        super().__init__(name, description, value)
        self.stat = stat
        self.statval = statval
        self.spcl = spcl        
# Strength Rings
class strength_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Strength Ring",
                         description="A ring that increases strength by 1.",
                         value=10,
                         stat="STR",
                         statval=1,
                         spcl="")
# Defense Rings
class defense_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Defense Ring",
                         description="A ring that increases defense by 1.",
                         value=10,
                         stat="DEF",
                         statval=1,
                         spcl="")
# Magic Rings
class magic_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Magic Ring",
                         description="A ring that increases magic by 1.",
                         value=10,
                         stat="MAG",
                         statval=1,
                         spcl="")   
# Resistance Rings
class resistance_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Resistance Ring",
                         description="A ring that increases resistance by 1.",
                         value=10,
                         stat="RES",
                         statval=1,
                         spcl="")
# Speed Rings
class speed_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Speed Ring",
                         description="A ring that increases speed by 1.",
                         value=10,
                         stat="SPD",
                         statval=1,
                         spcl="")
# Skill Rings
class skill_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Skill Ring",
                         description="A ring that increases skill by 1.",
                         value=10,
                         stat="SKL",
                         statval=1,
                         spcl="")
# Luck Rings
class luck_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Luck Ring",
                         description="A ring that increases luck by 1.",
                         value=10,
                         stat="LUCK",
                         statval=1,
                         spcl="")
# Special Rings
class water_ring(Ring):
    def __init__(self):
        self.spcl = "Water Breathing"
        super().__init__(name="Ring of the Sea",
                         description="This ring allows the wearer to breathe underwater. \nSpecial: {}".format(self.spcl),
                         value=10,
                         stat="",
                         statval=0,
                         spcl=self.spcl)
# Necklace Items
# Bracelet Items
# Earring Items
# Waist Items
# Headgear Items
# Foot Items
# Hand Items
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
    def __init__(self, name, description, value, heal, mheal):
        self.heal = heal
        self.mheal = mheal
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)
    
class small_red_potion(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Small Red Potion",
                         description="A small red potion. Heals 5 HP. ({})".format(str(self.qty)),
                         value=5,
                         heal=5,
                         mheal=0)

class large_red_potion(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Large Red Potion",
                         description="A large red potion. Heals 10 HP. ({})".format(str(self.qty)),
                         value=10,
                         heal=10,
                         mheal=0)

class small_blue_potion(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Small Blue Potion",
                         description="A small blue potion. Recovers 5 MP. ({})".format(str(self.qty)),
                         value=5,
                         heal=0,
                         mheal=5)
        
class elixir(Potion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Elixir",
                         description="A magical elixir. Fully restores HP and MP. ({})".format(str(self.qty)),
                         value=15,
                         heal=999,
                         mheal=999)

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

class emerald(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Emerald",
                         description="A simple emerald. Used for upgrading. ({})".format(str(self.qty)),
                         value=200,
                         rarity=5)
        
class sapphire(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Sapphire",
                         description="A simple sapphire. Used for upgrading. ({})".format(str(self.qty)),
                         value=200,
                         rarity=5)
        
class diamond(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Diamond",
                         description="A simple diamond. Used for upgrading. ({})".format(str(self.qty)),
                         value=1000,
                         rarity=5)
        
class topaz(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Topaz",
                         description="A simple topaz. Used for upgrading. ({})".format(str(self.qty)),
                         value=150,
                         rarity=5)
        
class amethyst(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Amethyst",
                         description="A simple amethyst. Used for upgrading. ({})".format(str(self.qty)),
                         value=50,
                         rarity=5)
        
class opal(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Opal",
                         description="A simple opal. Used for upgrading. ({})".format(str(self.qty)),
                         value=100,
                         rarity=5)
        
class garnet(Material):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Garnet",
                         description="A simple garnet. Used for upgrading. ({})".format(str(self.qty)),
                         value=50,
                         rarity=5)

# Cloth Items
# Monster Parts
# This is the base class for all monster parts.
class monster_part(Material):
    def __init__(self, name, description, value, rarity, drop_rate):
        self.drop_rate = drop_rate
        super().__init__(name, description, value, rarity)

# Basic Monster Parts
class spider_leg(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Spider Leg",
                         description="A spider's leg. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
class spider_silk(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Spider Silk",
                         description="A spider's silk. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)

class goblin_ear(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Goblin Ear",
                         description="A goblin's ear. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
class goblin_fingernail(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Goblin Fingernail",
                         description="A goblin's fingernail. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)

class bone(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Bone",
                         description="A bone from a skeleton. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)

class femur_bone(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Femur Bone",
                         description="A femur bone from a walking skeleton. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
class rat_fur(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Rat Fur",
                         description="A rat's fur. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)

class rat_tail(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Rat Tail",
                         description="A rat's tail. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
class bat_wing(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Bat Wing",
                         description="A bat's wing. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
class rotting_flesh(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Rotting Flesh",
                         description="A piece of rotting flesh. Used for upgrading. ({})".format(str(self.qty)),
                         value=5,
                         rarity=1,
                         drop_rate=0.5)
        
# Boss Monster Parts
class centipede_carapace(monster_part):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Centipede Carapace",
                         description="A centipede's carapace. Used for upgrading. ({})".format(str(self.qty)),
                         value=20,
                         rarity=2,
                         drop_rate=0.3)