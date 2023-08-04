import time
from utilities import *

class ScrollSpell():
    def __init__(self, name, damage, damage_type, hit_rate, status=""):
        self.name = name
        self.damage = damage
        self.damage_type = damage_type
        self.hit_rate = hit_rate
        self.status = status
        
    def cast(self, enemy):
        if scroll_hit(self, enemy):
            text_speed("You cast {} from the scroll!\n".format(self.name), .03)
            time.sleep(.2)
            damage = generate_scroll_damage(self, enemy)
            text_speed("The {} takes {} {} damage!\n".format(enemy.name, damage, self.damage_type), .03)

class fireball(ScrollSpell):
    def __init__(self):
        super().__init__(name="Fireball", damage=20, damage_type="Fire", hit_rate=80)


            