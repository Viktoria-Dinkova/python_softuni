from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):

    @property
    def get_interest_rate(self) -> float:
        return 3.5  # 3.5%

    @property
    def get_amount(self) -> float:
        return 50000.0

    def __init__(self):
        super().__init__(self.get_interest_rate, self.get_amount)

    def increase_interest_rate(self) -> float:
        return self.get_interest_rate + 0.5  # The method increases the interest rate by 0.5 percent
