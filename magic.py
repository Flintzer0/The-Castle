from utilities import *
import enemies, player, time

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
    
    def effect(self, caster, target):
        raise NotImplementedError()
    
    def cast(self, caster, target):
        if caster.stats['cMP']['value'] >= self.cost:
            caster.stats['cMP']['value'] -= self.cost
            self.effect(caster, target)

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
    def __init__(self, name, description, cost, debuff, potency, duration, dchance):
        self.debuff = debuff
        self.potency = potency
        self.duration = duration
        self.dchance = dchance
        super().__init__(name, description, cost)

# Basic Damage Spells

class fire(Damage):
    def __init__(self):
        super().__init__(name="Fire", cost=2, damage=5, damage_type="Fire", 
                         description="Shoots a steam of flames. Deals Fire damage to a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                base_dmg = (self.damage)
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
                text_speed("The {} has {} HP remaining.\n".format(target.name, target.stats['HP']), .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)    
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if damage <= 0:
                    damage = 1
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)    
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class ice(Damage):
    def __init__(self):
        super().__init__(name="Ice", cost=2, damage=5, damage_type="Cold", 
                         description="Sends out shards of ice. Deals Cold damage to a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                base_dmg = (self.damage)
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class shock(Damage):
    def __init__(self):
        super().__init__(name="Shock", cost=2, damage=5, damage_type="Lightning", 
                         description="Spouts electricity from your fingertips. Deals Lightning damage \nto a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                base_dmg = (self.damage)
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class water(Damage):
    def __init__(self):
        super().__init__(name="Water", cost=2, damage=5, damage_type="Water", 
                         description="Fire a stream of pressurized water. Deals Water damage to a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                base_dmg = (self.damage)
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class quake(Damage):
    def __init__(self):
        super().__init__(name="Quake", cost=2, damage=5, damage_type="Earth", 
                         description="Makes the ground tremble. Deals Earth damage to a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                base_dmg = (self.damage)
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class wind(Damage):
    def __init__(self):
        super().__init__(name="Wind", cost=2, damage=5, damage_type="Wind", 
                         description="Moves the air around you like blades. Deals Wind damage to a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                base_dmg = (self.damage)
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class smite(Damage):
    def __init__(self):
        super().__init__(name="Smite", cost=2, damage=5, damage_type="Holy", 
                         description="Calls forth heavenly judgement in a column of light. Deals \nHoly damage to a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class blood(Damage):
    def __init__(self):
        super().__init__(name="Blood", cost=2, damage=5, damage_type="Demonic", 
                         description="Sends blood-colored demonic energy from the shadows to damage your enemies. \nDeals Demonic damage to a single target.")

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                text_speed("You cast {}!\n".format(self.name), .03)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)

class wither(Damage, Debuff):
    
    def __init__(self):
        name="Wither",
        cost=6,
        damage=5,
        damage_type="Necrotic",
        debuff="crippled",
        potency=0,
        duration=5,
        dchance=55,
        description="Shoots a purple bolt of nectrotic energy that atrophies your enemies. \nDeals Necrotic damage to a single target. Has a chance to Cripple the target."        
        Damage(name, description, cost, damage, damage_type).__init__(name, cost, damage, damage_type, description)
        Debuff(name, description, cost, debuff, potency, duration, dchance).__init__(name, description, cost, debuff, potency, duration, dchance)
        
    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']) * 2) + 5)
                pdamage = generate_magic_damage(caster, stat_bonus, self, target) + 5
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) <= 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
                if target.status['crippled'] == False:
                    if chance(self.dchance):
                        target.status[self.debuff] = True
                        text_speed("The {} is {}!\n".format(target.name, self.debuff), .03)
                        time.sleep(.2)
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG'] * 2) + 5)
                pdamage = (generate_emagic_damage(caster, stat_bonus, self) + 5)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP'] -= damage
                if target.status['crippled'] == False:
                    if chance(self.dchance):
                        target.status[self.debuff]['flag'] = True
                        text_speed("You are {}!\n".format(self.debuff), .03)
                        time.sleep(.2)
            else:
                text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
                time.sleep(.2)
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)
        
class poison_dart(Damage, Debuff):
    def __init__(self):
        self.name = "Poison Dart"
        self.description = "Shoots a bolt of magical poison. Deals Poison damage to a single target. \nHas a chance to Poison the target."
        self.cost = 2
        self.damage = 3
        self.damage_type = "Poison"
        self.debuff = "poisoned"
        self.potency = 3
        self.duration = 5
        self.dchance = 45
        Damage(self.name, self.description, self.cost, self.damage, self.damage_type).__init__(name=self.name, description=self.description, cost=self.cost, damage=self.damage, damage_type=self.damage_type)
        Debuff(self.name, self.description, self.cost, self.debuff, self.potency, self.duration, self.dchance).__init__(name=self.name, description=self.description, cost=self.cost, debuff=self.debuff, potency=self.potency, duration=self.duration, dchance=self.dchance)

    def effect(self, caster, target):
        if isinstance(caster, player.Player):
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = ((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']))
                pdamage = generate_magic_damage(caster, stat_bonus, self, target)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
                if chance(self.dchance):
                    target.status[self.debuff]['flag'] = True
                    target.status[self.debuff]['potency'] = self.potency
                    target.status[self.debuff]['duration'] = self.duration
                    text_speed("The {} is {}!\n".format(target.name, self.debuff), .03)
                    time.sleep(.2)
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You missed!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            if calculate_hit(caster, target):
                cCRIT = chk_CRIT(caster, target)
                stat_bonus = (caster.damage * 2)
                pdamage = generate_emagic_damage(caster, stat_bonus, self)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                parmor = target.chk_marmor()
                if target.buffs['magical_resist']['flag'] == True:
                    damage = round(pdamage - (pdamage * parmor) - (pdamage * target.buffs['magical_resist']['potency']))
                else:
                    damage = round(pdamage - (pdamage * parmor))
                if (pdamage - target.stats['RES']['value']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES']['value'])
                text_speed("The {} dealt {} {} damage to you.\n".format(caster.name, damage, self.damage_type), .03)
                time.sleep(.2)
                target.stats['cHP']['value'] -= damage
                if chance(self.dchance):
                    target.status[self.debuff]['flag'] = True
                    target.status[self.debuff]['potency'] = self.potency
                    target.status[self.debuff]['duration'] = self.duration
                    text_speed("You are {}!\n".format(self.debuff), .03)
                    time.sleep(.2)
            else:
                text_speed("The {} missed!\n".format(caster.name), .03)
                time.sleep(.2)
        
class turn(Damage):
    def __init__(self):
        super().__init__(name="Turn Undead", cost=2, damage=5, damage_type="Holy", 
                         description="Your hands glow and burn away the undead. Deals damage to a single target. \nDeals tremendous damage to undead creatures.")
        
    def effect(self, caster, target):
        if calculate_hit(caster, target):
            cCRIT = chk_CRIT(caster, target)
            stat_bonus = (((caster.stats['MAG']['value'] + caster.statbonus['MAG']['value']) * 2) + 5)
            base_dmg = (self.damage)
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            pdamage = generate_magic_damage(caster, stat_bonus, self, target)
            if isinstance(target, enemies.Undead):
                pdamage *= 2
                text_speed("The {} burns from the holy energy!\n".format(target.name), .03)
                time.sleep(.2)
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
            elif isinstance(target, enemies.Undead) == False: 
                if cCRIT == True:
                    pdamage *= 2
                    text_speed("Critical hit!\n", .01)
                    time.sleep(.2)
                if (pdamage - target.stats['RES']) < 0:
                    damage = 1
                else:
                    damage = (pdamage - target.stats['RES'])
                text_speed("You dealt {} {} damage to the {}.\n".format(damage, self.damage_type, target.name), .03)
                time.sleep(.2)
                target.stats['HP'] -= damage
        else:
            text_speed("You cast {}!\n".format(self.name), .03)
            time.sleep(.2)
            text_speed("You missed!\n", .03)
            time.sleep(.2)

# Basic Restore Spells

class heal(Restore):
    def __init__(self):
        super().__init__(name="Heal", cost=2, rtype="Heal", potency=5, 
                         description="Heals the user for a small amount of HP. Heal amount increases with RES.")
        
    def effect(self, caster):
        if isinstance(caster, player.Player):
            if caster.stats['cHP']['value'] < caster.stats['mHP']['value']:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                heal = self.potency + ((self.potency * (caster.stats['RES']['value']) / 100))
                caster.stats['cHP']['value'] += heal
                if caster.stats['cHP']['value'] > caster.stats['mHP']['value']:
                    caster.stats['cHP']['value'] = caster.stats['mHP']['value']
                text_speed("You healed yourself for {} HP.\n".format(heal), .03)
                time.sleep(.2)
            else:
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You are already at full HP!\n", .03)
                time.sleep(.2)
        elif isinstance(caster, enemies.Enemy):
            text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            heal = self.potency + ((self.potency * (caster.stats['RES']) / 100))
            if heal + caster.stats['HP'] > caster.stats['mHP']['value']:
                caster.stats['HP'] = caster.stats['mHP']['value']
            else:
                caster.stats['HP'] += heal
            text_speed("The {} healed itself for {} HP.\n".format(caster.name, heal), .03)
            time.sleep(.2)

class cure(Restore):
    def __init__(self):
        super().__init__(name="Cure", cost=2, rtype="Cure", potency=0, 
                         description="Cures the user of a single, random status ailment.")
        
    def effect(self, caster):
        debuffs = []
        for s in caster.status:
            if caster.status[s]['flag'] == True:
                debuffs.append(s)
        if len(debuffs) > 0:
            if isinstance(caster, player.Player):
                text_speed("You cast {}!\n".format(self.name), .03)
            elif isinstance(caster, enemies.Enemy):
                text_speed("The {} cast {}!\n".format(caster.name, self.name), .03)
            time.sleep(.2)
            debuff = random.choice(debuffs)
            caster.status[debuff]['flag'] = False
            if caster.status[debuff]['potency']:
                caster.status[debuff]['potency'] = 0
            if caster.status[debuff]['duration']:
                caster.status[debuff]['duration'] = 0
            if isinstance(caster, player.Player):
                text_speed("You cured yourself of {}!\n".format(debuff), .03)
            elif isinstance(caster, enemies.Enemy):
                text_speed("The {} cured itself of {}!\n".format(caster.name, debuff), .03)
            time.sleep(.2)
        else:
            if isinstance(caster, player.Player):
                text_speed("You cast {}!\n".format(self.name), .03)
                time.sleep(.2)
                text_speed("You have no status ailments to cure!\n", .03)
                time.sleep(.2)