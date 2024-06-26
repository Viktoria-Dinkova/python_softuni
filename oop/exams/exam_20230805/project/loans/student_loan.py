from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    @property
    def get_interest_rate(self) -> float:
        return 1.5  # 1.5%

    @property
    def get_amount(self) -> float:
        return 2000.0

    def __init__(self):
        super().__init__(interest_rate=self.get_interest_rate, amount=self.get_amount)

    def increase_interest_rate(self) -> float:
        return self.get_interest_rate + 0.2  # The method increases the interest rate by 0.2 percent
