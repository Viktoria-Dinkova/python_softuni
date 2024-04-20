from abc import ABC

from project.animals.animal import Animal, Mammal
from project.food import Fruit, Meat, Vegetable


class Mouse(Mammal, ABC):

    @staticmethod
    def make_sound() -> str:
        return "Squeak"

    @property
    def food_that_eats(self):
        return [Fruit, Vegetable]

    @property
    def weight_increase(self):
        return 0.10


class Dog(Mammal, ABC):

    @staticmethod
    def make_sound() -> str:
        return "Woof!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 0.40


class Cat(Mammal, ABC):

    @staticmethod
    def make_sound() -> str:
        return "Meow"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable]

    @property
    def weight_increase(self):
        return 0.30


class Tiger(Mammal, ABC):

    @staticmethod
    def make_sound() -> str:
        return "ROAR!!!"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def weight_increase(self):
        return 1.00
