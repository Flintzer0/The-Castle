import items, world, actions, enemies, time, sys, title_screen
from player import Player
from utilities import text_speed

class map_tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.entered = False
        self.unlocked = True
        self.item = None
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            if isinstance(world.tile_exists(self.x + 1, self.y), locked_room):
                if world.tile_exists(self.x + 1, self.y).unlocked == True:
                    moves.append(actions.move_east())
                else:
                    text_speed("There's a locked door to the east.\n", .05)
                    moves.append(actions.unlock(world.tile_exists(self.x + 1, self.y)))
            else:
                moves.append(actions.move_east())
        if world.tile_exists(self.x - 1, self.y):
            if isinstance(world.tile_exists(self.x - 1, self.y), locked_room):
                if world.tile_exists(self.x - 1, self.y).unlocked == True:
                    moves.append(actions.move_west())
                else:
                    text_speed("There's a locked door to the west.\n", .05)
                    moves.append(actions.unlock(world.tile_exists(self.x - 1, self.y)))
            else:
                moves.append(actions.move_west())
        if world.tile_exists(self.x, self.y - 1):
            if isinstance(world.tile_exists(self.x, self.y - 1), locked_room):
                if world.tile_exists(self.x, self.y - 1).unlocked == True:
                    moves.append(actions.move_north())
                else:
                    text_speed("There's a locked door to the north.\n", .05)
                    moves.append(actions.unlock(world.tile_exists(self.x, self.y - 1)))
            else:
                moves.append(actions.move_north())
        if world.tile_exists(self.x, self.y + 1):
            if isinstance(world.tile_exists(self.x, self.y + 1), locked_room):
                if world.tile_exists(self.x, self.y + 1).unlocked == True:
                    moves.append(actions.move_south())
                else:
                    text_speed("There's a locked door to the south.\n", .05)
                    moves.append(actions.unlock(world.tile_exists(self.x, self.y + 1)))
            else:
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
    
    def search_text(self):
        raise NotImplementedError()
    
    def searched_text(self):
        text_speed("You find nothing of interest.\n", .05)
        time.sleep(1)

    # def intro_text(self):
    #     raise NotImplementedError()

class jail(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.small_red_potion(1)

    def intro_text(self):
        if self.entered == False:
            # text_speed("You leave your cell and find yourself in the dungeon.\n", .05)
            # time.sleep(1)
            # text_speed("There doesn't seem to be anyone around.\n", .05)
            # time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in the dungeon. \nWhat do you do?\n", .05)
            time.sleep(1)
    
    def search_text(self):
        text_speed("You can see something left on a dessicated table...\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("You find rotting wood and empty cells.\n", .05)

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
        self.unlocked = False
    
class armory(locked_room):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.dagger()

    def intro_text(self):
        if self.entered == False:
            text_speed("You enter a room that appears to have been an armory.\n", .05)
            time.sleep(1)
            text_speed("There are several suits of armor in massive states of decay.\n", .05)
            time.sleep(1)
            text_speed("Most all of the weapons have rusted beyond use, but some of\nthem might still be salvageable.\n", .05)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
        else:
            text_speed("You're back in the armory. \nWhat do you do?\n", .05)
            time.sleep(1)

    def search_text(self):
        text_speed("At first glance, it doesn't look like there's anything of use here,\n but you notice something close to a wall, behind a toppled display case...", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("Everything else in here is completely unuseable.\n", .05)
        time.sleep(1)

class enemy_room(map_tile):
    def __init__(self, x, y, enemy):
        super().__init__(x, y)
        self.enemy = enemy
        self.enemy.seen = False

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.fight(enemy=self.enemy)]
        else:
            return super.available_actions(self)
    
    def check_monster(self, player):
        if self.enemy.seen == False:
            self.enemy.seen = True
            player.add_monster(self.enemy)
        else:
            pass

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
            # text_speed("You hear something. . . \n", .5)
            # time.sleep(1)
            # text_speed(". . . \n", 1)
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
        if self.entered == False:
            # text_speed("You enter a room that appears to have been a guard's quarters.\n", .05)
            # time.sleep(1)
            # text_speed("There seems to be something on the table.\n", .05)
            # time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in the guard's quarters. \nWhat do you do?\n", .05)
            time.sleep(1)

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
        if self.entered == False:
            text_speed("It appears to be another unremarkable hallway.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(.5)
            self.entered = True
        else:
            text_speed("You're back in this unremarkable hallway. \nWhat do you do?\n", .05)
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

    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.fight(enemy=self.enemy)]
        else:
            return map_tile.available_actions(self)

class empty_passageway(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        if self.entered == False:
            text_speed("It appears to be another unremarkable hallway.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(.5)
            self.entered = True
        else:
            text_speed("You're back in this unremarkable hallway. \nWhat do you do?\n", .05)
            time.sleep(1)

class empty_room(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        if self.entered == False:
            text_speed("It appears to be an unremarkable room.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in this unremarkable room. \nWhat do you do?\n", .05)
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