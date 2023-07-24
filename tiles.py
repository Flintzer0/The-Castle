import items, world, actions, enemies, time, shop
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
        self.flooded = False

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
        moves.append(actions.view_stats())
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

class shop_room(map_tile):
    # Marks a room as containing a shopkeeper. The shopkeeper is passed in as an argument.
    def __init__(self, x, y, shopkeep):
        self.shopkeep = shopkeep
        super().__init__(x, y)

    # The available actions are overwritten to include the buy action.
    def available_actions(self):
        moves = self.adjacent_moves()
        moves.append(actions.buy(shopkeep=self.shopkeep))
        moves.append(actions.view_inventory())
        moves.append(actions.view_stats())
        moves.append(actions.potion())
        moves.append(actions.search())
        moves.append(actions.view_compendium())
        moves.append(actions.SaveAndExit())
        return moves
    
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

    def search_text(self):
        pass

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

    def search_text(self):
        pass

#===============================================================================#

# Basement 2 Tile Subclasses

#===============================================================================#

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
            text_speed("You awake in a dreary cell, surrounded by darkness.\n", .05)
            time.sleep(1)
            text_speed("You've lost track of how long it's been down here.\n", .05)
            time.sleep(1)
            text_speed("You hear something. . . \n", .1)
            time.sleep(1)
            text_speed(". . . \n", 1)
            time.sleep(2)
            text_speed("Your cell door creaks open.\n", .05)
            time.sleep(.5)
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

