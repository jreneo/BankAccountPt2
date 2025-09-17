class BankAccount:

    bank_title = "ITSC-3155 Bank"

    def __init__(self, name, balance, min_bal):
        self.customer_name = name
        self.current_balance = balance
        self.minimum_balance = min_bal
        print("Initializing Bank Account")

    def deposit(self, amount):
        self.current_balance += amount

    def withdraw(self, amount):
        if self.current_balance - amount < self.minimum_balance:
            print("Balance cannot fall below minimum balance.")
        else:
            self.current_balance -= amount

    def print_customer_information(self):
        print("Bank Title: " + self.bank_title)
        print("Customer Name: " + str(self.customer_name))
        print("Minimum Balance: " + str(self.minimum_balance))
        print("Current Balance: " + str(self.current_balance) + "\n")

def main():
    ba1 = BankAccount("Medina Checking", 676767, 999999)
    ba2 = BankAccount("Medina Savings", 200, 190)

    ba1.print_customer_information()
    ba2.print_customer_information()

    print("----------------------")

    ba1.deposit(100)
    ba1.print_customer_information()
    ba1.withdraw(100)
    ba1.print_customer_information()

    print("----------------------")

    ba2.deposit(100)
    ba2.print_customer_information()
    ba2.withdraw(200)
    ba2.print_customer_information()

if __name__ == '__main__':
    main()