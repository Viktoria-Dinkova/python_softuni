from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    INITIAL_OXYGEN_UNITS = 70
    OXYGEN_DECREASE_UNITS = 5

    def __init__(self, name: str):
        super().__init__(name, self.INITIAL_OXYGEN_UNITS)

    def breathe(self) -> None:
        self.oxygen -= self.OXYGEN_DECREASE_UNITS
