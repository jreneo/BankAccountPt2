from bank_account import BankAccount
from savings_account import SavingsAccount


def main():
    print("-----------Scenario 1-----------")
    # Put your checking here


    print("-----------Scenario 2-----------")
    ba2 = SavingsAccount("Medina Savings", 200, 190,54321,12345,.02)
    ba2.deposit(100)
    ba2.print_customer_information()
    ba2.withdraw(200)
    ba2.print_customer_information()
    ba2.add_interest(ba2.get_interest())
    print(ba2.get_interest())
    ba2.print_customer_information()

if __name__ == '__main__':
    main()