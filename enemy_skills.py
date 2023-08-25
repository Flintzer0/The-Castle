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

    def __repr__(self):
        return self.name

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
    def __init__(self, name, desc, debuff, potency, hit_rate):
        super().__init__(name, desc)
        self.debuff = debuff
        self.potency = potency
        self.hit_rate = hit_rate

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
                damage = edamage - target.stats['DEF']['value']
            target.stats['cHP']['value'] -= damage
            text_speed("The {} dealt {} damage to you!\n".format(user.name, damage), .03)
            time.sleep(.2)
            user.apply_poison()
        else:
            text_speed("{} missed!\n".format(user.name), .03)
            time.sleep(.2)
            user.apply_poison()

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
        user.apply_poison()

# Spider Skills

class venom(Debuff):
    def __init__(self):
        super().__init__(name='Venom', desc='A poisonous bite.', debuff='poison', potency=2, hit_rate=80)

    def ability(self, user, target):
        text_speed("The {} used {}!\n".format(user.name, self.name), .03)
        time.sleep(.2)
        if eskill_hit(self, user, target):
            time.sleep(.2)
            vdamage = round(1 + (1 * (user.tier / 10)))
            target.stats['cHP']['value'] -= vdamage
            text_speed("The {} dealt {} damage to you!\n".format(user.name, vdamage), .03)
            if chance((self.hit_rate*(self.hit_rate / 100))):
                if target.status['poison']['flag'] == False:
                    target.status['poison']['flag'] = True
                    target.status['poison']['potency'] = self.potency
                    text_speed("You were poisoned!\n", .03)
                    time.sleep(.2)
            user.apply_poison()
        else:
            text_speed("The {} missed!\n".format(user.name), .03)
            time.sleep(.2)
            user.apply_poison()

class web(Debuff):
    def __init__(self):
        super().__init__(name='Web', desc='A sticky web.', debuff='slowed', potency=1, hit_rate=80)

    def ability(self, user, target):
        text_speed("The {} used {}!\n".format(user.name, self.name), .03)
        time.sleep(.2)
        if eskill_hit(self, user, target):
            time.sleep(.2)
            if target.status['slowed']['flag'] == False:
                target.status['slowed']['flag'] = True
                target.status['slowed']['potency'] = self.potency
                text_speed("You were slowed!\n", .03)
                time.sleep(.2)
            user.apply_poison()
        else:
            text_speed("The {} missed!\n".format(user.name), .03)
            time.sleep(.2)
            user.apply_poison()

# Demon Bat Skills

class drain(Attack):
    def __init__(self):
        super().__init__(name='Drain', desc='A draining bite.', damage=2, damage_type = '', hit_rate = 80)

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
                damage = edamage - target.stats['DEF']['value']
            target.stats['cHP']['value'] -= damage
            recover = round(damage / 2)
            if user.stats['cHP']['value'] + recover > user.stats['mHP']:
                user.stats['cHP']['value'] = user.stats['mHP']
            else:
                user.stats['cHP']['value'] += recover
            text_speed("The {} dealt {} damage to you!\n".format(user.name, damage), .03)
            time.sleep(.2)
            text_speed("The {} recovered {} HP!\n".format(user.name, recover), .03)
            time.sleep(.2)
            user.apply_poison()
        else:
            text_speed("The {} missed!\n".format(user.name), .03)
            time.sleep(.2)
            user.apply_poison()