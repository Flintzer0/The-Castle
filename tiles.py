import items, world, actions, enemies, time, sys, title_screen
from player import Player

def text_speed(text, speed):
    for l in text:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(speed)

class map_tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.entered = False
        self.unlocked = False
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.move_east())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.move_west())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.move_north())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.move_south())
        return moves
 
    def available_actions(self):
        """Returns all of the available actions in this room."""
        moves = self.adjacent_moves()
        moves.append(actions.view_inventory())
        moves.append(actions.potion())
        moves.append(actions.search())
        moves.append(actions.view_compendium())
        moves.append(actions.SaveAndExit())
        return moves
    
    def unlock(self, unlocked):
        raise NotImplementedError()
    
    def search_text(self):
        raise NotImplementedError()
    
    def searched_text(self):
        text_speed("You find nothing of interest.\n", .05)
        time.sleep(1)

    def intro_text(self, entered):
        raise NotImplementedError()


class jail(map_tile):
    def __init__(self, x, y):
        self.item = items.small_red_potion(1)
        super().__init__(x, y)

    def intro_text(self):
        if self.entered == False:
            text_speed("You leave your cell and find yourself in the dungeon.\n", .05)
            time.sleep(1)
            text_speed("There doesn't seem to be anyone around.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in the dungeon. What do you do?\n", .05)
            time.sleep(1)
    
    def search_text(self):
        text_speed("You can see something left on a dessicated table...\n", .05)
        time.sleep(1)

class stairs(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self, player):
        text_speed('You see a staircase leading up...\n', .05)
        text_speed('This marks the end of the demo...\n', .05)
        player.victory = True
        title_screen()

class locked_room(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def check_for_key(self, player):
        if player.inventory == items.Key:
            return True
        else:
            return False

    def intro_text(self, player):
        print('You see a locked door.')
        time.sleep(2)

    def unlock(self, player):
        if self.check_for_key(player):
            print('You unlock the door.')
            time.sleep(2)
            return True
        else:
            print('The door is locked.')
            time.sleep(2)
            return False

class jail_cell(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.gold(5)
        
    def intro_text(self):
        if self.entered == False:
            # text_speed("You awake in a dreary cell, surrounded by darkness.\n", .05)
            # time.sleep(1)
            # text_speed("You've lost track of how long it's been down here.\n", .05)
            # time.sleep(1)
            # text_speed("You hear something. . . \n", .1)
            # time.sleep(1)
            # text_speed(". . . \n", .5)
            # time.sleep(2)
            # text_speed("Your cell door creaks open.\n", .05)
            # time.sleep(.5)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in your cell. What do you do?\n", .05)
            time.sleep(2)
    
    def search_text(self):
        text_speed("You rifle through the straw on the floor of your cell...\n", .05)
        time.sleep(1)
    
    def searched_text(self):
        text_speed("There doesn't appear to be anything else in your cell.\n", .05)
        time.sleep(1)

class key_room(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y) 
        self.item = items.wooden_key(1)

    def intro_text(self):
        text_speed("You enter a room that appears to have been a guard's quarters.\n", .05)
        time.sleep(1)
        text_speed("There seems to be something on the table.\n", .05)
        time.sleep(1)
        text_speed("What do you do?\n", .05)

    def search_text(self):
        text_speed("You rustle through the papers on the table...\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("Nothing else catches your attention.\n", .05)
        time.sleep(1)

class five_gold(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y) 
        self.item = items.gold(5)

    def intro_text(self):
        text_speed("It appears to be another unremarkable hallway.\n", .05)
        time.sleep(1)
        text_speed("what do you do?\n", .05)
        time.sleep(1)

    def search_text(self):
        text_speed("Something glitters off to the side of the hallway...\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("Just you and the hallway.\n", .05)
        time.sleep(1)

class enemy_room(map_tile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)
        self.enemy.seen = False

    def deal_damage(self, player):
        if self.enemy.damage < player.DEF:
            self.enemy.damage = 1
            player.HP = player.HP - self.enemy.damage
            text_speed("Enemy does 1 damage. You have {} HP remaining.\n".format(player.HP), .05)
        else:
            damage = self.enemy.damage - player.DEF
            player.HP = player.HP - damage
            text_speed("Enemy does {} damage. You have {} HP remaining.\n".format(damage, player.HP), .05)

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.fight(enemy=self.enemy)]
        else:
            pass
    
    def check_monster(self, player):
        if self.enemy.seen == False:
            self.enemy.seen = True
            player.add_monster(self.enemy)
        else:
            pass

class empty_passageway(map_tile):
    def intro_text(self):
        text_speed("It appears to be an unremarkable hallway.\n", .05)
        time.sleep(1)
        text_speed("What do you do?\n", .05)
        time.sleep(1)

class empty_room(map_tile):
    def intro_text(self):
        text_speed("It appears to be an unremarkable room.\n", .05)
        time.sleep(1)
        text_speed("What do you do?\n", .05)
        time.sleep(1)

class giant_spider_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.giant_spider())
 
    def intro_text(self):
        if self.enemy.is_alive():
            text_speed("This hallway seems especially dark.\n", .05)
            time.sleep(1)
            text_speed("You hear a skittering sound.\n", .05)
            time.sleep(1)
            text_speed("A giant spider drops from the ceiling!\n", .02)
            time.sleep(.5)
        else:
            text_speed("The corpse of a dead spider rots on the ground.\n", .05)
            time.sleep(1)
 
class goblin_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.goblin())
 
    def intro_text(self):
        if self.enemy.is_alive():
            text_speed("You enter a circular room with a low ceiling.\n", .05)
            time.sleep(1)
            text_speed("A figure appears crumpled in the corner.\n", .05)
            time.sleep(1)
            text_speed("It's a goblin!\n", .02)
            time.sleep(.5)
        else:
            text_speed("The corpse of a dead goblin rots on the ground.\n", .05)
            time.sleep(1)

class find_rusty_dagger_room(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y) 
        self.item = items.rusty_dagger()
 
    def intro_text(self):
        text_speed("You're in a slightly larger room than the others.\n", .05)
        time.sleep(1)
        text_speed("You're not quite sure what it was used for.\n", .05)
        time.sleep(1)
        text_speed("You can make out what appears to be torture devices, though they have long since decayed.\n", .05)
        time.sleep(1)
        text_speed("What do you do?\n", .05)
        time.sleep(1)

    def search_text(self):
        text_speed("You can see something glinting on one of the racks...\n", .05)
        time.sleep(1)
    
    def searched_text(self):
        text_speed("Just you and the torture devices.\n", .05)
        time.sleep(1)

class find_rusty_shield_room(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.rusty_shield()
 
    def intro_text(self):
        return """
        Your notice something up against a wall.
        It's a rusty shield! You pick it up.
        """