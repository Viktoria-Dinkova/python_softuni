from project.clients.base_client import BaseClient


class Adult(BaseClient):

    @property
    def get_initial_interest(self) -> float:
        return 4.0  # 4.0 percent

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, self.get_initial_interest)

    def increase_clients_interest(self) -> float:
        return self.interest + 2.0  # increases the client’s interest by 2.0 percent
