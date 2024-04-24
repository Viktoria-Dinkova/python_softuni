from abc import ABC

from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam (FormulaTeam, ABC):

    @property
    def expenses(self) -> int:
        return 200000

    @property
    def sponsors(self):
        return {
            "Petronas": {
                1: 1000000,
                3: 500000
            },

            "TeamViewer": {
                5: 100000,
                7: 50000
            }
        }
