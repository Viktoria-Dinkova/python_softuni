from project.waiters.base_waiter import BaseWaiter


class HalfTimeWaiter(BaseWaiter):

    def calculate_earnings(self) -> float:
        self.WAITER_EARNINGS = self.hours_worked * 12.0
        return self.WAITER_EARNINGS

    def report_shift(self):
        return f"{self.name} worked a half-time shift of {self.hours_worked} hours."
