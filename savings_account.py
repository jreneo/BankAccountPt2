from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, min_bal, routing_number, account_number, interest):
        super().__init__(name, balance, min_bal, routing_number, account_number)
        self.interest = interest

    def get_interest(self):
        return self.interest * self.current_balance

    def add_interest(self, interest):
        self.current_balance += interest


