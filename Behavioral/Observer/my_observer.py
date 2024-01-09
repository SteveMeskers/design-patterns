class Game:
    def __init__(self):
        self.events = Events()
        self.rats_total_attack = 0
        self.events.append(self.total_attack)

    def total_attack(self, value):
        self.rats_total_attack += value

class Rat:
    def __init__(self, game):
        self.game = game
        self.game.events(1)

    @property
    def attack(self):
        return self.game.rats_total_attack

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.game.events(-1)

class Events(list):
    def __call__(self, *args):
        for item in self:
            item(*args)
