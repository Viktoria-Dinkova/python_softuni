"""
In a folder called project create three files: vehicle.py and car.py, and sports_car.py.
In each file, create its corresponding class - Vehicle, Car, and SportsCar:
•	Vehicle with a single method move() that returns: "moving..."
•	Car with a single method drive() that returns: "driving..."
•	SportsCar with a single method race() that returns: "racing...".
SportsCar should inherit from Car and Car should inherit from Vehicle.
"""
from project.animal import Animal


class Cat(Animal):

    def meow(self):
        return "meowing..."
