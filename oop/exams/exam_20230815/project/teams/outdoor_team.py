from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    @property
    def get_budget(self):
        return 1000.0

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, self.get_budget)

    def win(self) -> None:
        self.wins += 1
        self.advantage += 115
