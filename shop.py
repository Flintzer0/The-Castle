import items, enemies, actions, world, time
from utilities import text_speed

class Shopkeeper:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def shop_intro(self):
        raise NotImplementedError()

    def shop_text(self):
        raise NotImplementedError()

    def display_shop(self, player):
        self.shop_text()
        text_speed("Choose an item to buy:\n", .05)
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            print("{}. {} - {} Gold".format(i + 1, item.name, item.value))
        print(f'{len(self.inventory)}: Exit Shop')
            

class Trader(Shopkeeper):
    def __init__(self):
        super().__init__(name="Dungeon Trader", inventory=[items.rusty_sword(), items.iron_dagger(), items.small_red_potion(5), items.small_blue_potion(5)])

    def shop_intro(self):
        text_speed("The toothy man smiles at you as you approach.\n", .05)
        time.sleep(1)
        text_speed("His smile splits as he says in a gravelly tone, \"What can I fix you with?\"\n", .05)

    def shop_text(self):
        text_speed("The trader grins as you peak at his wares.\n", .05)
        time.sleep(1)
        text_speed("He says, \"I have a few things that might interest you.\"\n", .05)