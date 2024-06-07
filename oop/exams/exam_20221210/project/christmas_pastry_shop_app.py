from typing import List

from project.booths.booth import Booth
from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.delicacy import Delicacy
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACY_TYPE = {"Gingerbread": Gingerbread,
                           "Stolen": Stolen
                           }
    VALID_BOOTH_TYPE = {"Open Booth": OpenBooth,
                        "Private Booth": PrivateBooth
                        }

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0.0

    def find_delicacy(self, name: str) -> Delicacy or None:
        try:
            return next(filter(lambda d: d.name == name, self.delicacies))
        except StopIteration:
            pass

    def find_booth(self, number: int) -> Booth or None:
        try:
            return next(filter(lambda b: b.booth_number == number, self.booths))
        except StopIteration:
            pass

    def add_delicacy(self, type_delicacy: str, name: str, price: float) -> str:

        if type_delicacy not in self.VALID_DELICACY_TYPE:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        if self.find_delicacy(name):
            raise Exception(f"{name} already exists!")

        delicacy = self.VALID_DELICACY_TYPE[type_delicacy](name, price)
        self.delicacies.append(delicacy)

        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int) -> str:

        if type_booth not in self.VALID_BOOTH_TYPE:
            raise Exception(f"{type_booth} is not a valid booth!")

        if self.find_booth(booth_number):
            raise Exception(f"Booth number {booth_number} already exists!")

        booth = self.VALID_BOOTH_TYPE[type_booth](booth_number, capacity)
        self.booths.append(booth)

        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int) -> str:
        try:
            booth = next(filter(lambda b: not b.is_reserved and b.capacity >= number_of_people, self.booths))
        except StopIteration:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def order_delicacy(self, booth_number: int, delicacy_name: str) -> str or None:

        booth = self.find_booth(booth_number)
        delicacy = self.find_delicacy(delicacy_name)

        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self.find_booth(booth_number)

        bill_for_that_booth = booth.price_for_reservation + sum(d.price for d in booth.delicacy_orders)
        self.income += bill_for_that_booth

        booth.delicacy_orders.clear()
        booth.price_for_reservation = 0
        booth.is_reserved = False

        return f"Booth {booth_number}:\n" \
               f"Bill: {bill_for_that_booth:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."
