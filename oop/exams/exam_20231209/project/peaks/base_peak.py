from abc import ABC, abstractmethod
from typing import List


class BasePeak(ABC):

    @property
    def get_min_name_len(self):
        return 2

    @property
    def get_min_elevation(self):
        return 1500

    def __init__(self, name: str, elevation: int):
        self.name = name
        self.elevation = elevation
        self.difficulty_level = self.calculate_difficulty_level()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < self.get_min_name_len:
            raise ValueError(f"Peak name cannot be less than {self.get_min_name_len} symbols!")
        self.__name = value

    @property
    def elevation(self):
        return self.__elevation

    @elevation.setter
    def elevation(self, value):
        if value < self.get_min_elevation:
            raise ValueError(f"Peak elevation cannot be below {self.get_min_elevation}m.")
        self.__elevation = value

    @abstractmethod
    def get_recommended_gear(self) -> List[str]:
        pass

    @abstractmethod
    def calculate_difficulty_level(self) -> str:
        pass
