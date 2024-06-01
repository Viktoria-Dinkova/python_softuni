from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    MAXIMUM_SPEED = 120
    SPEED_INCREASE = 2

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self) -> None:
        self.speed += self.SPEED_INCREASE
        if self.speed < self.MAXIMUM_SPEED:
            self.speed = self.MAXIMUM_SPEED

