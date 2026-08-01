# Bank Account Manager

# creating a BankAcoount class that performs banking operations
class BankAccount:
    # self is current instance of the class
    #  __init__ function is the constructor that assigns values to variables
    #  automatically
    def __init__(self, name, acc_number, balance=0):
        self.name = name
        self.acc_number = acc_number
        self.balance = balance

    # deposit operation
    def deposit(self, amount):
        self.balance += amount

    # withdraw operation
    def withdraw(self, amount):
        if self.balance < amount:
            print(f"Oops! Insufficient balance for account: {self.acc_number}")
            return

        self.balance -= amount

    # printing account status
    def get_balance(self):
        print(f"Name: {self.name} | Balance: {self.balance}")


# provided input
accounts = [
    ("Ramesh Thapa", "A001", 5000),
    ("Sunita Karki", "A002", 0),
    ("Bikash Rai", "A003", 12000),
]

# creating objects from provided list of input
bank_accounts = {}  # initializing empty dictionary to create objects
for name, acc_number, balance in accounts:
    bank_accounts[acc_number] = BankAccount(name, acc_number, balance)
# dictionary format:
# A001: object1 (Ramesh Thapa, A001, 5000)

# perform respective transactions
bank_accounts["A002"].deposit(3000)  # Deposit Rs. 3000
bank_accounts["A003"].withdraw(15000)  # Should fail
bank_accounts["A001"].withdraw(2000)  # Withdraw Rs. 2000

# print final status
print("\nFinal Account Balances:")
for account in bank_accounts.values():
    account.get_balance()
