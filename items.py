from scroll_spells import *
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
        self.buff = ""
 
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

# This is simply a placeholder item for when an item is sold out.
class sold_out(Item):
    def __init__(self):
        super().__init__(name="Sold Out!",
                         description="This item is sold out.",
                         value=0)
        
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

class dragon_fangs(Magic_Weapon):
    def __init__(self):
        self.damage_type = "Fire"
        super().__init__(name="Dragon Fangs",
                         description="Ornate twin daggers whose blades are made from dragon's teeth. \nThey emanate a harsh heat. \nAll damage dealt by this weapon is Fire damage.",
                         value=2500,
                         damage=60,
                         damage_type="Fire")

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
        
class blade_of_starlight(Magic_Weapon):
    def __init__(self):
        self.damage_type = "Holy"
        super().__init__(name="Blade of Starlight",
                         description="The sacred Starlight Blade of legend. \nIt appears as though the blade is encrusted with distant stars. \nAll damage dealt by this weapon is Holy damage.",
                         value=2500,
                         damage=60,
                         damage_type="Holy")

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

class blood_letter(Magic_Weapon):
    def __init__(self):
        super().__init__(name="Blood Letter",
                         description="A wicked axe with a serrated blade. \nIt seems to always have blood on its edge. \nAll damage dealt by this weapon is Necrotic damage.",
                         value=2500,
                         damage=60,
                         damage_type="Necrotic")

# Hammer Items
class rusty_hammer(Weapon):
    def __init__(self):
        super().__init__(name="Rusty Hammer",
                         description="A hammer covered in rust.",
                         value=3,
                         damage=3)

class mountain_cracker(Magic_Weapon):
    def __init__(self):
        super().__init__(name="Mountain Cracker",
                         description="A massive hammer, said to be capable of crushing mountains. \nIt's a bit heavy, but it's worth it. \nAll damage dealt by this weapon is Earth damage.",
                         value=2500,
                         damage=60,
                         damage_type="Earth")

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

class the_northern_star(Magic_Weapon):
    def __init__(self):
        super().__init__(name="The Northern Star",
                         description="A large bow that can shoot passed one's own sight. \nEvery arrow fired from this bow shines with a cold light. \nAll damage dealt by this weapon is Cold damage.",
                         value=2500,
                         damage=60,
                         damage_type="Cold")

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

class the_evertree(Spellcaster):
    def __init__(self):
        super().__init__(name="The Evertree",
                         description="A staff made of twisting wood. \nWhen motionless, it almost appears to be rooting itself into the ground. \nGreatly improves the damage of spells.",
                         value=2500,
                         damage=20,
                         mdamage=60)

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

class Magic_Armor(Armor):
    def __init__(self, name, description, value, armor, marmor, resistance, resamt, buff, propercent):
        self.marmor = marmor
        self.resistance = resistance
        self.resamt = resamt
        self.buff = buff
        self.propercent = propercent
        super().__init__(name, description, value, armor)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nArmor: {}\nMagic Armor: {}\nResistance: {}\nbuff: {}".format(self.name, self.description, self.value, self.armor, self.marmor, self.resistance, self.buff)

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

class starweave(Magic_Armor):
    def __init__(self):
        super().__init__(name="Starweave",
                         description="Cloth armor woven from the the remains of a meteor. \nIt is light and comfortable, and shines with a faint light. \nAll Demonic damage is reduced by 50%.\nApplies a permanent 40% Mana Rage buff while worn.",
                         value=2500,
                         armor=10,
                         marmor=30,
                         resistance="demonic_resist",
                         resamt=0.5,
                         buff="mana_rage",
                         propercent=0.4)

class shadecloak(Magic_Armor):
    def __init__(self):
        super().__init__(name="Shadecloak",
                         description="Cloth armor said to be woven with the fibers of the moon's shadow. \nWhile is seems harmless to the wearer, any attakers seem to wither upon contact. \nAll Holy damage is reduced by 50%.",
                         value=2500,
                         armor=20,
                         marmor=20,
                         resistance="holy",
                         resamt=0.5,
                         buff="necrosis",
                         propercent=0.3)

