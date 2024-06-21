from typing import List

from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": [StudentLoan, 'Student'],
                        "MortgageLoan": [MortgageLoan, 'Adult'],
                        }

    VALID_CLIENT_TYPES = {"Student": Student,
                          "Adult": Adult,
                          }

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str) -> str:
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOAN_TYPES[loan_type][0]()
        self.loans.append(loan)

        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float) -> str:
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")

        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."

        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)

        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str) -> str:
        client = next(filter(lambda c: c.client_id == client_id, self.clients))
        loan = next(filter(lambda l: l.__class__.__name__ == loan_type, self.loans))

        if client.__class__.__name__ != self.VALID_LOAN_TYPES[loan_type][1]:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)

        return f"Successfully granted {loan_type} to {client.name} with ID {client.client_id}."

    def remove_client(self, client_id: str) -> str or Exception:
        try:
            client = next(filter(lambda c: c.client_id == client_id, self.clients))
        except:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client.client_id}."

    def increase_loan_interest(self, loan_type: str) -> str:
        affected_loans = [al for al in self.loans if al.__class__.__name__ == loan_type]

        for curr_al in affected_loans:
            curr_al.increase_interest_rate()

        return f"Successfully changed {len(affected_loans)} loans."

    def increase_clients_interest(self, min_rate: float) -> str:
        affected_clients = [ac for ac in self.clients if ac.interest < min_rate]

        for curr_ac in affected_clients:
            curr_ac.increase_clients_interest()

        return f"Number of clients affected: {len(affected_clients)}."

    def get_statistics(self):
        result = [f"Active Clients: {len(self.clients)}",
                  f"Total Income: {sum(c.income for c in self.clients):.2f}"
                  ]

        loans_count_granted_to_clients = 0
        granted_sum = 0
        sum_interest_rate = 0

        # granted loans
        for c in self.clients:
            loans_count_granted_to_clients += len(c.loans)  # count of loans by client
            for l in c.loans:
                granted_sum += l.amount

        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0

        result.append(f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}")
        result.append(f"Available Loans: {len(self.loans)}, Total Sum: {sum(al.amount for al in self.loans):.2f}")
        result.append(f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

        return '\n'.join(result)