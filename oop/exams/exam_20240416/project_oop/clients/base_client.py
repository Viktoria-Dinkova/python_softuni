from abc import ABC, abstractmethod
from typing import Tuple


class BaseClient(ABC):
    VALID_MEMBERSHIP_TYPE = ["Regular", "VIP"]
    DISCOUNT_PERCENTAGE = 0
    EARNED_POINTS = 0

    def __init__(self, name: str, membership_type: str):
        self.name = name
        self.membership_type = membership_type
        self.points: int = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError(f"Client name should be determined!")
        self.__name = value

    @property
    def membership_type(self):
        return self.__membership_type

    @membership_type.setter
    def membership_type(self, value):
        if value not in self.VALID_MEMBERSHIP_TYPE:
            raise ValueError(f"Invalid membership type. Allowed types: Regular, VIP.")
        self.__membership_type = value

    @abstractmethod
    def earning_points(self, order_amount: float) -> int:
        pass

    def apply_discount(self) -> (int, int):
        if self.points >= 100:
            self.DISCOUNT_PERCENTAGE = 10
            self.points -= 100

        elif 50 <= self.points < 100:
            self.DISCOUNT_PERCENTAGE = 5
            self.points -= 50

        return (self.DISCOUNT_PERCENTAGE, self.points)