class cowl_of_the_hunt(Magic_Armor):
    def __init__(self):
        super().__init__(name="Cowl of the Hunt",
                         description="A hood made of the fur of a great wolf. \nIt feels as though your senses are sharper while you wear this. \nGain a resistance of 50% to POISON.",
                         value=2500,
                         armor=25,
                         marmor=15,
                         resistance="poison_resist",
                         resamt=0.5,
                         buff="heightened_senses",
                         propercent=15)

class chainmail(Armor):
    def __init__(self):
        super().__init__(name="Chainmail",
                         description="A simple chainmail. Provides minimal protection.",
                         value=15,
                         armor=3)

class healer_ringmail(Magic_Armor):
    def __init__(self):
        super().__init__(name="Ringmail of the Healer",
                         description="Intricately linked ringmail colored red and white. \nIt is said that it was blessed by the gods themselves. \nWearers benefit from a resistance to Necrotic damage of 50%.",
                         value=2500,
                         armor=15,
                         marmor=25,
                         resistance="necrotic_resist",
                         resamt=0.5,
                         buff="regen",
                         propercent=0.2)

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

class sunplate(Magic_Armor):
    def __init__(self):
        super().__init__(name="Sunplate",
                         description="A suit of platemail embossed with symbols of the sun. \nWhen worn, it shines so brightly that it is hard to look at. \nAll Necrotic damage dealt is reduced by 50%.",
                         value=2500,
                         armor=25,
                         marmor=15,
                         resistance="necrotic_resist",
                         resamt=0.5,
                         buff="blind",
                         propercent=0.3)

class bloodplate(Magic_Armor):
    def __init__(self):
        super().__init__(name="Bloodplate",
                         description="Bloodred platemail with a sinister aura. \nIts energy tries to sap away the strength of any who inted to harm it. \nAll Holy damage dealt is reduced by 50%.",
                         value=2500,
                         armor=20,
                         marmor=20,
                         resistance="holy_resist",
                         resamt=0.5,
                         buff="cripple",
                         propercent=0.3)

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
    def __init__(self, name, description, value, armor, marmor, buff, propercent, resistance, resamt):
        self.marmor = marmor
        self.buff = buff
        self.propercent = propercent
        self.resistance = resistance
        self.resamt = resamt
        super().__init__(name, description, value, armor)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nArmor: {}\nMagic Armor: {}".format(self.name, self.description, self.value, self.armor, self.marmor)

class iron_curtain(Spellshield):
    def __init__(self):
        super().__init__(name="Iron Curtain",
                         description="The shield of a powerful warrior. It glints in the light. \nIt provides high protection against physical attacks, and resistance to Cold damage.",
                         value=200,
                         armor=10,
                         marmor=5,
                         buff=False,
                         propercent=0,
                         resistance="cold_resist",
                         resamt=0.2)

class brokentower(Spellshield):
    def __init__(self):
        super().__init__(name="Shield of the Broken Tower",
                         description="Made from a reflective, white metal, this shield is embossed with the \nstandard of a long forgotten order of knights. \nIt provides high protection against physical attacks, and resistance to Demonic damage by 50%.",
                         value=200,
                         armor=30,
                         marmor=10,
                         buff="silence",
                         propercent=0.5,
                         resistance="demonic_resist",
                         resamt=0.5)
        
class moonbrace(Spellshield):
    def __init__(self):
        super().__init__(name="Moonbrace",
                         description="A shield made of a strange, silvery metal. It glows with a soft light. \nIt grants the wielder temporary invisibility, and reduces Necrotic damage by 50%.",
                         value=200,
                         armor=15,
                         marmor=25,
                         buff="invisible",
                         propercent=10,
                         resistance="necrotic_resist",
                         resamt=0.2)
        
