import sys, time, random, items

# This module contains functions that are used in multiple files.

# This function is used to print text one character at a time.
# It takes two arguments: the text to be printed, and the speed at which to print it.
def text_speed(text, speed):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(speed)


# Combat Utilities

# This functions is used in combat to determine if the attack is a critical hit.
def chk_CRIT(object):
    return random.randint(1,100) <= ((object.SKL*2) + object.LUCK)

def chk_weakness(target):
    weakness = None
    if target.weak != None:
        weakness = target.weak
        return weakness
    else:
        return weakness
    
def calculate_hit(attacker, defender):
    if attacker.status['blind'] == True:
        Hit_rate = 100 + ((attacker.SKL + attacker.LUCK) - defender.AVO) - 20
        return random.randint(1,100) <= Hit_rate
    Hit_rate = 100 + ((attacker.SKL + attacker.LUCK) - defender.AVO)
    return random.randint(1,100) <= Hit_rate

def skill_hit(skill, attacker, defender):
    if attacker.status['blind'] == True:
        Hit_rate = skill.hit_rate + ((attacker.SKL + attacker.LUCK) - defender.AVO) - 20
        return random.randint(1,100) <= Hit_rate
    Hit_rate = skill.hit_rate + ((attacker.SKL + attacker.LUCK) - defender.AVO)
    return random.randint(1,100) <= Hit_rate

def generate_damage(player, stat, attack, enemy):
    eweak = chk_weakness(enemy)
    if player.equipped['weapon'].damage_type == eweak:
        text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
        return random.randrange(stat + attack, stat + (attack * 2))
    else:
        return random.randrange(stat, stat + attack)
    
def generate_magic_damage(player, spell, enemy):
    eweak = chk_weakness(enemy)
    spellcaster = player.equipped['weapon']
    if isinstance(spellcaster, items.Spellcaster):
        base = spellcaster.mdamage + player.MAG
        if spell.damage_type == eweak:
            text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
            return random.randrange(base + spell.damage, base + (spell.damage * 2))
        else:
            return random.randrange(base, base + spell.damage)
    else:
        if spell.damage_type == eweak:
            text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
            return random.randrange(player.MAG + spell.damage, player.MAG + (spell.damage * 2))
        else:
            return random.randrange(player.MAG, player.MAG + spell.damage)