from typing import List

from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets: List[Planet] = []

    def add(self, planet: Planet) -> None:
        self.planets.append(planet)

    def remove(self, planet: Planet) -> None:
        self.planets.remove(planet)

    def find_by_name(self, name: str) -> Planet or None:
        try:
            return next(filter(lambda p: p.name == name, self.planets))
        except StopIteration:
            pass
