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
        super().__init__(name="Cleave", cost=2, damage=5, damage_type="", bonus_stat="STR", hit_rate=85,
                         description="Your Cleave skill. Deals damage to a single target. Deals extra damage based on your STR.")
        
    def ability(self, player, enemy):
        if skill_hit(self, player, enemy):
            cCRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            stat_bonus = (player.STR * 2)
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, stat_bonus, base_dmg, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.DEF) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.DEF)
            text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
            enemy.hp -= damage
        else:
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.hp), .03)
            time.sleep(.2)

class sneak_attack(Skill):
    def __init__(self):
        super().__init__(name="Sneak Attack", cost=4, damage=5, damage_type="", bonus_stat="SKL", hit_rate=90,
                         description="Your Sneak Attack skill. Deals damage to a single target. Deals extra damage based on your SKL.")
        
    def ability(self, player, enemy):
        if skill_hit(self, player, enemy):
            cCRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            stat_bonus = (player.SKL * 2)
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, stat_bonus, base_dmg, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.DEF) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.DEF)
            text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
            enemy.hp -= damage
        else:
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.hp), .03)
            time.sleep(.2)
        
class precision_strike(Skill):
    def __init__(self):
        super().__init__(name="Precision Strike", cost=6, damage=7, damage_type="", bonus_stat="SKL", hit_rate=100,
                         description="Your Precision Strike skill. Deals damage to a single target. \nThis attack always hits. Deals extra damage based on your SKL.")
        
    def ability(self, player, enemy):
        cCRIT = chk_CRIT(player)
        weapon = player.equipped['weapon']
        stat_bonus = (player.SKL * 2)
        base_dmg = (self.damage + weapon.damage)
        text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
        pdamage = generate_damage(player, stat_bonus, base_dmg, enemy)
        time.sleep(.2)
        if cCRIT == True:
            pdamage *= 2
            text_speed("Critical hit!\n", .01)
            time.sleep(.2)
        if (pdamage - enemy.DEF) < 0:
            damage = 1
        else:
            damage = (pdamage - enemy.DEF)
        text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
        enemy.hp -= damage
        
class double_strike(Skill):
    def __init__(self):
        super().__init__(name="Double Strike", cost=5, damage=4, damage_type="", bonus_stat="SPD", hit_rate=70,
                         description="Your Double Strike skill. Deals damage to a single target. Has a chance to hit twice based on SPD.")

    def ability(self, player, enemy):
        if skill_hit(self, player, enemy):
            CRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, player.SPD, base_dmg, enemy)
            time.sleep(.2)
            if CRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.DEF) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.DEF)
            text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
            enemy.hp -= damage
            self.second_hit(player, enemy)

    def second_hit(self, player, enemy):
        second_hit = random.randint(1,100) <= 50 + (player.SPD * 2)
        if second_hit == True:
            text_speed("You hit the {} again!\n".format(enemy.name), .03)
            time.sleep(.2)
            CRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, player.SPD, base_dmg, enemy)
            time.sleep(.2)
            if CRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.DEF) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.DEF)
            text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
            enemy.hp -= damage
        
class guard_breaker(Skill):
    def __init__(self):
        super().__init__(name="Guard Breaker", cost=7, damage=5, damage_type="", bonus_stat="", hit_rate=80,
                         description="Your Guard Breaker skill. Deals damage to a single target. Ignores enemy DEF.")
        
    def ability(self, player, enemy):
        if skill_hit(self, player, enemy):
            cCRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, player.STR, base_dmg, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            text_speed("You dealt {} damage to the {}.\n".format(pdamage, enemy.name), .03)
            time.sleep(.2)
            enemy.hp -= pdamage
        else:
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.hp), .03)
            time.sleep(.2)
        
