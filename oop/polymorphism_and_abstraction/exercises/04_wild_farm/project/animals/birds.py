from project.animals.animal import Bird
from project.food import Meat, Fruit, Vegetable, Seed


class Owl(Bird):

    @property
    def weight_increase(self):
        return 0.25

    @staticmethod
    def make_sound() -> str:
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]


class Hen(Bird):

    @property
    def weight_increase(self):
        return 0.35

    @staticmethod
    def make_sound() -> str:
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Fruit, Vegetable, Seed]
