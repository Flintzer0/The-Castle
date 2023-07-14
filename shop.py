import items, enemies, actions, world
from utilities import text_speed

class Shopkeeper:
    def __init__(self, name, inventory):
        self.name = name
        self.inventory = inventory

    def shop_text(self):
        raise NotImplementedError()

    def display_shop(self, player):
        self.shop_text()
        text_speed("Choose an item to buy:\n", .05)
        for i in range(len(self.inventory)):
            item = self.inventory[i]
            print("{}. {} - {} Gold".format(i + 1, item.name, item.value))
        print("0. Exit Shop")

class Trader(Shopkeeper):
    def __init__(self):
        super().__init__(name="Dungeon Trader", inventory=[items.dagger(), items.small_red_potion(5), items.small_blue_potion(5)])

    def shop_text(self):
        text_speed("The trader grins as you peak at his wares.\n", .05)
        text_speed("He says, \"I have a few things that might interest you.\"\n", .05)