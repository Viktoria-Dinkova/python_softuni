from abc import ABC
from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam, ABC):

    @property
    def expenses(self) -> int:
        return 250000

    @property
    def sponsors(self):
        return {
            "Oracle": {
                1: 1500000,
                2: 800000
            },

            "Honda": {
                8: 20000,
                10: 10000
            }

        }



