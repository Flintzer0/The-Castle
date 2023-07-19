class Enemy:
    def __init__(self, name, hp, mhp, damage, DEF, RES, SPD, SKL, LUCK, EXP, gold, description):
        self.name = name
        self.hp = hp
        self.mhp = mhp
        self.damage = damage
        self.DEF = DEF
        self.RES = RES
        self.SPD = SPD
        self.SKL = SKL
        self.LUCK = LUCK
        self.EXP = EXP
        self.gold = gold
        self.description = description
        self.seen = False

    def __str__(self):
        return "{}\n=====\n{}\nHP: {}\nDamage: {}\nDEF: {}\nRES: {}\nSPD: {}\nSKL: {}\nLUCK: {}\n".format(self.name, self.description, self.mhp, self.damage, self.DEF, self.RES, self.SPD, self.SKL, self.LUCK)
 
    def is_alive(self):
        return self.hp > 0
    
# Tier 1 Enemies

class giant_spider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, mhp=10, damage=2, DEF=0, RES=1, SPD=3, SKL=2, LUCK=1, EXP=13, gold=10,
                         description="A large spider with dripping fangs and a hairy body. They are quicker than most basic monsters. \nBeing all buggy, its defense isn't superb, but it has a bit of magic resistance.")
 
class goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=5, mhp=5, damage=1, DEF=1, RES=0, SPD=2, SKL=1, LUCK=0, EXP=10, gold=16,
                         description="A small, green humanoid with a large nose and pointed ears, wielding a wooden club. \nThey aren't very special, but they have a bit of defense.")

class skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", hp=7, mhp=7, damage=3, DEF=2, RES=-1, SPD=1, SKL=0, LUCK=0, EXP=17, gold=13,
                         description="A walking skeleton. \nThey are slow, but they have some defense and deal a little more \ndamage.")
        
class large_rat(Enemy):
    def __init__(self):
        super().__init__(name="Large Rat", hp=15, mhp=10, damage=3, DEF=1, RES=1, SPD=1, SKL=0, LUCK=0, EXP=15, gold=15,
                         description="An incredibly large rat. They aren't hard to hit, but their thick hide and hard teeth \ngive them decent health and damage.")

class demon_bat(Enemy):
    def __init__(self):
        super().__init__(name="Demon Bat", hp=4, mhp=4, damage=2, DEF=0, RES=3, SPD=4, SKL=3, LUCK=1, EXP=12, gold=9,
                         description="A bat with red eyes and a demonic aura. \nThey are quick and have a bit of magic resistance, but physically weak.")
        
# Bosses

class giant_centipede(Enemy):
    # Basement Floor Boss
    def __init__(self): 
        super().__init__(name="Centipede", hp=20, mhp=20, damage=7, DEF=3, RES=2, SPD=5, SKL=4, LUCK=2, EXP=50, gold=30,
                         description="A giant centipede, with acid dripping off its mandibles. There also appeared to be several old weapons stuck in its hard shell. \nBeing a centipede, it is quite dangerous, with high damage, some defense both physically and magically, quick, and capable of making skillful strikes. Only engage when you are ready.")
        
