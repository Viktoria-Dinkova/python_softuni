from project.drink.drink import Drink


class Tea(Drink):
    INITIAL_PRICE = 2.5

    def __init__(self, name: str, portion: float, brand: str):
        super().__init__(name, portion, self.INITIAL_PRICE, brand)

    def __repr__(self):
        pass
