import random
import math


class Fighter:
    def __init__(self, name, health, strength, block):
        self.name = name
        self.health = health
        self.strength = strength
        self.block = block

    @property
    def name(self):
        return self.__name

    @property  # getter
    def health(self):
        return self.__health

    @property
    def strength(self):
        return self.__strength

    @property
    def block(self):
        return self.__block

    @name.setter
    def name(self, value):
        self.__name = value

    @health.setter
    def health(self, value):
        self.__health = value

    @strength.setter
    def strength(self, value):
        self.__strength = value

    @block.setter
    def block(self, value):
        self.__block = value

    def attack(self):
        return math.floor(random.random() * self.__strength)  # random.random() gets a random number between 0 and 1

    def getBlock(self):
        return math.floor(random.random() * self.__block)


class Battle:
    @staticmethod  # used for methods that don't use 'self'  (i think)
    def getAttack(attacker, defender):
        attack = attacker.attack()
        block = defender.getBlock()
        damage = attack - block
        if damage >= 0:
            defender.health -= damage

        print("{} attacked with {} force!".format(attacker.name, attack))
        print("{} blocked with {} block!".format(defender.name, block))
        print("{}'s health -> {}".format(defender.name, defender.health))
        print()

        if defender.health <= 0:
            print("{} has died, {} is victorious!".format(defender.name, attacker.name))
            return "Game Over"
        else:
            return "the fight will continue!"

    def battle(self, fighter1, fighter2):
        while True:
            if self.getAttack(fighter1, fighter2) == "Game Over":
                print("Game Over")
                break
            if self.getAttack(fighter2, fighter1) == "Game Over":
                print("Game Over")
                break
