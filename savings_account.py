from main import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, name, balance, min_bal, interest):
        super().__init__(name, balance, min_bal)
        self.interest = interest

    def add_interest(self, interest):
        self.interest += interest

    def get_interest(self):
        return self.interest * self.current_balance
