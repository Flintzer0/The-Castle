import items, world, actions, enemies, time, sys, title_screen
from player import Player
from utilities import text_speed

# Base Class all other tiles are built off of
class map_tile:
    def __init__(self, x, y):
        # Template for tile placement. All tiles will have these attributes.
        # Coordinates are first set, and all base tiles are marked as unentered, unlocked, and empty.
        # These attributes are overwritten in the subclasses.
        self.x = x
        self.y = y
        # Indicates whether the player has been to the room before. This flag is used to determine whether to display the 
        # standard intro text or a variation of it.
        self.entered = False
        # Indicates whether the room is locked. This helps determine what actions are available to the player.
        self.unlocked = True
        # Indicates whether the room contains an item or not. If a room contains an item, it will be shown here in the __init__ method.
        self.item = None

    def adjacent_moves(self):
        # Returns all move actions for adjacent tiles.
        moves = []
        # Checks if the tile exists in that direction of the world.
        if world.tile_exists(self.x + 1, self.y):
            # Checks if the adjacent tile in this direction is a locked room. If it is, but is currently locked, 
            # it will add the unlock action to the list of moves instead and notify the player that the door is locked in that direction.
            # First, it checks whther the tile is an instance of the locked_room class.
            if isinstance(world.tile_exists(self.x + 1, self.y), locked_room):
                # If it is, it checks whether the room is unlocked.
                if world.tile_exists(self.x + 1, self.y).unlocked == True:
                    # If it is, it returns the available moves as normal.
                    moves.append(actions.move_east())
                else:
                    # If it isn't, it notifies the player that the door is locked and adds the unlock action to the list of moves.
                    text_speed("There's a locked door to the east.\n", .05)
                    moves.append(actions.unlock(world.tile_exists(self.x + 1, self.y)))
            else:
                # If the tile isn't a locked_room, it adds the move action to the list of moves as normal.
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
        # Returns all of the standard available actions in this room.
        moves = self.adjacent_moves()
        moves.append(actions.view_inventory())
        moves.append(actions.potion())
        moves.append(actions.search())
        moves.append(actions.view_compendium())
        moves.append(actions.SaveAndExit())
        return moves
    
    # Funtions from here down are all overwritten by the subclasses.
    # The methods are described mainly to ensure that they are all implemented in the subclasses.

    def intro_text(self):
        # Text that displays when the player enters the room.
        raise NotImplementedError()
    
    def search_text(self):
        # Text that displays when the player searches the room.
        raise NotImplementedError()
    
    def searched_text(self):
        # Text that displays when the player has already searched the room. If no unique dialogue is set, or the room is empty, it will display the default text.
        text_speed("You find nothing of interest.\n", .05)
        time.sleep(1)

# Main Tile Subclasses

class locked_room(map_tile):
    # Marks a room as locked. The player will need to unlock the room to enter it.
    def __init__(self, x, y):
        super().__init__(x, y)
        self.unlocked = False

class enemy_room(map_tile):
    # Marks a room as containing an enemy. The enemy is passed in as an argument.
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    # The available actions are overwritten to include the fight action if the enemy is alive.
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.fight(enemy=self.enemy)]
        else:
            return map_tile.available_actions(self)

# Empty Tile Subclasses

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

# Basement 1 Tile Subclasses

# Starting Room
class jail_cell(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        # Here we can see that the item attribute is overwritten to contain a gold item.
        self.item = items.gold(5)
        
    def intro_text(self):
        # Here we can see that the intro_text method is overwritten to display a unique message.
        # Also shown is what occurs when the player enters the room for the first time and when they return to the room.
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
        # Here we can see that the search_text method is overwritten to display a unique message.
        text_speed("You rifle through the straw on the floor of your cell...\n", .05)
        time.sleep(1)
    
    def searched_text(self):
        # Here we can see that the searched_text method is overwritten to display a unique message.
        # It also demonstrates what occurs when the player searches the room after it has already been searched and cleared.
        text_speed("There doesn't appear to be anything else in your cell.\n", .05)
        time.sleep(1)

class dungeon(map_tile):
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