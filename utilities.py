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
def chk_CRIT(attacker, target):
    crit = (attacker.stats['SKL'] + attacker.stats['LUCK']) - target.stats['LUCK']
    return random.randint(1,100) <= crit

def chk_weakness(target):
    if target.weak:
        return target.weak
    
def calculate_hit(attacker, defender):
    if attacker.status['blind'] == True:
        Hit_rate = 100 + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO()) - 20
        return random.randint(1,100) <= Hit_rate
    Hit_rate = 100 + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO())
    return random.randint(1,100) <= Hit_rate

def skill_hit(skill, attacker, defender):
    if attacker.status['blind'] == True:
        Hit_rate = skill.hit_rate + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO()) - 20
        return random.randint(1,100) <= Hit_rate
    Hit_rate = skill.hit_rate + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO())
    return random.randint(1,100) <= Hit_rate

def scroll_hit(scroll, defender):
    Hit_rate = scroll.accuracy - defender.AVO()
    return random.randint(1,100) <= Hit_rate

def generate_damage(player, stat, attack, enemy):
    eweak = chk_weakness(enemy)
    if player.equipped['weapon'].damage_type == eweak:
        text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
        return random.randrange(stat + attack, stat + (attack * 2))
    else:
        return random.randrange(stat, stat + attack)
    
def generate_skill_damage(player, skill, stat, damage, enemy):
    eweak = chk_weakness(enemy)
    print(damage)
    if player.equipped['weapon'].damage_type == eweak or skill.damage_type == eweak:
        text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
        return random.randrange(stat + damage, stat + (damage * 2))
    else:
        return random.randrange(stat, stat + damage)

def generate_magic_damage(player, stat, spell, enemy):
    eweak = chk_weakness(enemy)
    spellcaster = player.equipped['weapon']
    if isinstance(spellcaster, items.Spellcaster):
        base = spellcaster.mdamage + stat
        sdamage = spell.damage + spellcaster.mdamage
        if spell.damage_type == eweak:
            text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
            return random.randrange(base + sdamage, base + (sdamage * 2))
        else:
            return random.randrange(base, base + sdamage)
    else:
        sdamage = spell.damage
        if spell.damage_type == eweak:
            text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
            return random.randrange(stat + sdamage, stat + (sdamage * 2))
        else:
            return random.randrange(stat, stat + sdamage)
        
def generate_scroll_damage(scroll, enemy):
    eweak = chk_weakness(enemy)
    if scroll.damage_type == eweak:
        text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
        return random.randrange(scroll.damage * 1.5, scroll.damage * 3)
    else:
        return random.randrange(scroll.damage, scroll.damage * 2)