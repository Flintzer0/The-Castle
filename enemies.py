import random, time
from utilities import text_speed

class Enemy:

    steal_list = {}
    
    status = {
        'poison': False,
        'paralysis': False,
        'blind': False,
        'silence': False,
        'sleep': False,
        'confusion': False,
        'charm': False,
        'crippled': False,
        }
    
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.name = name
        self.tier = tier
        self.hp = hp
        self.mhp = mhp
        self.damage = damage
        self.statusatk = statusatk
        self.status_chance = status_chance
        self.weak = weak
        self.DEF = DEF
        self.RES = RES
        self.SPD = SPD
        self.SKL = SKL
        self.LUCK = LUCK
        self.EXP = EXP
        self.gold = gold
        self.part = part
        self.description = description
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return "{}     Type: {}\n========================================\n{}========================================\nHP: {}     Weakness: {}\nDMG: {}     DEF: {}\nRES: {}     SPD: {}\nSKL: {}     LUCK: {}\n".format(self.name, self.ID, self.description, self.mhp, self.weak, self.damage, self.DEF, self.RES, self.SPD, self.SKL, self.LUCK)
 
    def AVO(self):
        return ((self.SPD + self.SKL) * (random.randint(self.LUCK, 100) / 100))

    def is_alive(self):
        return self.hp > 0
    
    def roll_status(self):
        return random.randint(1,100) <= self.status_chance
    
    def drop_part(self):
        import items
        part = self.part
        return random.randint(1,100) <= 100 * part.drop_rate
    
    def apply_poison(self):
        if self.status['poison'] == True:
            damage = random.randint(1, 5)
            self.hp -= damage
            text_speed("The {} takes {} damage from poison!\n".format(self.name, damage), .03)
            time.sleep(.2)

