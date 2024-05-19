from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_DECREASE_UNITS = 10

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    @abstractmethod
    def breathe(self) -> None:
        self.oxygen -= self.OXYGEN_DECREASE_UNITS

    def increase_oxygen(self, amount: int) -> None:
        self.oxygen += amount
