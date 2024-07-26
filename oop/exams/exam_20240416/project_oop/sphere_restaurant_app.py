from typing import List

from project.clients.base_client import BaseClient
from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.base_waiter import BaseWaiter
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITER_TYPE = {"FullTimeWaiter": FullTimeWaiter,
                         "HalfTimeWaiter": HalfTimeWaiter
                         }

    VALID_CLIENT_TYPE = {"RegularClient": RegularClient,
                         "VIPClient": VIPClient
                         }

    def __init__(self):
        self.waiters: List[BaseWaiter] = []
        self.clients: List[BaseClient] = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int) -> str:
        if waiter_type not in self.VALID_WAITER_TYPE:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = self._find_waiter_by_name(waiter_name)
        if waiter:
            return f"{waiter_name} is already on the staff."

        waiter = self.VALID_WAITER_TYPE[waiter_type](waiter_name, hours_worked)
        self.waiters.append(waiter)

        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str) -> str:
        if client_type not in self.VALID_CLIENT_TYPE:
            return f"{client_type} is not a recognized client type."

        client = self._find_client_by_name(client_name)
        if client:
            return f"{client_name} is already a client."

        client = self.VALID_CLIENT_TYPE[client_type](client_name)
        self.clients.append(client)

        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str) -> str:
        waiter = self._find_waiter_by_name(waiter_name)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float) -> str:
        client = self._find_client_by_name(client_name)
        if not client:
            return f"{client_name} is not a registered client."

        points = client.earning_points(order_amount)
        return f"{client_name} earned {points} points from the order."

    def apply_discount_to_client(self, client_name: str) -> str:
        client = self._find_client_by_name(client_name)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_details = client.apply_discount()
        return f"{client_name} received a {discount_details[0]}% discount. Remaining points {discount_details[1]}"

    def generate_report(self) -> str:
        total_earnings = sum([w.calculate_earnings() for w in self.waiters])
        total_clients_unused_points = sum([c.points for c in self.clients])

        result = [f"$$ Monthly Report $$",
                  f"Total Earnings: ${total_earnings:.2f}",
                  f"Total Clients Unused Points: {total_clients_unused_points}",
                  f"Total Clients Count: {len(self.clients)}", f"** Waiter Details **"]

        self.waiters = sorted(self.waiters, key=lambda w: -w.calculate_earnings())
        for curr_w in self.waiters:
            result.append(str(curr_w))

        return '\n'.join(result)

    # helper
    def _find_waiter_by_name(self, waiter_name) -> (BaseWaiter, FullTimeWaiter, HalfTimeWaiter):
        try:
            return next(filter(lambda w: w.name == waiter_name, self.waiters))
        except StopIteration:
            pass

    def _find_client_by_name(self, client_name) -> (BaseClient, RegularClient, VIPClient):
        try:
            return next(filter(lambda c: c.name == client_name, self.clients))
        except StopIteration:
            pass
