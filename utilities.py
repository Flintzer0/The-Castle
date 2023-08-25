import sys, time, random, items

# This module contains functions that are used in multiple files.

# This function is used to print text one character at a time.
# It takes two arguments: the text to be printed, and the speed at which to print it.
def text_speed(text, speed):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(speed)

# This function is used for all percentage-based chances.
# It takes the rate given, rolls twice, and only returns True if both are True.
def chance(rate):
    roll1 = random.randint(1,100) <= rate
    roll2 = random.randint(1,100) <= rate
    if roll1 == True and roll2 == True:
        return True
    else:
        return False

# Combat Utilities

# Checks the speed of the player and enemy to determine who goes first.
# Also checks if either is slowed, and if so, divides their speed by the potency of the slowed condition.
# Returns either "player" or "enemy", which the combat dialogue uses to determine who goes first.
def chk_SPD(player, enemy):
    pspeed = player.stats['SPD']['value']
    espeed = enemy.stats['SPD']
    if player.status['slowed']['flag'] == True:
        pspeed = round(pspeed / player.status['slowed']['potency'])
    if enemy.status['slowed']['flag'] == True:
        espeed = round(espeed / enemy.status['slowed']['potency'])
    if pspeed > espeed:
        return "player"
    elif pspeed < espeed:
        return "enemy"
    elif pspeed == espeed:
        return random.choice(["player", "enemy"])

# This functions is used in combat to determine if the attack is a critical hit.
def chk_CRIT(attacker, target):
    import player, enemies
    if isinstance(attacker, player.Player):
        crit = (attacker.stats['SKL']['value'] + attacker.stats['LUCK']['value']) - target.stats['LUCK']
        return chance(crit)
    elif isinstance(attacker, enemies.Enemy):
        crit = (attacker.stats['SKL'] + attacker.stats['LUCK']) - target.stats['LUCK']['value']
        return chance(crit)

def chk_weakness(target):
    if target.weak:
        return target.weak
    
def calculate_hit(attacker, defender):
    import player, enemies
    if isinstance(attacker, player.Player):
        if attacker.status['blinded']['flag'] == True:
            Hit_rate = 100 + ((attacker.stats['SKL']['value'] + attacker.stats['LUCK']['value']) - defender.AVO()) - 20
            return chance(Hit_rate)
        Hit_rate = 100 + ((attacker.stats['SKL']['value'] + attacker.stats['LUCK']['value']) - defender.AVO())
        return chance(Hit_rate)
    elif isinstance(attacker, enemies.Enemy):
        if attacker.status['blinded']['flag'] == True:
            Hit_rate = 100 + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO()) - 20
            return chance(Hit_rate)
        Hit_rate = 100 + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO())
        return chance(Hit_rate)

def skill_hit(hrate, attacker, defender):
    if attacker.status['blinded']['flag'] == True:
        Hit_rate = hrate + ((attacker.stats['SKL']['value'] + attacker.stats['LUCK']['value']) - defender.AVO()) - 20
        return chance(Hit_rate)
    Hit_rate = hrate + ((attacker.stats['SKL']['value'] + attacker.stats['LUCK']['value']) - defender.AVO())
    return chance(Hit_rate)

def eskill_hit(skill, attacker, defender):
    if attacker.status['blinded']['flag'] == True:
        Hit_rate = skill.hit_rate + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO()) - 20
        print(Hit_rate)
        return chance(Hit_rate)
    Hit_rate = skill.hit_rate + ((attacker.stats['SKL'] + attacker.stats['LUCK']) - defender.AVO())
    return chance(Hit_rate)

def scroll_hit(scroll, defender):
    Hit_rate = scroll.accuracy - defender.AVO()
    return chance(Hit_rate)

def generate_damage(player, stat, attack, enemy):
    eweak = chk_weakness(enemy)
    if player.equipped['weapon'].damage_type == eweak:
        text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
        return random.randrange(stat + attack, stat + (attack * 2))
    else:
        return random.randrange(stat, stat + attack)

def generate_edamage(enemy, stat, attack):
    damage = random.randint(stat, stat + attack)
    return damage
    
def generate_skill_damage(player, skill, stat, damage, enemy):
    eweak = chk_weakness(enemy)
    if player.equipped['weapon'].damage_type == eweak or skill.damage_type == eweak:
        text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
        return random.randrange((stat + damage), (stat + (damage * 2)))
    else:
        return random.randrange((stat), (stat + damage))

def generate_eskill_damage(enemy, stat, damage):
    damage = random.randint(stat, stat + damage)
    return damage

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

def generate_emagic_damage(enemy, stat, spell):
    damage = random.randint(stat, stat + spell.damage)
    return damage
        
def generate_scroll_damage(scroll, enemy):
    eweak = chk_weakness(enemy)
    if scroll.damage_type == eweak:
        text_speed("You hit the {}'s weakness!\n".format(enemy.name), .05)
        return random.randrange(scroll.damage * 1.5, scroll.damage * 3)
    else:
        return random.randrange(scroll.damage, scroll.damage * 2)