class fallenshield(Spellshield):
    def __init__(self):
        super().__init__(name="Shield of the Fallen",
                         description="A chipped and cracked shield with the Healer's Mark on its face.\nDespite its obvious wear, it is still strudy and reliable. \nIt grants the wielder Health Regen, and reduces Demonic damage by 50%.",
                         value=200,
                         armor=20,
                         marmor=20,
                         buff="regen",
                         propercent=.25,
                         resistance="demonic_resist",
                         resamt=0.5)
        
class hexbreaker(Spellshield):
    def __init__(self):
        super().__init__(name="Hexbreaker",
                         description="An intricate shield. \nIt grants the wielder resistance to all status effects by 25%, and reduces Magic damage by 20%.",
                         value=200,
                         armor=10,
                         marmor=30,
                         buff="hexbreak",
                         propercent=.25,
                         resistance="magical_resist",
                         resamt=0.2)

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
    def __init__(self, name, description, value, stat, statval, buff, propercent):
        super().__init__(name, description, value)
        self.stat = stat
        self.statval = statval
        self.buff = buff
        self.propercent = propercent
# Strength Rings
class strength_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Strength Ring",
                         description="A ring that increases strength by 1.",
                         value=10,
                         stat="STR",
                         statval=1,
                         buff="",
                         propercent=0)

# Defense Rings
class defense_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Defense Ring",
                         description="A ring that increases defense by 1.",
                         value=10,
                         stat="DEF",
                         statval=1,
                         buff="",
                         propercent=0)
# Magic Rings
class magic_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Magic Ring",
                         description="A ring that increases magic by 1.",
                         value=10,
                         stat="MAG",
                         statval=1,
                         buff="",
                         propercent=0)
# Resistance Rings
class resistance_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Resistance Ring",
                         description="A ring that increases resistance by 1.",
                         value=10,
                         stat="RES",
                         statval=1,
                         buff="",
                         propercent=0)
# Speed Rings
class speed_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Speed Ring",
                         description="A ring that increases speed by 1.",
                         value=10,
                         stat="SPD",
                         statval=1,
                         buff="",
                         propercent=0)
# Skill Rings
class skill_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Skill Ring",
                         description="A ring that increases skill by 1.",
                         value=10,
                         stat="SKL",
                         statval=1,
                         buff="",
                         propercent=0)
# Luck Rings
class luck_1_ring(Ring):
    def __init__(self):
        super().__init__(name="+1 Luck Ring",
                         description="A ring that increases luck by 1.",
                         value=10,
                         stat="LUCK",
                         statval=1,
                         buff="",
                         propercent=0)
# Special Rings
class water_ring(Ring):
    def __init__(self):
        super().__init__(name="Ring of the Sea",
                         description="This ring allows the wearer to breathe underwater.",
                         value=10,
                         stat="",
                         statval=0,
                         buff="water_breathing",
                         propercent=0)

class might_ring(Ring):
    def __init__(self):
        super().__init__(name="Ring of Might",
                         description="This ring grants the wearer +5 STR and DEF.",
                         value=10,
                         stat=["STR", "DEF"],
                         statval=5,
                         buff="",
                         propercent=0)
        
class wisdom_ring(Ring):
    def __init__(self):
        super().__init__(name="Ring of Wisdom",
                         description="This ring grants the wearer +5 MAG and RES.",
                         value=10,
                         stat=["MAG", "RES"],
                         statval=5,
                         buff="",
                         propercent=0)
        
class reflex_ring(Ring):
    def __init__(self):
        super().__init__(name="Ring of Quick Reflexes",
                         description="This ring grants the wearer +5 SPD and SKL.",
                         value=10,
                         stat=["SPD", "SKL"],
                         statval=5,
                         buff="",
                         propercent=0)

