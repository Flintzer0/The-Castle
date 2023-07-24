class Skill:
    def __init__(self, name, description, cost, damage, damage_type, bonus_stat):
        self.name = name
        self.description = description
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.bonus_stat = bonus_stat

    def __str__(self):
        return '{}\n====================\n{}\nMP: {}\nDamage: {}\nType: {}'.format(self.name, self.description, self.cost, self.damage, self.damage_type)
    
# Basic Skills

class cleave(Skill):
    def __init__(self):
        self.bonus_stat = "STR"
        super().__init__(name="Cleave", cost=5, damage=5, damage_type="", 
                         description="Your Cleave skill. Deals damage to a single target. Deals extra damage based on your STR.")
        
class sneak_attack(Skill):
    def __init__(self):
        self.bonus_stat = "SKL"
        super().__init__(name="Sneak Attack", cost=5, damage=5, damage_type="", 
                         description="Your Sneak Attack skill. Deals damage to a single target. Deals extra damage based on your SKL.")
        
class precision_strike(Skill):
    def __init__(self):
        self.bonus_stat = "SKL"
        super().__init__(name="Precision Strike", cost=5, damage=5, damage_type="", 
                         description="Your Precision Strike skill. Deals damage to a single target. Deals extra damage based on your SKL.")
        
class double_strike(Skill):
    def __init__(self):
        self.bonus_stat = "SPD"
        super().__init__(name="Double Strike", cost=5, damage=5, damage_type="", 
                         description="Your Double Strike skill. Deals damage to a single target. If your SPD is higher than the enemy's, you attack twice.")