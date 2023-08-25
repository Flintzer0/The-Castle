import random, enemy_skills, magic

class EnemyAI:
    def __init__(self, enemy):
        self.enemy = enemy

    def chk_heals(self):
        for s in self.enemy.skills:
            if isinstance(s, enemy_skills.Restore):
                return True
        for m in self.enemy.spells:
            if isinstance(m, magic.Restore):
                return True

    def chk_lists(self, alist, atype):
        if alist == self.enemy.skills:
            for s in self.enemy.skills:
                if isinstance(s, atype):
                    return True
        elif alist == self.enemy.spells:
            for m in self.enemy.spells:
                if isinstance(m, atype):
                    return True

    def decide(self, player):
        pchoice = player.pchoice
        debuffed = False
        skillchance = random.randint(1, 100) < 0
        magicchance = random.randint(1, 100) < 0
        hslist = []
        hchance = random.randint(1, 100) < 0
        aslist = []
        achance = random.randint(1, 100) < 0
        bslist = []
        bchance = random.randint(1, 100) < 0
        dslist = []
        dchance = random.randint(1, 100) < 0

        for d in self.enemy.status:
            if self.enemy.status[d]['flag'] == True:
                debuffed = True

        if self.enemy.stats['HP'] < (self.enemy.stats['mHP'] / 3) and self.chk_heals():
            if self.chk_lists(self.enemy.skills, enemy_skills.Restore):
                for s in self.enemy.skills:
                    if isinstance(s, enemy_skills.Restore):
                        if s.rtype == 'Heal':
                            return self.enemy.use_skill(s, player)
                        
            if self.chk_lists(self.enemy.spells, magic.Restore):
                for s in self.enemy.spells:
                    if isinstance(s, magic.Restore):
                        if s.rtype == 'Heal':
                            return self.enemy.use_spell(s, player)
                            
        elif debuffed:
            if self.chk_lists(self.enemy.skills, enemy_skills.Restore):
                for sk in self.enemy.skills:
                    if isinstance(sk, enemy_skills.Restore):
                        if sk.rtype == 'Cure':
                            return self.enemy.use_skill(sk, player)
                        
            elif self.chk_lists(self.enemy.spells, magic.Restore):
                for sp in self.enemy.spells:
                    if isinstance(sp, magic.Restore):
                        if sp.rtype == 'Cure':
                            return self.enemy.use_spell(sp, player)
                    
        elif self.enemy.skills and self.enemy.spells:
            if pchoice == None:
                skillchance = random.randint(1, 100) < 40
                magicchance = random.randint(1, 100) < 40
            elif pchoice == 'attack':
                skillchance = random.randint(1, 100) < 40
                magicchance = random.randint(1, 100) < 40
            elif pchoice == 'skill':
                skillchance = random.randint(1, 100) < 60
                magicchance = random.randint(1, 100) < 25
            elif pchoice == 'magic':
                skillchance = random.randint(1, 100) < 25
                magicchance = random.randint(1, 100) < 60
            elif pchoice == 'item':
                skillchance = random.randint(1, 100) < 80
                magicchance = random.randint(1, 100) < 80
        elif self.enemy.skills:
            if pchoice == None:
                skillchance = random.randint(1, 100) < 66
            elif pchoice == 'attack':
                skillchance = random.randint(1, 100) < 66
            elif pchoice == 'skill':
                skillchance = random.randint(1, 100) < 85
            elif pchoice == 'magic':
                skillchance = random.randint(1, 100) < 85
            elif pchoice == 'item':
                skillchance = random.randint(1, 100) < 80
        elif self.enemy.spells:
            if pchoice == None:
                magicchance = random.randint(1, 100) < 66
            elif pchoice == 'attack':
                magicchance = random.randint(1, 100) < 66
            elif pchoice == 'skill':
                magicchance = random.randint(1, 100) < 85
            elif pchoice == 'magic':
                magicchance = random.randint(1, 100) < 85
            elif pchoice == 'item':
                magicchance = random.randint(1, 100) < 80
        else:
            print('Only Basic')

        if skillchance:
            print('Skill', skillchance)
            skilled = False
            while not skilled:
                for c in self.enemy.skills:
                    if isinstance(c, enemy_skills.Restore):
                        if self.enemy.stats['HP'] < (self.enemy.stats['mHP'] / 2):
                            if c.rtype == 'Heal':
                                hchance = random.randint(1, 100) < 25
                                hslist.append(c)
                    if isinstance(c, enemy_skills.Attack):
                        achance = random.randint(1, 100) < 80
                        aslist.append(c)
                    if isinstance(c, enemy_skills.Buff):
                        bchance = random.randint(1, 100) < 80
                        bslist.append(c)
                    if isinstance(c, enemy_skills.Debuff):
                        dchance = random.randint(1, 100) < 80
                        dslist.append(c)
                if hchance:
                    heal = random.choice(hslist)
                    skilled = True
                    return self.enemy.use_skill(heal, player)
                elif achance:
                    attack = random.choice(aslist)
                    skilled = True
                    return self.enemy.use_skill(attack, player)
                elif bchance:
                    buff = random.choice(bslist)
                    skilled = True
                    return self.enemy.use_skill(buff, player)
                elif dchance:
                    debuff = random.choice(dslist)
                    skilled = True
                    return self.enemy.use_skill(debuff, player)    
        
        if magicchance:
            print('Magic', magicchance)
            spelled = False
            while not spelled:
                for c in self.enemy.spells:
                    if isinstance(c, magic.Restore):
                        if self.enemy.stats['HP'] < (self.enemy.stats['mHP'] / 2):
                            if c.rtype == 'Heal':
                                hchance = random.randint(1, 100) < 25
                                hslist.append(c)
                    if isinstance(c, magic.Attack):
                        achance = random.randint(1, 100) < 40
                        aslist.append(c)
                    if isinstance(c, magic.Buff):
                        bchance = random.randint(1, 100) < 40
                        bslist.append(c)
                    if isinstance(c, magic.Debuff):
                        dchance = random.randint(1, 100) < 40
                        dslist.append(c)
                if hchance:
                    heal = random.choice(hslist)
                    spelled = True
                    return self.enemy.use_spell(heal, player)
                elif achance:
                    attack = random.choice(aslist)
                    spelled = True
                    return self.enemy.use_spell(attack, player)
                elif bchance:
                    buff = random.choice(bslist)
                    spelled = True
                    return self.enemy.use_spell(buff, player)
                elif dchance:
                    debuff = random.choice(dslist)
                    spelled = True
                    return self.enemy.use_spell(debuff, player)

        return self.enemy.attack(player)