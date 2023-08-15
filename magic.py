from utilities import *
import enemies

'''
Damage damage_types
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

Status Effects
    Poison
    Paralysis
    Blind
    Silence
    Sleep
    Confusion
    Charm
    Crippled
'''

class Spell:
    def __init__(self, name, description, cost, damage, damage_type):
        self.name = name
        self.description = description
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
    
    def __str__(self):
        return '{}\n====================\n{}\nMP: {}\nDamage: {}\nType: {}'.format(self.name, self.description, self.cost, self.damage, self.damage_type)
    
    def __repr__(self):
        return self.name
    
    def effect(self, player, enemy):
        raise NotImplementedError()
    
    def cast_spell(self, player, enemy):
        if player.stats['cMP'] >= self.cost:
            player.stats['cMP'] -= self.cost
            self.effect(player, enemy)
    
# Basic Spells

class fire(Spell):
    def __init__(self):
        super().__init__(name="Fire", cost=2, damage=5, damage_type="Fire", 
                         description="Shoots a steam of flames. Deals Fire damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.stats['HP']), .03)
            time.sleep(.2)
        
class ice(Spell):
    def __init__(self):
        super().__init__(name="Ice", cost=2, damage=5, damage_type="Cold", 
                         description="Sends out shards of ice. Deals Cold damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class shock(Spell):
    def __init__(self):
        super().__init__(name="Shock", cost=2, damage=5, damage_type="Lightning", 
                         description="Spouts electricity from your fingertips. Deals Lightning damage \nto a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class water(Spell):
    def __init__(self):
        super().__init__(name="Water", cost=2, damage=5, damage_type="Water", 
                         description="Fire a stream of pressurized water. Deals Water damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class quake(Spell):
    def __init__(self):
        super().__init__(name="Quake", cost=2, damage=5, damage_type="Earth", 
                         description="Makes the ground tremble. Deals Earth damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class wind(Spell):
    def __init__(self):
        super().__init__(name="Wind", cost=2, damage=5, damage_type="Wind", 
                         description="Moves the air around you like blades. Deals Wind damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class smite(Spell):
    def __init__(self):
        super().__init__(name="Smite", cost=2, damage=5, damage_type="Holy", 
                         description="Calls forth heavenly judgement in a column of light. Deals \nHoly damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class curse(Spell):
    def __init__(self):
        super().__init__(name="Curse", cost=2, damage=5, damage_type="Demonic", 
                         description="Sends demonic energy from the shadows to curse your enemies. \nDeals Demonic damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class wither(Spell):
    def __init__(self):
        super().__init__(name="Wither", cost=6, damage=5, damage_type="Necrotic", 
                         description="Shoots a purple bolt of nectrotic energy that atrophies your enemies. \nDeals Necrotic damage to a single target. Has a chance to Cripple the target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = (((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2) + 5)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy) + 5
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if random.randint(1,100) <= 55:
                enemy.status['crippled'] = True
                text_speed("The {} is crippled!\n".format(enemy.name), .03)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            text_speed("The {} has {} HP remaining.\n".format(enemy.name, enemy.stats['HP']), .03)
            time.sleep(.2)
        
class poison(Spell):
    def __init__(self):
        super().__init__(name="Poison", cost=2, damage=3, damage_type="Poison", 
                         description="Shoots a thin, green bolt. Deals Poison damage to a single target. \nHas a chance to Poison the target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            time.sleep(.2)
            if cCRIT == True:
                pdamage *= 2
                text_speed("Critical hit!\n", .01)
                time.sleep(.2)
            if (pdamage - enemy.stats['RES']) < 0:
                damage = 1
            else:
                damage = (pdamage - enemy.stats['RES'])
            text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
            time.sleep(.2)
            enemy.stats['HP'] -= damage
            if random.randint(1,100) <= 95:
                enemy.status['poison'] = True
                text_speed("The {} is poisoned!\n".format(enemy.name), .03)
                time.sleep(.2)
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class turn(Spell):
    def __init__(self):
        super().__init__(name="Turn Undead", cost=2, damage=5, damage_type="Holy", 
                         description="Your hands glow and burn away the undead. Deals damage to a single target. \nDeals tremendous damage to undead creatures.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = (((player.stats['MAG'] + player.statbonus['MAG']['value']) * 2) + 5)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            pdamage = generate_magic_damage(player, stat_bonus, self, enemy)
            if isinstance(enemy, enemies.Undead):
                pdamage *= 2
                text_speed("The {} burns from the holy energy!\n".format(enemy.name), .03)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - enemy.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - enemy.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
                time.sleep(.2)
                enemy.stats['HP'] -= damage
            elif isinstance(enemy, enemies.Undead) == False: 
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - enemy.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - enemy.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, enemy.name), .03)
                time.sleep(.2)
                enemy.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)