# Enemy Types
class Undead(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Undead"
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Beast(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Beast"
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Bug(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Bug"
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Humanoid(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Humanoid"
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Demon(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Demon"
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Dragon(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Dragon"
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Shifter(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Shifter"
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Boss(Enemy):
    def __init__(self, name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        super().__init__(name, tier, hp, mhp, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class dummy(Enemy):
    def __init__(self):
        super().__init__(name="Dummy", tier=0, hp=1000000, mhp=1000000, damage=0, statusatk=None, status_chance=0, weak=None, DEF=0, RES=0, SPD=0, SKL=0, LUCK=0, EXP=0, gold=0, part=None,
                         description="A wooden dummy. It doesn't do anything.\n")
        self.id = "Dummy"

class testing_boss(Demon, Boss):
    def __init__(self):
        super().__init__(name="Mega Demon", tier=50, hp=1000, mhp=1000, damage=150, statusatk=None, status_chance=0, weak=None, DEF=80, RES=80, SPD=80, SKL=50, LUCK=40, EXP=0, gold=0, part=None,
                         description="The Mega Demon, a powerful foe for any adventurer to face.")

# Tier 1 Enemies
class giant_spider(Bug):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.spider_silk(10),
        '3': items.garnet(5)
    }

    def __init__(self):
        import items
        super().__init__(name="Giant Spider", tier=1, hp=10, mhp=10, damage=2, statusatk=None, status_chance=0, weak=None, DEF=0, RES=1, SPD=3, SKL=2, LUCK=1, EXP=13, gold=10, part=items.spider_leg(1),
                         description="A large spider with dripping fangs and a hairy body.\nThey are quicker than most basic monsters. Being all buggy, its defense\nisn't superb, but it has a bit of magic resistance.\n")
 
class goblin(Humanoid):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.goblin_fingernail(10),
        '3': items.amethyst(5)
    }

    def __init__(self):
        import items
        super().__init__(name="Goblin",
                         tier=1,
                         hp=5,
                         mhp=5,
                         damage=1,
                         statusatk=None,
                         status_chance=0,
                         weak="Cold",
                         DEF=1,
                         RES=0,
                         SPD=2,
                         SKL=1,
                         LUCK=0,
                         EXP=10,
                         gold=16,
                         part=items.goblin_ear(1),
                         description="A small, green humanoid with a large nose and pointed ears.\nThey aren't very special, but they have a bit of defense.\n")

class skeleton(Undead):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.bone(10),
        '3': items.opal(5)
    }

    def __init__(self):
        import items
        super().__init__(name="Skeleton",
                         tier=1,
                         hp=7, 
                         mhp=7, 
                         damage=3, 
                         statusatk=None, 
                         status_chance=0, 
                         weak=None, 
                         DEF=2, 
                         RES=-1, 
                         SPD=1, 
                         SKL=0, 
                         LUCK=0, 
                         EXP=17, 
                         gold=13, 
                         part=items.femur_bone(1),
                         description="A walking skeleton. \nThey are slow, but they have some defense and deal a little more \ndamage. Very weak to Magic damage.\n")
        
class large_rat(Beast):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.rat_fur(10),
        '3': items.opal(5)
    }

    def __init__(self):
        import items
        super().__init__(name="Large Rat", tier=1, hp=15, mhp=10, damage=3, statusatk="Disease", status_chance=30, weak="Fire", DEF=1, RES=1, SPD=1, SKL=0, LUCK=0, EXP=15, gold=15, part=items.rat_tail(1),
                         description="An incredibly large rat.\nThey aren't hard tp hurt, but their thick hide and hard teeth give them\ndecent health and damage.\n")

class demon_bat(Demon):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.stone(10),
        '3': items.ruby(5)
    }

    def __init__(self):
        import items
        super().__init__(name="Demon Bat", tier=1, hp=4, mhp=4, damage=2, statusatk=None, status_chance=0, weak="Holy", DEF=0, RES=3, SPD=4, SKL=3, LUCK=1, EXP=12, gold=9, part=items.bat_wing(1),
                         description="A bat with red eyes and a demonic aura. \nThey are quick and have a bit of magic resistance, but physically weak.\n")
        
class zombie(Undead):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.wood_plank(10),
        '3': items.amethyst(5)
    }

    def __init__(self):
        import items
        super().__init__(name="Zombie", tier=1, hp=15, mhp=15, damage=3, statusatk="Disease", status_chance=45, weak=None, DEF=2, RES=2, SPD=1, SKL=0, LUCK=0, EXP=20, gold=20, part=items.rotting_flesh(1),
                         description="A walking corpse.\nThey are slow, but they have some defense and deal a little more damage.\nIt is important to strike them down quickly to avoid being afflicted\nwith DISEASE.\n")

# Tier 2 Enemies


# Tier 3 Enemies


# Tier 4 Enemies


# Bosses
# BF2 Boss
class underking(Boss, Undead):
    import items

    steal_list = {
        '1': items.gold(100),
        '2': items.elixir(10),
        '3': items.diamond(10)
    }

    def __init__(self):
        import items
        super().__init__(name="Underking", hp=200, mhp=200, damage=50, statusatk="Wither", status_chance=70, weak="Holy", DEF=15, RES=20, SPD=18, SKL=35, LUCK=10, EXP=100, gold=3000, part=items.obsidian_blade(),
                         description="The powerful Underking, once the ruler of all below the surface.\nHe is a powerful foe, with high damage, defense, and resistance, and is\ncapable of inflicting WITHER. Only engage when you are ready.\n")

# BF1 Boss
class giant_centipede(Boss, Bug):
    import items

    potential_weapons = {items.rusty_sword(), items.rusty_sword(), items.rusty_axe(), items.rusty_axe, items.wooden_spear(), items.wooden_spear, items.iron_spear()}

    steal_list = {
        '1': items.gold(100),
        '2': random.choice(list(potential_weapons)),
        '3': items.diamond(1)
    }

    def __init__(self):
        import items
        super().__init__(name="Centipede", tier="Boss", hp=20, mhp=20, damage=5, statusatk="Poison", status_chance=50, weak="Fire", DEF=3, RES=2, SPD=5, SKL=4, LUCK=2, EXP=50, gold=30, part=items.centipede_carapace(1),
                         description="A giant centipede, with acid dripping off its mandibles. There also \nappears to be several old weapons stuck in its hard shell. Being a \ncentipede, it is quite dangerous, with high damage, some defense both \nphysically and magically, quick, and capable of making skillful \nstrikes. Only engage when you are ready.\n")
        
# F1 Boss

# F2 Boss

# F3 Boss

# F4 Boss

# F5 Boss
