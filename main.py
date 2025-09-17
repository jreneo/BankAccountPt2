from bank_account import BankAccount

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