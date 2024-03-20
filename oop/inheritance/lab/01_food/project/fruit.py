"""
•	In the fruit.py file, create a class called Fruit which will receive a username (str) and an expiration_date (str) upon initialization.
"""
from project.food import Food


class Fruit(Food):
    def __init__(self, name: str, expiration_data: str):
        super().__init__(expiration_data)
        self.name = name