class heavy_swing(Skill):
    def __init__(self):
        super().__init__(name="Heavy Swing", cost=3, damage=10, damage_type="Earth", bonus_stat="STR", hit_rate=65,
                         description="Your Heavy Swing skill. Has a low hit-rate, but can deal high Earth damage to a single target.")
        
    def ability(self, player, enemy):
        weapon = player.equipped['weapon']
        if skill_hit(self, player, enemy):
            cCRIT = chk_CRIT(player)
            stat_bonus = (player.STR * 2)
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, stat_bonus, base_dmg, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.DEF) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.DEF)
            text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
            enemy.hp -= damage
        else:
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.hp), .03)
            time.sleep(.2)
        
class steal(Skill):
    def __init__(self):
        super().__init__(name="Steal", cost=1, damage=1, damage_type="", bonus_stat="SPD", hit_rate=90,
                         description="Your Steal skill. Deals damage to a single target. Has a chance to steal from enemies based on SPD.")
        
    def ability(self, player, enemy):
        if skill_hit(self, player, enemy):
            cCRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, player.SPD, base_dmg, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.DEF) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.DEF)
            text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
            enemy.hp -= damage
            self.steal(player, enemy)
        else:
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.hp), .03)
            time.sleep(.2)

    def steal(self, player, enemy):
        steal = random.randint(1,100) <= 50 + (player.SPD * 2)
        if steal == True:
            item_choice = random.randint(1,100)
            if item_choice <= 50:
                gold = enemy.steal_list['1']
                amount = random.randint(1, 20)
                player.cash += amount
                enemy.steal_list['1'].amt -= amount
                text_speed("You stole {} gold!\n".format(amount), .03)
                time.sleep(.2)
            elif item_choice <= 85:
                item = enemy.steal_list['2']
                player.inventory.append(item)
                text_speed("You stole a {}!\n".format(item.name), .03)
                time.sleep(.2)
            elif item_choice <= 100:
                item = enemy.steal_list['3']
                player.inventory.append(item)
                text_speed("You stole a {}!\n".format(item.name), .03)
                time.sleep(.2)
        else:
            text_speed("You failed to steal an item from the {}!\n".format(enemy.name), .03)
            time.sleep(.2)
        
class poison_point(Skill):
    def __init__(self):
        super().__init__(name="Poison Point", cost=3, damage=2, damage_type="Poison", bonus_stat="SKL", hit_rate=85,
                         description="Your Poison Point skill. Deals damage based on SKL to a single target. Has a high chance to poison enemies.")
        
    def ability(self, player, enemy):
        if skill_hit(self, player, enemy):
            cCRIT = chk_CRIT(player)
            weapon = player.equipped['weapon']
            stat_bonus = (player.SKL * 2)
            base_dmg = (self.damage + weapon.damage)
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            pdamage = generate_damage(player, stat_bonus, base_dmg, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.DEF) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.DEF)
            text_speed("You dealt {} damage to the {}.\n".format(damage, enemy.name), .03)
            enemy.hp -= damage
            self.poison(player, enemy)
        else:
            text_speed("You use {} with your {}!\n".format(self.name, weapon.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.hp), .03)
            time.sleep(.2)

    def poison(self, player, enemy):
        poison = random.randint(1,100) <= 60 + (player.SKL * 2)
        if poison == True:
            text_speed("You poisoned the {}!\n".format(enemy.name), .03)
            time.sleep(.2)
            enemy.status['poison'] = True
        else:
            text_speed("You failed to poison the {}!\n".format(enemy.name), .03)
            time.sleep(.2)
        
class wind_shot(Skill):
    def __init__(self):
        super().__init__(name="Wind Shot", cost=4, damage=3, damage_type="Wind", bonus_stat="SKL", hit_rate=90,
                         description="Your Wind Shot skill. Deals Wind damage based on SKL to a single target. High crit rate. Must be wielding a bow.")
        
class retribution(Skill):
    def __init__(self):
        super().__init__(name="Retribution", cost=4, damage=6, damage_type="Holy", bonus_stat="HP", hit_rate=90,
                         description="Your Retribution skill. Deals Holy damage based on damage received to a single target.")