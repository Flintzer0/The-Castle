from player import Player
import title_screen
 
class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs
 
    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class move_north(Action):
    def __init__(self):
        super().__init__(method=Player.move_north, name='Move north', hotkey='w')
 
class move_south(Action):
    def __init__(self):
        super().__init__(method=Player.move_south, name='Move south', hotkey='s')
 
class move_east(Action):
    def __init__(self):
        super().__init__(method=Player.move_east, name='Move east', hotkey='d')
 
class move_west(Action):
    def __init__(self):
        super().__init__(method=Player.move_west, name='Move west', hotkey='a')

class search(Action):
    def __init__(self):
        super().__init__(method=Player.search, name='Search', hotkey='e')
 
class fight(Action):
    def __init__(self, enemy):
        super().__init__(method=Player.fight, name="Fight", hotkey="f", enemy=enemy)

class potion(Action):
    def __init__(self):
        super().__init__(method=Player.use_potion, name="Use Potion", hotkey="p")

class unlock(Action):
    def __init__(self, room):
        super().__init__(method=Player.unlock, name="Unlock", hotkey="q", room=room)

class buy(Action):
    def __init__(self, shopkeep):
        super().__init__(method=Player.buy, name="Buy", hotkey="b", shopkeep=shopkeep)

class menu(Action):
    def __init__(self):
        super().__init__(method=Player.menu, name="Menu", hotkey="m")

class SaveAndExit(Action):
    def __init__(self):
        super().__init__(method=Player.save_game, name="Save and Exit", hotkey='x')
