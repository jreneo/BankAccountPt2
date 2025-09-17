from bank_account import BankAccount


class CheckingAccount(BankAccount):
    def __init__(self, name, balance, min_bal, routing_number, account_number, transfer_limit):
        BankAccount.__init__(self, name, balance, min_bal, routing_number, account_number)

        self.transfer_limit = transfer_limit

    def deposit(self, amount):
        if amount > self.transfer_limit:
            print("Cannot deposit more than your transfer limit.\n")
        else:
            BankAccount.deposit(self, amount)

    def withdraw(self, amount):
        if amount > self.transfer_limit:
            print("Cannot withdraw more than transfer limit.\n")
        else:
            BankAccount.withdraw(self, amount)