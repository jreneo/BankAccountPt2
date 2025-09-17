from BankAccountPt2.main import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, name, balance, min_bal, routing_number, account_number, transfer_limit):
        BankAccount.__init__(self, name, balance, min_bal, routing_number, account_number)

        self.transfer_limit = transfer_limit