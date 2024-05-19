from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    INITIAL_OXYGEN_UNITS = 90
    OXYGEN_DECREASE_UNITS = 15

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_UNITS)

    def breathe(self) -> None:
        self.oxygen -= self.OXYGEN_DECREASE_UNITS
