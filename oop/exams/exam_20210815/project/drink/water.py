from project.drink.drink import Drink


class Water(Drink):
    INITIAL_PRICE = 1.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.INITIAL_PRICE, brand)

    def __repr__(self):
        pass
