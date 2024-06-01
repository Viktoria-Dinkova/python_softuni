from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    MAXIMUM_SPEED = 140
    SPEED_INCREASE = 3

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self) -> None:
        self.speed += self.SPEED_INCREASE
        if self.speed < self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED

