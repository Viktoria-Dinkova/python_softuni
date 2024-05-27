from project.supply.supply import Supply


class Drink(Supply):
    ENERGY_UNITS = 15

    def __init__(self, name: str, energy: int = ENERGY_UNITS):
        super().__init__(name, energy)

    def details(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
