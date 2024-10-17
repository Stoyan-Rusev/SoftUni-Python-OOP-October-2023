from typing import List
from project.clients.adult import Adult
from project.clients.base_client import BaseClient
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.mortgage_loan import MortgageLoan
from project.loans.student_loan import StudentLoan


class BankApp:
    VALID_LOAN_TYPES = {"StudentLoan": StudentLoan,
                        "MortgageLoan": MortgageLoan}
    VALID_CLIENT_TYPES = {"Student": Student,
                          "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOAN_TYPES:
            raise Exception("Invalid loan type!")

        loan = self.VALID_LOAN_TYPES[loan_type]()
        self.loans.append(loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENT_TYPES:
            raise Exception("Invalid client type!")
        if self.capacity <= len(self.clients):
            return "Not enough bank capacity."
        client = self.VALID_CLIENT_TYPES[client_type](client_name, client_id, income)
        self.clients.append(client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        valid_client_to_loan_cases = {'Student': 'StudentLoan',
                                      'Adult': 'MortgageLoan'}
        client = next((c for c in self.clients if c.client_id == client_id), None)
        loan = next((lo for lo in self.loans if lo.__class__.__name__ == loan_type), None)

        if valid_client_to_loan_cases[client.__class__.__name__] != loan.__class__.__name__:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = next((c for c in self.clients if c.client_id == client_id), None)
        if not client:
            raise Exception("No such client!")
        if len(client.loans) > 0:
            raise Exception("The client has loans! Removal is impossible!")
        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        number_of_changed_loans = 0
        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                number_of_changed_loans += 1
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1
        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        avg_client_interest_rate = sum([c.interest for c in self.clients]) / len(self.clients) \
            if len(self.clients) > 0 else 0

        result = (f"Active Clients: {len(self.clients)}\n"
                  f"Total Income: {sum([c.income for c in self.clients]):.2f}\n"
                  f"Granted Loans: {sum([len(c.loans) for c in self.clients]):}, "
                  f"Total Sum: {sum(loan.amount for client in self.clients for loan in client.loans):.2f}\n"
                  f"Available Loans: {len(self.loans)}, Total Sum: {sum([lo.amount for lo in self.loans]):.2f}\n"
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")
        return result
