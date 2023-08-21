import random, time, enemy_skills, magic
from utilities import *

class Enemy:

    steal_list = {}
    
    status = {
        'poison': {'flag' : False, 'potency' : 0},
        'paralysis': {'flag' : False, 'potency' : 0},
        'blind': {'flag' : False, 'potency' : 0},
        'silence': {'flag' : False, 'potency' : 0},
        'sleep': {'flag' : False, 'potency' : 0},
        'confusion': {'flag' : False, 'potency' : 0},
        'charm': {'flag' : False, 'potency' : 0},
        'crippled': {'flag' : False, 'potency' : 0},
        }

    skills = []
    spells = []

    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.name = name
        self.tier = tier
        self.stats = {
            'HP': HP,
            'mHP': mHP,
            'DEF': DEF,
            'RES': RES,
            'SPD': SPD,
            'SKL': SKL,
            'LUCK': LUCK
        }
        self.damage = damage
        self.statusatk = statusatk
        self.status_chance = status_chance
        self.weak = weak
        self.EXP = EXP
        self.gold = gold
        self.part = part
        self.description = description
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return "{}     Type: {}\n========================================\n{}========================================\nHP: {}     Weakness: {}\nDMG: {}     DEF: {}\nRES: {}     SPD: {}\nSKL: {}     LUCK: {}\n".format(self.name, self.ID, self.description, self.stats['mHP'], self.weak, self.damage, self.stats['DEF'], self.stats['RES'], self.stats['SPD'], self.stats['SKL'], self.stats['LUCK'])
 
    def AVO(self):
        return ((self.stats['SPD'] + self.stats['SKL']) * (random.randint(self.stats['LUCK'], 100) / 100))

    def is_alive(self):
        return self.stats['HP'] > 0
    
    def roll_status(self):
        return random.randint(1,100) <= self.status_chance
    
    def drop_part(self):
        import items
        if self.part:
            part = self.part
            return random.randint(1,100) <= 100 * part.drop_rate
        else:
            return False
    
    def apply_poison(self):
        if self.status['poison'] == True:
            damage = self.status['poison']['potency']
            self.stats['HP'] -= damage
            text_speed("The {} takes {} damage from poison!\n".format(self.name, damage), .03)
            time.sleep(.2)

    def use_skill(self, skill, player):
        if isinstance(skill, enemy_skills.Restore):
            return skill.use(self)
        else:
            return skill.use(self, player)

    def use_spell(self, spell, player):
        return spell.cast_spell(self, player)

    def attack(self, player):
        if calculate_hit(self, player):
            text_speed("The {} attacks!\n".format(self.name), .03)
            time.sleep(.2)
            ecrit = chk_CRIT(self, player)
            edamage = generate_edamage(self, self.damage, self.damage)
            if ecrit:
                text_speed("Critical hit!\n", .01)
                time.sleep(.05)
                edamage *= 2
            parmor = player.chk_armor()
            if player.buffs['physical_resist']['flag'] == True:
                damage = round(edamage - (edamage * parmor) - (edamage * player.buffs['physical_resist']['potency']))
            else:
                damage = round(edamage - (edamage * parmor))
            if damage <= player.stats['DEF']['value']:
                damage = 1
            else:
                damage = damage - player.stats['DEF']['value']
            player.stats['cHP']['value'] -= damage
            text_speed("The {} dealt {} damage to you!\n".format(self.name, damage), .03)
            time.sleep(.2)
        else:
            text_speed("{} missed!\n".format(self.name), .03)
            time.sleep(.2)

