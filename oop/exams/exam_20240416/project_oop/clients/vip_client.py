from project.clients.base_client import BaseClient


class VIPClient(BaseClient):

    def __init__(self, name: str):
        super().__init__(name, "VIP")

    def earning_points(self, order_amount: float) -> int:
        multiplayer = order_amount / 5
        self.EARNED_POINTS = int(1 * multiplayer)
        self.points += self.EARNED_POINTS

        return self.EARNED_POINTS
