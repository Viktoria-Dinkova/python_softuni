from typing import List


class Planet:
    UNIQUE_PLANETS_NAMES = []

    def __init__(self, name: str, ):
        self.name = name
        self.items: List[str] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Planet name cannot be empty string or whitespace!")
        self.__name = value