class leprechaun_ring(Ring):
    def __init__(self):
        super().__init__(name="Leprechaun Ring",
                         description="This ring grants the wearer +5 LUCK, and grants the Fortune buff.",
                         value=10,
                         stat="LUCK",
                         statval=5,
                         buff="fortune",
                         propercent=.5)

class warding_ring(Ring):
    def __init__(self):
        super().__init__(name="Ring of Warding",
                         description="This ring grants the wearer +5 RES, and resistance 30% to magical attacks.",
                         value=10,
                         stat="RES",
                         statval=5,
                         buff="magic_resist",
                         propercent=.3)

class armor_ring(Ring):
    def __init__(self):
        super().__init__(name="Ring of Armor",
                         description="This ring grants the wearer +5 DEF, and resistance of 30% to physical attacks.",
                         value=10,
                         stat="DEF",
                         statval=5,
                         buff="physical_resist",
                         propercent=.3)
        
class unbreakable(Ring):
    def __init__(self):
        super().__init__(name="Unbreakable Ring",
                         description="This ring grants the wearer +5 DEF and RES, and resistance of 30% to all attacks.",
                         value=10,
                         stat=["DEF", "RES"],
                         statval=5,
                         buff="unbreakable",
                         propercent=.3)

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
    def __init__(self, name, description, value, stat, potency):
        self.stat = stat
        self.potency = potency
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nStat: {}\nPotency: {}".format(self.name, self.description, self.value)

# Can be used in and out of combat.
class Anytime(Potion):
    def __init__(self, name, description, value, stat, potency):
        super().__init__(name, description, value, stat, potency)

# Permanent Stat Boosts
class PermBoost(Anytime):
    def __init__(self, name, description, value, stat, potency):
        super().__init__(name, description, value, stat, potency)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nStat: {}\nPotency: {}".format(self.name, self.description, self.value, self.stat, self.potency)
    
    def boost(self, target):
        if self.stat == "STR":
            target.stats['STR'] += self.potency
        elif self.stat == "DEF":
            target.stats['DEF'] += self.potency
        elif self.stat == "MAG":
            target.stats['MAG'] += self.potency
        elif self.stat == "RES":
            target.stats['RES'] += self.potency
        elif self.stat == "SPD":
            target.stats['SPD'] += self.potency
        elif self.stat == "SKL":
            target.stats['SKL'] += self.potency
        elif self.stat == "LUCK":
            target.stats['LUCK'] += self.potency
        text_speed("You permanently boosted {} by {}!\n".format(self.stat, str(self.potency)), .03)
        time.sleep(.2)

class STR_1_boost(PermBoost):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="+1 Strength Boost",
                         description="A potion that permanently boosts strength by 1. ({})".format(str(self.qty)),
                         value=10,
                         stat="STR",
                         potency=1)
        
class DEF_1_boost(PermBoost):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="+1 Defense Boost",
                         description="A potion that permanently boosts defense by 1. ({})".format(str(self.qty)),
                         value=10,
                         stat="DEF",
                         potency=1)

