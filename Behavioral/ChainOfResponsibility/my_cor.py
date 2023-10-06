from abc import ABC
from enum import Enum

class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, *kwargs)
            
class CreatureAttributes(Enum):
    ATTACK = 1
    DEFENSE = 2
    
class Query:
    def __init__(self, creature_name, creature_attribute, default_value):
        self.value = default_value
        self.creature_attribute = creature_attribute
        self.creature_name = creature_name
        
class Creature(ABC):
    def __init__(self, game, name, attack, defense):
        self.init_defense = defense
        self.init_attack = attack
        self.name = name
        self.game = game

    @property
    def attack(self):
        pass
        
    @property
    def defense(self):
        pass
    

class Goblin(Creature):
    def __init__(self, game, name="Goblin", attack=1, defense=1):
        super().__init__(game, name, attack, defense)
        GoblinModifier(game, self)

    @property
    def attack(self):
        q = Query(self.name, CreatureAttributes.ATTACK, self.init_attack)
        self.game.perform_events(self, q)
        return q.value
        
    @property
    def defense(self):
        q = Query(self.name, CreatureAttributes.DEFENSE, self.init_attack)
        self.game.perform_events(self, q)
        return q.value
        
        
class GoblinKing(Goblin):
    def __init__(self, game):
        super().__init__(game, "Goblin King", 3, 3)
        GoblinKingModifier(game, self)

class Game:
    def __init__(self):
        self.creatures = []
        self.events = Event()
        
    def perform_events(self, sender, query):
        self.events(sender, query)
        
class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.events.append(self.handle)
        
    def handle(self):
        pass
    
class GoblinKingModifier(CreatureModifier):
    def __init__(self, game, creature):
        super().__init__(game, creature)
        
    def handle(self, sender, query):
        if sender.name == self.creature.creature_name and query.creature_attribute == CreatureAttributes.ATTACK:
            query.value += 1
        elif sender.name == self.creature.creature_name and query.creature_attribute == CreatureAttributes.DEFENSE:
            query.value += 1
            
class GoblinModifier(CreatureModifier):
    def __init__(self, game, creature):
        super().__init__(game, creature)
        
    def handle(self, sender, query):
        if sender.name == self.creature.creature_name and query.creature_attribute == CreatureAttributes.DEFENSE:
            query.value += 1
        