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

class giant_spider(Enemy):
    def __init__(self):
        super().__init__(name="Giant Spider", hp=10, mhp=10, damage=2, DEF=0, RES=1, SPD=3, SKL=2, LUCK=1, EXP=25, gold=5,
                         description="A large spider with dripping fangs and a hairy body. They are quicker than most basic monsters. \nBeing all buggy, its defense isn't superb, but it has a bit of magic resistance.")
 
class goblin(Enemy):
    def __init__(self):
        super().__init__(name="Goblin", hp=5, mhp=5, damage=1, DEF=1, RES=0, SPD=2, SKL=1, LUCK=0, EXP=15, gold=3,
                         description="A small, green humanoid with a large nose and pointed ears. \nThey aren't very special, but they have a bit of defense.")

class skeleton(Enemy):
    def __init__(self):
        super().__init__(name="Skeleton", hp=7, mhp=7, damage=3, DEF=2, RES=-1, SPD=1, SKL=0, LUCK=0, EXP=40, gold=4,
                         description="A walking skeleton. \nThey are slow, but they have a bit of defense and deal a little more damage.")