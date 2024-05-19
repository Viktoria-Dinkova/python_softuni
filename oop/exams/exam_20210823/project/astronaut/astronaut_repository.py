from typing import List

from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: List[Astronaut] = []

    def add(self, astronaut: Astronaut) -> None:
        self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut) -> None:
        self.astronauts.remove(astronaut)

    def find_by_name(self, name: str) -> Astronaut or None:
        try:
            return next(filter(lambda a: a.name == name, self.astronauts))
        except StopIteration:
            pass
