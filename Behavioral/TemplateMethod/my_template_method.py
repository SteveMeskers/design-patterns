from abc import ABC

class Creature:
    def __init__(self, attack, health):
        self.health = health
        self.attack = attack

class CardGame(ABC):
    def __init__(self, creatures):
        self.creatures = creatures

    # return -1 if both creatures alive or both dead after combat
    # otherwise, return the _index_ of winning creature
    def combat(self, c1_index, c2_index):
        winnder_index = -1
        c1 = self.creatures[c1_index]
        c2 = self.creatures[c2_index]
        c2_health = self.hit(c1, c2)
        c1_health = self.hit(c2, c1)

        if c1_health > 0 and c2_health <= 0:
            winnder_index = c1_index
        elif c2_health > 0 and c1_health <= 0:
            winnder_index = c2_index

        return winnder_index

    def hit(self, attacker, defender):
        pass  # implement this in derived classes


class TemporaryDamageCardGame(CardGame):
    def __init__(self, creatures):
        super().__init__(creatures)

    def hit(self, attacker, defender):
        health = defender.health
        health -= attacker.attack
        return health


class PermanentDamageCardGame(CardGame):
    def __init__(self, creatures):
        super().__init__(creatures)

    def hit(self, attacker, defender):
        defender.health -= attacker.attack
        return defender.health
