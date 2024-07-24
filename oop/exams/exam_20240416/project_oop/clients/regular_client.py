from project.clients.base_client import BaseClient


class RegularClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, "Regular")

    def earning_points(self, order_amount: float) -> int:
        multiplayer = order_amount / 10
        self.EARNED_POINTS = int(1 * multiplayer)
        self.points += self.EARNED_POINTS

        return self.EARNED_POINTS
