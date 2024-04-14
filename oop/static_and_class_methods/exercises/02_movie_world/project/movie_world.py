from typing import List

from project.customer import Customer
from project.dvd import DVD


class MovieWorld :
    DVDS_COLLECTION_CAPACITY = 15
    CUSTOMERS_COLLECTION_CAPACITY = 10

    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @classmethod
    def dvd_capacity(cls) -> int:

        return cls.DVDS_COLLECTION_CAPACITY

    @classmethod
    def customer_capacity(cls) -> int:
        return cls.CUSTOMERS_COLLECTION_CAPACITY

    def add_customer(self, customer: Customer) -> None:
        if self.CUSTOMERS_COLLECTION_CAPACITY > len(self.customers):
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD) -> None:
        if self.DVDS_COLLECTION_CAPACITY > len(self.dvds):
            self.dvds.append(dvd)

    def find_customer(self, c_id: int) -> Customer:
        return next(filter(lambda c: c.id == c_id, self.customers))

    def find_dvd(self, d_id: int) -> Customer:
        return next(filter(lambda d: d.id == d_id, self.dvds))

    def rent_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)

        if dvd.is_rented and dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        elif dvd.is_rented:
            return "DVD is already rented"

        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        else:
            dvd.is_rented = True
            customer.rented_dvds.append(dvd)

            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id: int, dvd_id: int) -> str:
        customer = self.find_customer(customer_id)
        dvd = self.find_dvd(dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        else:
            dvd.is_rented = False
            customer.rented_dvds.remove(dvd)

            return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = '\n'.join(str(c) for c in self.customers)
        result += '\n'
        result += '\n'.join(str(d) for d in self.dvds)
        return result

