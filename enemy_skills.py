import random, time
from utilities import *

# This module is for Enemy Skills. There are four types of skills:
# 1. Attack Skills
# 2. Restore Skills
# 3. Buff Skills
# 4. Debuff Skills

class eSkill:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def ability(self, user, target):
        raise NotImplementedError()

    def use(self, user, target):
        return self.ability(user, target)

class Attack(eSkill):
    def __init__(self, name, desc, damage, damage_type, hit_rate):
        super().__init__(name, desc)
        self.damage = damage
        self.damage_type = damage_type
        self.hit_rate = hit_rate

class Restore(eSkill):
    def __init__(self, name, desc, rtype, potency):
        super().__init__(name, desc)
        self.rtype = rtype
        self.potency = potency

    def use(self, user):
        return self.ability(user)

class Buff(eSkill):
    def __init__(self, name, desc, buff, potency):
        super().__init__(name, desc)
        self.buff = buff
        self.potency = potency

class Debuff(eSkill):
    def __init__(self, name, desc, debuff, potency):
        super().__init__(name, desc)
        self.debuff = debuff
        self.potency = potency

# Tier 1 Monster Skills

# Goblin Skills
class club_smash(Attack):
    def __init__(self):
        super().__init__(name='Club Smash', desc='A basic attack with a club.', damage=3, damage_type = '', hit_rate = 80)

    def ability(self, user, target):
        text_speed("The {} used {}!\n".format(user.name, self.name), .03)
        time.sleep(.2)
        if eskill_hit(self, user, target):
            time.sleep(.2)
            ecrit = chk_CRIT(user, target)
            edamage = generate_eskill_damage(user, user.damage, self.damage)
            if ecrit:
                text_speed("Critical hit!\n", .01)
                time.sleep(.05)
                edamage *= 2
            parmor = target.chk_armor()
            if target.buffs['physical_resist']:
                damage = round(edamage - (edamage * parmor) - (edamage * target.buffs['physical_resist']['potency']))
            else:
                damage = round(edamage - (edamage * parmor))
            if damage <= target.stats['DEF']['value']:
                damage = 1
            else:
                damage = damage - target.stats['DEF']['value']
            target.stats['cHP']['value'] -= damage
            text_speed("The {} dealt {} damage to you!\n".format(user.name, damage), .03)
            time.sleep(.2)
        else:
            text_speed("{} missed!\n".format(user.name), .03)
            time.sleep(.2)

class patch(Restore):
    def __init__(self):
        super().__init__(name='Patch', desc='Let\'\s put a bandaid on that wound.', rtype='Heal', potency=3)

    def ability(self, user):
        text_speed("The {} used {}!\n".format(user.name, self.name), .03)
        time.sleep(.2)
        if self.potency + user.stats['HP'] > user.stats['mHP']:
            user.stats['HP'] = user.stats['mHP']
        else:
            user.stats['HP'] += self.potency
        text_speed("The {} patched itself up!\n".format(user.name), .03)
        time.sleep(.2)
        text_speed("The {} recovered {} HP!\n".format(user.name, self.potency), .03)
        time.sleep(.2)