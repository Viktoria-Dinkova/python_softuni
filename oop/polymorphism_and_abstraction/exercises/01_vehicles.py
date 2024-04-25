from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity: float, fuel_consumption: float):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance: float) -> None:
        pass

    @abstractmethod
    def refuel(self, fuel: float) -> None:
        pass


class Car(Vehicle):
    CONSUMPTION_INCREASE = 0.9

    def drive(self, distance: float):
        fuel_change = (self.fuel_consumption + self.CONSUMPTION_INCREASE) * distance

        if self.fuel_quantity >= fuel_change:
            self.fuel_quantity -= fuel_change

    def refuel(self, fuel: float):
        self.fuel_quantity += fuel


class Truck(Vehicle):

    CONSUMPTION_INCREASE = 1.6
    TANK_HOL_DECREASE = 0.95

    def drive(self, distance: float) -> None:
        fuel_change = (self.fuel_consumption + self.CONSUMPTION_INCREASE) * distance

        if self.fuel_quantity >= fuel_change:
            self.fuel_quantity -= fuel_change

    def refuel(self, fuel: float) -> None:
        self.fuel_quantity += fuel * self.TANK_HOL_DECREASE



# car = Car(20, 5)
# car.drive(3)
# print(car.fuel_quantity)
# car.refuel(10)
# print(car.fuel_quantity)
# truck = Truck(100, 15)
# truck.drive(5)
# print(truck.fuel_quantity)
# truck.refuel(50)
# print(truck.fuel_quantity)
