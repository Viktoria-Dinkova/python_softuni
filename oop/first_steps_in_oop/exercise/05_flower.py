"""
Create a class called Flower. Upon initialization, the class should receive a username (string) and a water_requirements (number).
The flower should also have an instance attribute called is_happy (False by default).
Add two additional methods to the class:
-	water(quantity) - it will water the flower. Each time check if the quantity is greater than or equal to the required.
If it is - the flower becomes happy (set is_happy to True).
-	status() - it should return "{username} is happy" if the flower is happy, otherwise it should return "{username} is not happy".
Submit only the class in the judge system.
"""


class Flower:

    is_happy = False

    def __init__(self, name: str, water_requirements: int):
        self.name = name
        self.water_requirements = water_requirements

    def water(self, quantity: int) -> None:
        if quantity >= self.water_requirements:
            self.is_happy = True

    def status(self):
        if self.is_happy:
            return f"{self.name} is happy"
        else:
            return f"{self.name} is not happy"


flower = Flower("Lilly", 100)
flower.water(50)
print(flower.status())
flower.water(60)
print(flower.status())
flower.water(100)
print(flower.status())

