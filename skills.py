from utilities import *

class Skill:
    def __init__(self, name, description, cost, damage, damage_type, bonus_stat, hit_rate):
        self.name = name
        self.description = description
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.bonus_stat = bonus_stat
        self.hit_rate = hit_rate

    def __str__(self):
        return '{}\n====================\n{}\nMP: {}\nDamage: {}\nType: {}'.format(self.name, self.description, self.cost, self.damage, self.damage_type)
    
    def __repr__(self):
        return self.name
    
    def ability(self, player, enemy):
        raise NotImplementedError()
    
    def use_ability(self, player, enemy):
        if player.cMP >= self.cost:
            player.cMP -= self.cost
            self.ability(player, enemy)
    
# Basic Skills

class cleave(Skill):
    def __init__(self):
        super().__init__(name="Cleave", cost=5, damage=5, damage_type="", bonus_stat="STR", hit_rate=85,
                         description="Your Cleave skill. Deals damage to a single target. Deals extra damage based on your STR.")
        
    def ability(self, player, enemy):
        if skill_hit(self, player, enemy):
            cCRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            stat_bonus = (player.STR * 2)
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = player.generate_damage(stat_bonus, base_dmg, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            text_speed("You dealt {} damage to the {}.\n".format(pdamage, enemy.name), .03)
            time.sleep(.2)
            enemy.hp -= (pdamage - enemy.DEF)
        else:
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)

class sneak_attack(Skill):
    def __init__(self):
        super().__init__(name="Sneak Attack", cost=5, damage=5, damage_type="", bonus_stat="SKL", hit_rate=90,
                         description="Your Sneak Attack skill. Deals damage to a single target. Deals extra damage based on your SKL.")
        
class precision_strike(Skill):
    def __init__(self):
        super().__init__(name="Precision Strike", cost=5, damage=5, damage_type="", bonus_stat="SKL", hit_rate=100,
                         description="Your Precision Strike skill. Deals damage to a single target. \nThis attack always hits. Deals extra damage based on your SKL.")
        
class double_strike(Skill):
    def __init__(self):
        super().__init__(name="Double Strike", cost=5, damage=5, damage_type="", bonus_stat="SPD", hit_rate=70,
                         description="Your Double Strike skill. Deals damage to a single target. If your SPD is higher than the enemy's, you attack twice.")
        
class  guard_breaker(Skill):
    def __init__(self):
        super().__init__(name="Guard Breaker", cost=5, damage=5, damage_type="", bonus_stat="", hit_rate=80,
                         description="Your Guard Breaker skill. Deals damage to a single target. Ignores enemy DEF.")