# Damage damage_types
# Fire
# Cold
# Lightning
# Water
# Earth
# Wind
# Holy
# Demonic
# Necrotic
# Poison
# Turn Undead (labeled as Turn in-code)

class Spell:
    def __init__(self, name, description, cost, damage, damage_type):
        self.name = name
        self.description = description
        self.cost = cost
        self.damage = damage
        self.damage_type = damage_type
    
    def __str__(self):
        return '{}\n====================\n{}\nMP: {}\nDamage: {}\nType: {}'.format(self.name, self.description, self.cost, self.damage, self.damage_type)
    
# Basic Spells

class fire(Spell):
    def __init__(self):
        super().__init__(name="Fire", cost=5, damage=5, damage_type="Fire", 
                         description="Your Fire spell. Deals Fire damage to a single target.")
        
class ice(Spell):
    def __init__(self):
        super().__init__(name="Ice", cost=5, damage=5, damage_type="Cold", 
                         description="Your Ice spell. Deals Cold damage to a single target.")
        
class shock(Spell):
    def __init__(self):
        super().__init__(name="Shock", cost=5, damage=5, damage_type="Lightning", 
                         description="Your Shock spell. Deals Lightning damage to a single target.")
        
class water(Spell):
    def __init__(self):
        super().__init__(name="Water", cost=5, damage=5, damage_type="Water", 
                         description="Your Water spell. Deals Water damage to a single target.")
        
class quake(Spell):
    def __init__(self):
        super().__init__(name="Quake", cost=5, damage=5, damage_type="Earth", 
                         description="Your Quake spell. Deals Earth damage to a single target.")
        
class wind(Spell):
    def __init__(self):
        super().__init__(name="Wind", cost=5, damage=5, damage_type="Wind", 
                         description="Your Wind spell. Deals Wind damage to a single target.")
        
class smite(Spell):
    def __init__(self):
        super().__init__(name="Smite", cost=5, damage=5, damage_type="Holy", 
                         description="Your Smite spell. Deals Holy damage to a single target.")
        
class curse(Spell):
    def __init__(self):
        super().__init__(name="Curse", cost=5, damage=5, damage_type="Demonic", 
                         description="Your Curse spell. Deals Demonic damage to a single target.")
        
class wither(Spell):
    def __init__(self):
        super().__init__(name="Wither", cost=5, damage=5, damage_type="Necrotic", 
                         description="Your Wither spell. Deals Necrotic damage to a single target.")
        
class poison(Spell):
    def __init__(self):
        super().__init__(name="Poison", cost=5, damage=5, damage_type="Poison", 
                         description="Your Poison spell. Deals Poison damage to a single target.")
        
class turn(Spell):
    def __init__(self):
        super().__init__(name="Turn Undead", cost=5, damage=5, damage_type="Turn", 
                         description="Your Turn Undead spell. Deals damage to a single target. \nDeals bonus damage to undead creatures.")