# Recovery Potions
class Recovery(Anytime):
    def __init__(self, name, description, value, stat, potency):
        super().__init__(name, description, value, stat, potency)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nStat: {}\nPotency: {}".format(self.name, self.description, self.value, self.stat, self.potency)
    
    def heal(self, target):
        if self.stat == "HP":
            if target.stats['cHP'] == target.stats['mHP']:
                text_speed("You are already at full HP!\n", .03)
                time.sleep(.2)
                target.stats['use_potion']()
            elif target.stats['cHP'] + self.potency > target.stats['mHP']:
                target.stats['cHP'] = target.stats['mHP']
                text_speed("You fully restored your HP!\n", .03)
                time.sleep(.2)
            else:
                target.stats['cHP'] += self.potency
                text_speed("{} healed {} HP!\n".format(self.name, str(self.potency)), .03)
                time.sleep(.2)
        elif self.stat == "MP":
            if target.stats['cMP'] == target.stats['mMP']:
                text_speed("You are already at full MP!\n", .03)
                time.sleep(.2)
                target.stats['use_potion']()
            if target.stats['cMP'] + self.potency > target.stats['mMP']:
                target.stats['cMP'] = target.stats['mMP']
                text_speed("You fully restored your MP!\n", .03)
                time.sleep(.2)
            else:
                target.stats['cMP'] += self.potency
                text_speed("{} recovered {} MP!\n".format(self.name, str(self.potency)), .03)
                time.sleep(.2)
        elif self.stat == "HP/MP":
            if target.stats['cHP'] == target.stats['mHP'] and target.stats['cMP'] == target.stats['mMP']:
                text_speed("You are already at full HP and MP!\n", .03)
                time.sleep(.2)
                target.stats['use_potion']()
            if target.stats['cHP'] + self.potency > target.stats['mHP']:
                target.stats['cHP'] = target.stats['mHP']
                text_speed("You fully restored your HP!\n", .03)
                time.sleep(.2)
            else:
                target.stats['cHP'] += self.potency
                text_speed("You healed {} HP!\n".format(str(self.potency)), .03)
                time.sleep(.2)
            if target.stats['cMP'] + self.potency > target.stats['mMP']:
                target.stats['cMP'] = target.stats['mMP']
                text_speed("You fully restored your MP!\n", .03)
                time.sleep(.2)
            else:
                target.stats['cMP'] += self.potency
                text_speed("You recovered {} MP!\n".format(str(self.potency)), .03)
                time.sleep(.2)


class small_red_potion(Recovery):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Small Red Potion",
                         description="A small red potion. Heals 5 HP. ({})".format(str(self.qty)),
                         value=5,
                         stat="HP",
                         potency=5)

class large_red_potion(Recovery):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Large Red Potion",
                         description="A large red potion. Heals 10 HP. ({})".format(str(self.qty)),
                         value=10,
                         stat="HP",
                         potency=10)

class small_blue_potion(Recovery):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Small Blue Potion",
                         description="A small blue potion. Recovers 5 MP. ({})".format(str(self.qty)),
                         value=5,
                         stat="MP",
                         potency=5)
        
class elixir(Recovery):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Elixir",
                         description="A magical elixir. Fully restores HP and MP. ({})".format(str(self.qty)),
                         value=15,
                         stat="HP/MP",
                         potency=99999)
        
    def heal(self, target):
        if target.stats['cHP'] == target.stats['mHP'] and target.stats['cMP'] == target.stats['mMP']:
            text_speed("You are already at full HP and MP!\n", .03)
            time.sleep(.2)
            target.stats['use_potion']()
        else:
            target.stats['cHP'] = target.stats['mHP']
            target.stats['cMP'] = target.stats['mMP']
            text_speed("You fully restored your HP and MP!\n".format(self.name), .03)
            time.sleep(.2)

# Boost Potions
class BoostPotion(Potion):
    def __init__(self, name, description, value, stat, potency, duration):
        self.duration = duration
        super().__init__(name, description, value, stat, potency)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nStat: {}\nPotency: {}".format(self.name, self.description, self.value, self.stat, self.potency)
    
    def boost(self, target):
        target.tempboosts[self.stat]['flag'] = True
        target.tempboosts[self.stat]['value'] = self.potency
        target.tempboosts[self.stat]['duration'] = self.duration
        target.stats['starting_turn'] = target.stats['turns']
        text_speed("You boosted {} by {}!\n".format(self.stat, str(self.potency)), .03)
        time.sleep(.2)

class minor_strength_boost(BoostPotion):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Minor Potion of Boost Strength",
                         description="A potion that temporarily boosts strength by 1. ({})".format(str(self.qty)),
                         value=10,
                         stat="STR",
                         potency=1,
                         duration=10)

