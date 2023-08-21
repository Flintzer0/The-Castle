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
    def __init__(self, name, description, cost):
        self.name = name
        self.description = description
        self.cost = cost
    
    def __str__(self):
        return '{}\n====================\n{}\nMP: {}'.format(self.name, self.description, self.cost)
    
    def __repr__(self):
        return self.name
    
    def effect(self, player, enemy):
        raise NotImplementedError()
    
    def cast_spell(self, player, enemy):
        if player.stats['cMP']['value'] >= self.cost:
            player.stats['cMP']['value'] -= self.cost
            self.effect(player, enemy)

class Damage(Spell):
    def __init__(self, name, description, cost, damage, damage_type):
        self.damage = damage
        self.damage_type = damage_type
        super().__init__(name, description, cost)

class Restore(Spell):
    def __init__(self, name, description, cost, rtype, potency):
        self.rtype = rtype
        self.potency = potency
        super().__init__(name, description, cost)

class Buff(Spell):
    def __init__(self, name, description, cost, buff, potency, duration):
        self.buff = buff
        self.potency = potency
        self.duration = duration
        super().__init__(name, description, cost)

class Debuff(Spell):
    def __init__(self, name, description, cost, debuff, potency, duration):
        self.debuff = debuff
        self.potency = potency
        self.duration = duration
        super().__init__(name, description, cost)

# Basic Damaging Spells

class fire(Damage):
    def __init__(self):
        super().__init__(name="Fire", cost=2, damage=5, damage_type="Fire", 
                         description="Shoots a steam of flames. Deals Fire damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class ice(Damage):
    def __init__(self):
        super().__init__(name="Ice", cost=2, damage=5, damage_type="Cold", 
                         description="Sends out shards of ice. Deals Cold damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class shock(Damage):
    def __init__(self):
        super().__init__(name="Shock", cost=2, damage=5, damage_type="Lightning", 
                         description="Spouts electricity from your fingertips. Deals Lightning damage \nto a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class water(Damage):
    def __init__(self):
        super().__init__(name="Water", cost=2, damage=5, damage_type="Water", 
                         description="Fire a stream of pressurized water. Deals Water damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class quake(Damage):
    def __init__(self):
        super().__init__(name="Quake", cost=2, damage=5, damage_type="Earth", 
                         description="Makes the ground tremble. Deals Earth damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class wind(Damage):
    def __init__(self):
        super().__init__(name="Wind", cost=2, damage=5, damage_type="Wind", 
                         description="Moves the air around you like blades. Deals Wind damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class smite(Damage):
    def __init__(self):
        super().__init__(name="Smite", cost=2, damage=5, damage_type="Holy", 
                         description="Calls forth heavenly judgement in a column of light. Deals \nHoly damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class curse(Damage):
    def __init__(self):
        super().__init__(name="Curse", cost=2, damage=5, damage_type="Demonic", 
                         description="Sends demonic energy from the shadows to curse your enemies. \nDeals Demonic damage to a single target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
        
class wither(Damage):
    def __init__(self):
        super().__init__(name="Wither", cost=6, damage=5, damage_type="Necrotic", 
                         description="Shoots a purple bolt of nectrotic energy that atrophies your enemies. \nDeals Necrotic damage to a single target. Has a chance to Cripple the target.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = (((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2) + 5)
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
        
class poison_dart(Damage, Debuff):
    def __init__(self):
        name = "Poison Dart"
        description = "Shoots a bolt of magical poison. Deals Poison damage to a single target. \nHas a chance to Poison the target."
        cost = 2
        damage = 3
        damage_type = "Poison"
        debuff = "poison"
        potency = 5
        duration = 3
        self.name = name
        self.description = description
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
        self.debuff = debuff
        self.potency = potency
        self.duration = duration
        Damage(name, description, cost, damage, damage_type).__init__(name, description, cost, damage, damage_type)
        Debuff(name, description, cost, debuff, potency, duration).__init__(name, description, cost, debuff, potency, duration)

    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = ((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2)
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
                enemy.status['poison']['flag'] = True
                enemy.status['poison']['potency'] = self.potency
                text_speed("The {} is poisoned!\n".format(enemy.name), .03)
                time.sleep(.2)
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)
        
class turn(Damage):
    def __init__(self):
        super().__init__(name="Turn Undead", cost=2, damage=5, damage_type="Holy", 
                         description="Your hands glow and burn away the undead. Deals damage to a single target. \nDeals tremendous damage to undead creatures.")
        
    def effect(self, player, enemy):
        if calculate_hit(player, enemy):
            cCRIT = chk_CRIT(player, enemy)
            stat_bonus = (((player.stats['MAG']['value'] + player.statbonus['MAG']['value']) * 2) + 5)
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

# Basic Restore Spells

class pheal(Restore):
    def __init__(self):
        super().__init__(name="Heal", cost=2, rtype="Heal", potency=5, 
                         description="Heals the user for a small amount of HP. Heal amount increases with RES.")
        
    def effect(self, player):
        if player.stats['cHP']['value'] < player.stats['mHP']['value']:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            heal = self.potency + ((self.potency * (player.stats['RES']['value']) / 100))
            player.stats['cHP']['value'] += heal
            if player.stats['cHP']['value'] > player.stats['mHP']['value']:
                player.stats['cHP']['value'] = player.stats['mHP']['value']
            text_speed("You healed yourself for {} HP.\n".format(heal), .03)
            time.sleep(.2)
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You are already at full HP!\n", .03)
            time.sleep(.2)

class eheal(Restore):
    def __init__(self):
        super().__init__(name="Heal", cost=2, rtype="Heal", potency=5, 
                         description="Heals the user for a small amount of HP. Heal amount increases with RES.")
        
    def effect(self, enemy):
        text_speed("The {} cast {}!\n".format(enemy.name, self.name), .03)
        time.sleep(.2)
        heal = self.potency + ((self.potency * (enemy.stats['RES']) / 100))
        if heal + enemy.stats['HP'] > enemy.stats['mHP']['value']:
            enemy.stats['HP'] = enemy.stats['mHP']['value']
        else:
            enemy.stats['HP'] += heal
        text_speed("The {} healed itself for {} HP.\n".format(enemy.name, heal), .03)
        time.sleep(.2)