from abc import ABC
from typing import List

from exams.exam_20210815.project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people: int = 0
        self.is_reserved: bool = False

    def reserve(self, number_of_people: int) -> None:
        self.number_of_people += number_of_people

    def order_food(self, baked_food: BakedFood) -> None:
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink) -> None:
        self.drink_orders.append(drink)

    def get_bill(self) -> float:
        bill = 0
        bill += sum((f.price * self.number_of_people for f in self.food_orders))
        bill += sum((d.price * self.number_of_people for d in self.drink_orders))

        return bill

    def clear(self) -> None:
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    def free_table_info(self):
        if self.is_reserved:
            return (f"Table: {self.table_number}\n"
                    f"Type: {self.__class__.__name__}\n"
                    f"Capacity: {self.capacity}")