# Scroll Items
class Scroll(Item):
    def __init__(self, name, description, value, spell):
        self.spell = spell
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nSpell: {}".format(self.name, self.description, self.value, self.spell)
    
class scroll_of_fireball(Scroll):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Scroll of Fireball",
                         description="A scroll with a fireball spell inscribed on it. Casts Fireball. ({})".format(str(self.qty)),
                         value=10,
                         spell=fireball())

# Throw Items
class Thrown(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)
    
    def throw(self, user, target):
        if user.status['blind'] != True:
            total = (self.damage + user.STR) - target.stats['DEF']
            target.stats['hp'] -= total
            text_speed("You threw the {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("The {} dealt {} damage to the {}!\n".format(self.name, total, target.stats['name']), .03)
            time.sleep(.2)

class rock(Thrown):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Rock",
                         description="A simple rock. Deals damage to a single target. ({})".format(str(self.qty)),
                         value=1,
                         damage=1)
        
class throwing_knife(Thrown):
    def __init__(self, qty):
        self.qty = qty
        super().__init__(name="Throwing Knife",
                         description="A simple throwing knife. Deals damage to a single target. ({})".format(str(self.qty)),
                         value=5,
                         damage=5)

# Boost Items
class StatBoost(Item):
    def __init__(self, name, description, value, stat, potency, duration):
        self.stat = stat
        self.potency = potency
        self.duration = duration
        super().__init__(name, description, value)
    
    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nStat: {}\nPotency: {}\nDuration: {}".format(self.name, self.description, self.value, self.stat, self.potency, self.duration)
    
    def boost(self, target):
        target.tempboosts[self.stat]['value'] += self.potency
        if target.tempboosts[self.stat]['flag'] == False:
            target.tempboosts[self.stat]['flag'] = True
            target.tempboosts[self.stat]['value'] = self.potency
            target.tempboosts[self.stat]['duration'] = self.duration
            target.starting_turn = target.turns
        else:
            if target.tempboosts[self.stat]['duration'] < self.duration:
                target.tempboosts[self.stat]['duration'] = self.duration
        text_speed("You boosted {} by {}!\n".format(self.stat, str(self.potency)), .03)
        time.sleep(.2)

class StatusBoost(Item):
    def __init__(self, name, description, value, status, duration):
        self.status = status
        self.duration = duration
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nStatus: {}\nDuration: {}".format(self.name, self.description, self.value, self.status, self.duration)
    
    def boost(self, target):
        target.tempstatus[self.status]['value'] += self.potency
        if target.tempstatus[self.status]['flag'] == False:
            target.tempstatus[self.status]['flag'] = True
            target.tempstatus[self.status]['duration'] = self.duration
            target.starting_turn = target.turns
        else:
            if target.tempstatus[self.status]['duration'] < self.duration:
                target.tempstatus[self.status]['duration'] = self.duration
        text_speed("You are now {}!\n".format(self.status), .03)
        time.sleep(.2)

class ResistanceBoost(Item):
    def __init__(self, name, description, value, resistance, potency, duration):
        self.resistance = resistance
        self.potency = potency
        self.duration = duration
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nResistance: {}\nPotency: {}\nDuration: {}".format(self.name, self.description, self.value, self.resistance, self.potency, self.duration)
    
    def boost(self, target):
        target.tempresistances[self.resistance]['value'] += self.potency
        if target.tempresistances[self.resistance]['flag'] == False:
            target.tempresistances[self.resistance]['flag'] = True
            target.tempresistances[self.resistance]['duration'] = self.duration
            target.starting_turn = target.turns
        else:
            if target.tempresistances[self.resistance]['duration'] < self.duration:
                target.tempresistances[self.resistance]['duration'] = self.duration
        target.stats['starting_turn'] = target.stats['turns']
        text_speed("You are now have {} + {}!\n".format(self.resistance, self.potency), .03)
        time.sleep(.2)

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