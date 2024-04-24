from abc import abstractmethod


class FormulaTeam:
    MIN_BUDGET_FOR_INCLUDE: int = 1000000

    def __init__(self, budget: int):
        self.budget = budget
        
    @property
    @abstractmethod
    def sponsors(self):
        pass

    @property
    @abstractmethod
    def expenses(self) -> int:
        pass

    @property
    def budget(self):
        return self.__budget

    @budget.setter
    def budget(self, value):
        if value < FormulaTeam.MIN_BUDGET_FOR_INCLUDE:
            raise ValueError("F1 is an expensive sport, find more sponsors!")

        self.__budget = value

    @abstractmethod
    def calculate_revenue_after_race(self, race_pos: int):
        revenue = -self.expenses

        for awards in self.sponsors.values():  # [{1: 1_500_000, 2: 800_000}, {8: 20_000, 10: 10_000}]
            for place in awards: # {1: 1_500_000, 2: 800_000} - should be sorted
                if race_pos <= place:
                    revenue += awards[place]
                    break

        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
