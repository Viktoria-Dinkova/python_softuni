"""
Create a class called Hero. Upon initialization, it should receive a username (string) and health (number).
Create two additional methods:
•	defend(damage) - reduce the given damage from the hero's health:
o	if the health becomes 0 or less, set it to 0 and return "{username} was defeated"
•	heal(amount) - increase the health of the hero with the given amount
"""


class Hero:
    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    def defend(self, changes):
        self.health -= changes
        if self.health <= 0:
            self.health = 0
            return f"{self.name} was defeated"

    def heal(self, changes):
        self.health += changes


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))