# Enemy Types
class Undead(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Undead"
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Beast(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Beast"
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Bug(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Bug"
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Humanoid(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Humanoid"
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Demon(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Demon"
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Dragon(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Dragon"
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Shifter(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        self.ID = "Shifter"
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class Boss(Enemy):
    def __init__(self, name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description):
        super().__init__(name, tier, HP, mHP, damage, statusatk, status_chance, weak, DEF, RES, SPD, SKL, LUCK, EXP, gold, part, description)

class dummy(Enemy):
    def __init__(self):
        super().__init__(
            name="Dummy",
            tier=0,
            HP=1000000,
            mHP=1000000,
            damage=0,
            statusatk=None,
            status_chance=0,
            weak=None,
            DEF=0,
            RES=0,
            SPD=0,
            SKL=0, 
            LUCK=0,
            EXP=0,
            gold=0,
            part=None,
            description="A wooden dummy. It doesn't do anything.\n"
            )
        
        self.id = "Dummy"

class testing_boss(Demon, Boss):
    def __init__(self):
        super().__init__(
            name="Mega Demon",
            tier='Boss',
            HP=1000,
            mHP=1000,
            damage=150,
            statusatk=None,
            status_chance=0,
            weak=None,
            DEF=80,
            RES=80,
            SPD=80,
            SKL=50,
            LUCK=40,
            EXP=100,
            gold=0,
            part=None,
            description="The Mega Demon, a powerful foe for any adventurer to face."
            )

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
        super().__init__(
            name="Giant Spider",
            tier=1,
            HP=10,
            mHP=10,
            damage=2,
            statusatk=None,
            status_chance=0,
            weak=None,
            DEF=0,
            RES=1,
            SPD=3,
            SKL=2,
            LUCK=1,
            EXP=13,
            gold=10,
            part=items.spider_leg(1),
            description="A large spider with dripping fangs and a hairy body.\nThey are quicker than most basic monsters. Being all buggy, its defense\nisn't superb, but it has a bit of magic resistance.\n"
            )
 
class goblin(Humanoid):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.goblin_fingernail(10),
        '3': items.amethyst(5)
    }

    def __init__(self):
        import items
        super().__init__(
            name="Goblin",
            tier=1,
            HP=5,
            mHP=5,
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
            description="A small, green humanoid with a large nose and pointed ears.\nThey aren't very special, but they have a bit of defense.\n"
            )
        self.skills.append(enemy_skills.club_smash())
        self.skills.append(enemy_skills.patch())

class skeleton(Undead):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.bone(10),
        '3': items.opal(5)
    }

    def __init__(self):
        import items
        super().__init__(
            name="Skeleton",
            tier=1,
            HP=7, 
            mHP=7, 
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
        super().__init__(
            name="Large Rat",
            tier=1,
            HP=15,
            mHP=10,
            damage=3,
            statusatk="Disease",
            status_chance=30,
            weak="Fire",
            DEF=1,
            RES=1,
            SPD=1, 
            SKL=0,
            LUCK=0,
            EXP=15,
            gold=15,
            part=items.rat_tail(1),
            description="An incredibly large rat.\nThey aren't hard tp hurt, but their thick hide and hard teeth give them\ndecent health and damage.\n"
            )

class demon_bat(Demon):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.stone(10),
        '3': items.ruby(5)
    }

    def __init__(self):
        import items
        super().__init__(
            name="Demon Bat",
            tier=1,
            HP=4,
            mHP=4,
            damage=2,
            statusatk=None,
            status_chance=0,
            weak="Holy",
            DEF=0,
            RES=3,
            SPD=4,
            SKL=3,
            LUCK=1,
            EXP=12,
            gold=9,
            part=items.bat_wing(1),
            description="A bat with red eyes and a demonic aura. \nThey are quick and have a bit of magic resistance, but physically weak.\n"
            )
        
class zombie(Undead):
    import items
    steal_list = {
        '1': items.gold(100),
        '2': items.wood_plank(10),
        '3': items.amethyst(5)
    }

    def __init__(self):
        import items
        super().__init__(
            name="Zombie",
            tier=1,
            HP=15,
            mHP=15,
            damage=3,
            statusatk="Disease",
            status_chance=45,
            weak=None,
            DEF=2,
            RES=2,
            SPD=1,
            SKL=0,
            LUCK=0,
            EXP=20,
            gold=20,
            part=items.rotting_flesh(1),
            description="A walking corpse.\nThey are slow, but they have some defense and deal a little more damage.\nIt is important to strike them down quickly to avoid being afflicted\nwith DISEASE.\n"
            )

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
        super().__init__(
            name="Underking",
            tier="Boss",
            HP=200,
            mHP=200,
            damage=50, 
            statusatk="Wither",
            status_chance=70,
            weak="Holy",
            DEF=15,
            RES=20,
            SPD=18,
            SKL=35,
            LUCK=10,
            EXP=100,
            gold=3000,
            part=items.obsidian_blade(),
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
        super().__init__(
            name="Centipede",
            tier="Boss",
            HP=20,
            mHP=20,
            damage=5,
            statusatk="Poison",
            status_chance=50,
            weak="Fire",
            DEF=3,
            RES=2,
            SPD=5,
            SKL=4,
            LUCK=2,
            EXP=50,
            gold=30,
            part=items.centipede_carapace(1),
            description="A giant centipede, with acid dripping off its mandibles. There also \nappears to be several old weapons stuck in its hard shell. Being a \ncentipede, it is quite dangerous, with high damage, some defense both \nphysically and magically, quick, and capable of making skillful \nstrikes. Only engage when you are ready.\n"
            )
        
# F1 Boss

# F2 Boss

# F3 Boss

# F4 Boss

# F5 Boss