# Regular Rooms
class dungeon_1(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.small_red_potion(1)

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
            text_speed("You're back in the dungeon. \nWhat do you do?\n", .05)
            time.sleep(1)
    
    def search_text(self):
        text_speed("You can see something left on a dessicated table...\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("You find rotting wood and empty cells.\n", .05)

class dungeon_2(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.rusty_shield()

    def intro_text(self):
        if self.entered == False:
            text_speed("You find another dungeon, not that you're surprised.\n", .05)
            time.sleep(1)
            text_speed("All of the cells are empty, from what you can tell.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in the dungeon. \nWhat do you do?\n", .05)
            time.sleep(1)

    def search_text(self):
        text_speed("You notice something poking out of the straw of one of the cells...\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("The empty cells send a chill down your spine, but nothing more...\n", .05)
        time.sleep(1)

class torture_chamber(map_tile):
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

class guard_room(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y) 
        self.item = items.wooden_key(1)

    def intro_text(self):
        if self.entered == False:
            text_speed("You enter a room that appears to have been a guard's quarters.\n", .05)
            time.sleep(1)
            text_speed("There is a table with broken legs and a few dessicated chairs.\n", .05)
            time.sleep(1)
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

# Flooded Rooms
class pre_flooded_hall(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.gold(15)

    def intro_text(self):
        if self.entered == False:
            text_speed("You enter what appears to be a normal hallway at first glance.\n", .05)
            time.sleep(1)
            text_speed("However, on closer inspection you notice that the floor is slightly damp.\n", .05)
            time.sleep(1)
            text_speed("Opposite you in the room, the hallway descends downwards into dark, murky water.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in the damp hallway. \nWhat do you do?\n", .05)
            time.sleep(1)

    def search_text(self):
        text_speed("You notice something glinting in the water...\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("The water is too murky to see anything else.\n", .05)
        time.sleep(1)

class flooded_hall(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.strength_1_ring()
        self.flooded = True

    def intro_text(self):
        if self.entered == False:
            text_speed("You enter a hallway that is completely submerged in water.\n", .05)
            time.sleep(1)
            text_speed("You can't see the bottom, and the water is murky.\n", .05)
            time.sleep(1)
            text_speed("Luckily, your Ring of the Sea is keeping you from drowning.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            text_speed("You're back in the flooded hallway. \nWhat do you do?\n", .05)
            time.sleep(1)

    def search_text(self):
        text_speed("You notice something glinting in the water...\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("You look into the depths of the water...\n", .05)
        time.sleep(1)
        text_speed("It looks back.\n", .05)
        time.sleep(1)
        text_speed(". . .\n", .01)
        time.sleep(3)
        text_speed("Probably best not to linger here.\n", .05)
        time.sleep(1)

# Stairs
class stairs(map_tile):
    def __init__(self, x, y):
        super().__init__(x, y)

    def intro_text(self):
        text_speed('You see a staircase leading up...\n', .05)
        time.sleep(1)
        text_speed('This marks the end of the demo...\n', .05)
        time.sleep(1)
        
    def end_demo(self, player):
        text_speed('You completed the demo!\n', .05)
        time.sleep(1)
        text_speed('Thanks for playing!\n', .05)
        time.sleep(1)
        player.victory = True

# Special Tile Subclasses
class low_trader(shop_room):
    def __init__(self, x, y):
        super().__init__(x, y, shopkeep=shop.Trader())

    def intro_text(self):
        if self.entered == False:
            text_speed("You enter a room and are suddenly blinded by a bright light.\n", .05)
            time.sleep(1)
            text_speed("Once your eyes have adjusted to the light, you see a room \ncompletely out of place in the bleak atmosphere you've grown accustomed to.\n", .05)
            time.sleep(1)
            text_speed("The room is brightly lit, and there are shelves full of \nvarious items lining the walls.\n", .05)
            time.sleep(1)
            text_speed("There is a countertop, with a stocky man standing behind it.\n", .05)
            time.sleep(1)
            self.shopkeep.shop_intro()
            self.entered = True
        else:
            text_speed("You're back in the room of the Low Trader. \nWhat do you do?\n", .05)
            time.sleep(1)

    def searched_text(self):
        text_speed("You probably shouldn't search through the Trader's wares.\n", .05)
        time.sleep(1)

class ritual_room(locked_room):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.cold_iron_sword()
        self.choice = ""

    def intro_text(self):
        if self.entered == False:
            text_speed("You enter a dark room dimly lit by a single torch.\n", .05)
            time.sleep(1)
            text_speed("The room is empty, save for a single pedestal in the center.\n", .05)
            time.sleep(1)
            text_speed("You can make out what seems to be ritualistic markings on the floor.\n", .05)
            time.sleep(1)
            text_speed("A cold chill runs down your spine as you realize that you can hear \nconstant whispers in the darkness.\n", .05)
            time.sleep(1)
            text_speed("What do you do?\n", .05)
            time.sleep(1)
            self.entered = True
        else:
            if self.item != None:
                text_speed("You're back in the dimly lit room.", .05)
                time.sleep(1)
                text_speed("The whisper seem to invite you to stay...\n", .05)
                time.sleep(1)
                text_speed("What do you do?\n", .05)
                time.sleep(1)
            else:
                text_speed("You're back in the ritual room. \n", .05)
                time.sleep(1)
                text_speed("It's... quiet, here.\n", .05)
                time.sleep(1)
                text_speed("What do you do?\n", .05)

    def search_text(self):
        text_speed("As you move your hands across the floor, candles you didn't notice before light up.\n", .05)
        time.sleep(1)
        text_speed("The pedestal in the center of the room begins to glow and steadily rises.\n", .05)
        time.sleep(1)
        text_speed("You can see the pedestal is really an altar, with an eerie blue sword jammed into it.\n", .05)
        time.sleep(1)
        text_speed("You can hear the whispers more clearly now, and they seem to be coming from the sword.\n", .05)
        time.sleep(1)
        text_speed("The whipsers invite you to offer your blood in exchange for the sword.\n", .05)
        time.sleep(1)
        text_speed("What do you do?\n", .05)
        time.sleep(1)
        print("1. Offer your blood.\n 2. Leave the sword alone.")
        self.choice = input()
    
    def choice_1_text(self):
        text_speed("You offer your blood to the sword.\n", .05)
        time.sleep(1)
        text_speed("The whispers grow louder, and the sword begins to glow brighter.\n", .05)
        time.sleep(1)
        text_speed("You can feel the sword's power coursing through your veins.\n", .05)
        time.sleep(1)
        text_speed("You take the sword.\n", .05)
        time.sleep(1)
        text_speed("The whispers fade away.\n", .05)
        time.sleep(1)

    def choice_2_text(self):
        text_speed("You decide to leave the sword alone.\n", .05)
        time.sleep(1)
        text_speed("You ignore the whispers urging you to reconsider.\n", .05)
        time.sleep(1)

    def searched_text(self):
        text_speed("The room is quiet now.\n", .05)
        time.sleep(1)

# Enemy Rooms
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
 
class giant_spider_room_2(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.giant_spider())

    def intro_text(self):
        if self.enemy.is_alive():
            text_speed("You enter a large, round room.\n", .05)
            time.sleep(1)
            text_speed("There are large webs covering the walls.\n", .05)
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

class skeleton_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.skeleton())
 
    def intro_text(self):
        if self.enemy.is_alive():
            text_speed("You enter a room with several heavily decayed corpses.\n", .05)
            time.sleep(1)
            text_speed("It seems to have been the site of a battle.\n", .05)
            time.sleep(1)
            text_speed("Suddenly, a figure stands up.\n", .05)
            time.sleep(1)
            text_speed("It's a skeleton!\n", .02)
            time.sleep(.5)
        else:
            text_speed("The bones of the defeated skeleton lie scattered on the floor.\n", .05)
            time.sleep(1)

class demon_bat_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.demon_bat())
 
    def intro_text(self):
        if self.enemy.is_alive():
            text_speed("You enter a room with a high ceiling.\n", .05)
            time.sleep(1)
            text_speed("You can hear a faint flapping sound.\n", .05)
            time.sleep(1)
            text_speed("A demon bat swoops down from the ceiling!\n", .02)
            time.sleep(.5)
        else:
            text_speed("The corpse of the demon bat rots on the ground.\n", .05)
            time.sleep(1)

class large_rat_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.large_rat())
 
    def intro_text(self):
        if self.enemy.is_alive():
            text_speed("You enter a room covered in rotten food and bones.\n", .05)
            time.sleep(1)
            text_speed("You can hear a screech.\n", .05)
            time.sleep(1)
            text_speed("A giant rat scurries towards you!\n", .02)
            time.sleep(.5)
        else:
            text_speed("The corpse of the giant rat rots on the ground.\n", .05)
            time.sleep(1)

class giant_centipede_room(enemy_room):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.giant_centipede())
 
    def intro_text(self):
        if self.enemy.is_alive():
            text_speed("You're in a large room with a curving rooftop.\n", .05)
            time.sleep(1)
            text_speed("The ceiling is too high and dark to make out.\n", .05)
            time.sleep(1)
            text_speed("However, up ahead you can see through the doorway to the next room.\n", .05)
            time.sleep(1)
            text_speed("There are stairs leading up to the next floor!\n Your escape from this dungeon seems close at hand!", .05)
            time.sleep(1)
            text_speed("As you stride towards the next room, you feel a rumbling in the ground and hear a skittering sound.\n", .05)
            time.sleep(1)
            text_speed("With an ear-splitting screech, a giant centipede drops from the ceiling!\n", .05)
            time.sleep(1)
            text_speed("It's time to fight your way out of this dungeon!\n", .05)
            time.sleep(1)
        else:
            text_speed("The corpse of the giant centipede rots on the ground.\n", .05)
            time.sleep(1)

#===============================================================================#

# Floor 1 Tile Subclasses
# Unique tiles still needed:
class armory(locked_room):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.item = items.iron_sword()

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

#===============================================================================#

# Floor 2 Tile Subclasses
# Unique tiles still needed:

#===============================================================================#

# Floor 3 Tile Subclasses
# Unique tiles still needed:

#===============================================================================#

# Floor 4 Tile Subclasses
# Unique tiles still needed:

#===============================================================================#

# Floor 5 Tile Subclasses
# Unique tiles still needed: