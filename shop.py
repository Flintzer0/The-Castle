import items, enemies, actions, world, time, random
from utilities import text_speed

class Shopkeeper:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def shop_intro(self):
        raise NotImplementedError()

    def shop_text(self):
        raise NotImplementedError()
    
    def leave_shop(self):
        raise NotImplementedError()
    
    def leave_tile(self):
        raise NotImplementedError()

    def display_shop(self):
        text_speed("Choose an item to buy:\n", .05)
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            if isinstance(item, items.Potion):
                print("{}. {} x{} - {} Gold each".format(i + 1, item.name, item.qty, item.value))
            elif isinstance(item, items.sold_out):
                print("{}. {}".format(i + 1, item.name))
            else:
                print("{}. {} - {} Gold".format(i + 1, item.name, item.value))
        print(f'{len(self.inventory) + 1}: Exit Shop')
            

class Trader(Shopkeeper):
    def __init__(self):
        super().__init__(name="Dungeon Trader", inventory=[items.rusty_sword(), items.iron_dagger(), items.small_red_potion(5), items.small_blue_potion(5)])

    def shop_intro(self):
        text_speed("The toothy man smiles at you as you approach.\n", .05)
        time.sleep(.5)
        text_speed("His smile splits as he says in a gravelly tone, \"What can I fix you with?\"\n", .05)

    def shop_text(self):
        text_speed("The trader grins as you peak at his wares.\n", .05)
        time.sleep(.5)
        roll = random.randint(1, 5)
        if roll == 1:
            text_speed("\"I have a few things that might interest you.\"\n", .05)
        elif roll == 2:
            text_speed("\"See anything you like?\"\n", .05)
        elif roll == 3:
            text_speed("\"I have decent prices, for decent... folk. Heheh.\"\n", .05)
        elif roll == 4:
            text_speed("\"You won't find anyone else here offering what I have!\n Though... You won't find anyone else, either! Heheheh!\"\n", .05)
        elif roll == 5:
            text_speed("\"I'm sure you'll find something to your liking.\"\n", .05)

    def leave_shop(self):
        text_speed("\"Let me know if there's anything else I can help you with...\"\n", .05)
        time.sleep(.2)

    def leave_tile(self):
        text_speed("\"Do come back...\"\n", .05)
        time.sleep(.2)