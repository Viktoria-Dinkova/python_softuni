from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    VALID_ASTRONAUT_TYPES = {"Biologist": Biologist,
                             "Geodesist": Geodesist,
                             "Meteorologist": Meteorologist
                             }
    SUCCESSFUL_MISSIONS = 0
    NOT_COMPLETED_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str) -> str:
        if astronaut_type not in self.VALID_ASTRONAUT_TYPES:
            raise Exception("Astronaut type is not valid!")

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = self.VALID_ASTRONAUT_TYPES[astronaut_type](name)
        self.astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str) -> str:
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = Planet(name)
        planet.items = items.split(', ')
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str) -> str:
        astronaut = self.astronaut_repository.find_by_name(name)
        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self) -> None:
        for ca in self.astronaut_repository.astronauts:
            ca.increase_oxygen(10)

    def send_on_mission(self, planet_name: str) -> str:
        planet = self.planet_repository.find_by_name(planet_name)
        if not planet:
            raise Exception("Invalid planet name!")

        suitable = [sa for sa in self.astronaut_repository.astronauts if sa.oxygen > 30]
        if not suitable:
            raise Exception("You need at least one astronaut to explore the planet!")

        sorted(suitable, key=lambda ca: (-ca.oxygen))

        number_of_astronauts = 0
        for i in range(5):
            outgoing_astronaut = suitable[i]
            number_of_astronauts += 1
            for j in range(len(planet.items)):
                outgoing_astronaut.backpack.append(planet.items.pop())
                outgoing_astronaut.breathe()
                if outgoing_astronaut.oxygen <= 0:
                    break

                if not planet.items:
                    self.SUCCESSFUL_MISSIONS += 1
                    return f"Planet: {planet_name} was explored. {number_of_astronauts} astronauts participated in collecting items."

        self.NOT_COMPLETED_MISSIONS += 1
        return "Mission is not completed."

    def report(self):
        result = [f"{self.SUCCESSFUL_MISSIONS} successful missions!",
                  f"{self.NOT_COMPLETED_MISSIONS} missions were not completed!",
                  f"Astronauts' info:"]

        for ra in self.astronaut_repository.astronauts:
            result.append(f"Name: {ra.name}")
            result.append(f"Oxygen: {ra.oxygen}")
            result.append(f"Backpack items: {', '.join(ra.backpack)}")

        return '\n'.join(result)
