from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CAR_TYPES = {"MuscleCar": MuscleCar,
                       "SportsCar": SportsCar
                       }

    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def create_car(self, car_type: str, model: str, speed_limit: int) -> str:
        if [c for c in self.cars if c.model == model]:
            raise Exception(f"Car {model} is already created!")

        car = self.VALID_CAR_TYPES[car_type](model, speed_limit)
        self.cars.append(car)
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str) -> str:
        driver = self._find_driver_by_name(driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str) -> str:
        race = self._find_race_by_name(race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str) -> str:
        driver = self._find_driver_by_name(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if car_type in self.VALID_CAR_TYPES:
            available_cars_for_type = [ac for ac in self.cars if ac.__class__.__name__ == car_type and not ac.is_taken]
            if not available_cars_for_type:
                raise Exception(f"Car {car_type} could not be found!")

            if driver.car:
                old_car = driver.car
                for cc in self.cars:
                    if cc == old_car:
                        cc.is_taken = False

                new_car = available_cars_for_type[-1]
                new_car.is_taken = True
                driver.car = new_car
                return f"Driver {driver_name} changed his car from {old_car.model} to {new_car.model}."

            new_car = available_cars_for_type[-1]
            new_car.is_taken = True
            driver.car = new_car
            return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str) -> str:
        driver = self._find_driver_by_name(driver_name)
        race = self._find_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str) -> str:
        race = self._find_race_by_name(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        rate = sorted(race.drivers, key=lambda d: -d.car.speed_limit)
        for i in range(3):
            cur_drive = rate[i]
            for self_d in self.drivers:
                if self_d == cur_drive:
                    self_d.number_of_wins += 1
                    break

        winner = rate[0]
        return f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}."



    """ helper"""
    def _find_driver_by_name(self, name) -> Driver:
        try:
            return next(filter(lambda d: d.name == name, self.drivers))
        except StopIteration:
            pass

    def _find_race_by_name(self, name) -> Race:
        try:
            return next(filter(lambda r: r.name == name, self.races))
        except StopIteration:
            pass

