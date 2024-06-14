from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    INITIALLY_WEIGHT = 9
    INCREASE_WEIGHT = 3

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, MaleRobot.INITIALLY_WEIGHT)

    def eating(self) -> None:
        self.weight += MaleRobot.INCREASE_WEIGHT
