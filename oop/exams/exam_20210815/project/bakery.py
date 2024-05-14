from typing import List

from exams.exam_20210815.project.baked_food.bread import Bread
from exams.exam_20210815.project.baked_food.cake import Cake
from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class Bakery:
    VALID_FOODS = {"Bread": Bread,
                   "Cake": Cake,
                   }

    VALID_DRINKS = {"Tea": Tea,
                    "Water": Water,
                    }

    VALID_TABLES = {"InsideTable": InsideTable,
                    "OutsideTable": OutsideTable,
                    }

    def __init__(self, name: str):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income: float = 0.0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float) -> str:
        food = self._find_food(name)
        if food:
            raise Exception(f"{food_type} {name} is already in the menu!")

        food = self.VALID_FOODS[food_type](name=name, price=price)
        self.food_menu.append(food)

        return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str) -> str:
        drink = self._find_drink(name)
        if drink:
            raise Exception(f"{drink_type} {name} is already in the menu!")

        drink = self.VALID_DRINKS[drink_type](name=name, portion=portion, brand=brand)
        self.drinks_menu.append(drink)

        return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int) -> str:
        table = self._find_table(table_number)
        if table:
            raise Exception(f"Table {table_number} is already in the bakery!")

        table = self.VALID_TABLES[table_type](table_number=table_number, capacity=capacity)
        self.tables_repository.append(table)

        return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int) -> str:
        table = [t for t in self.tables_repository if not t.is_reserved and t.capacity >= number_of_people]

        if not table:
            return f"No available table for {number_of_people} people"

        reserved_table = table[0]
        reserved_table.is_reserved = True
        reserved_table.number_of_people += number_of_people

    def order_food(self, table_number: int, *food_names):
        table = self._find_table(table_number)
        if not table:
            f"Could not find table {table_number}"

        result = [f"Table {table_number} ordered:"]

        for wish_food in food_names:
            in_menu = []
            not_in_menu = []
            if wish_food in self.food_menu:
                in_menu.append(self._find_food(wish_food))
            not_in_menu.append(wish_food)

        for inf in in_menu:
            result.append(inf.__repr__())

        result.append(f"{self.name} does not have in the menu:")
        for notinf in not_in_menu:
            result.append(notinf)

        return '\n'.join(result)

    def leave_table(self, table_number: int) -> str:
        table = self._find_table(table_number)

        table_bill = table.get_bill()
        self.total_income += table_bill
        table.clear()
        return f"Table: {table_number}\nBill: {table_bill}"

    def get_free_tables_info(self):
        result = [repr(t) for t in self.tables_repository if not t.is_reserved]

        return '\n'.join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def _find_food(self, name) -> BakedFood:
        try:
            return next(filter(lambda f: f.name == name, self.food_menu))
        except StopIteration:
            pass

    def _find_drink(self, name) -> Drink:
        try:
            return next(filter(lambda d: d.name == name, self.drinks_menu))
        except StopIteration:
            pass

    def _find_table(self, number) -> Table:
        try:
            return next(filter(lambda t: t.table_number == number, self.tables_repository))
        except StopIteration:
            pass
