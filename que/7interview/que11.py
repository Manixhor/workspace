class BankError(Exception):
    def __init__(self,message):
        self.message = message 
        super().__init__(self.message)

class BankAccount:
    def __init__(self,account_num,balance):
        self.account_num = account_num
        self.balance = balance

    def withdraw(self,amount):
        if amount > self.balance:
            raise BankError("Insufficient funds!")
        self.balance -= amount
        print(f"withdraw {amount}. Remaining balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise BankError("Deposit amount must be positive!")
        self.balance += amount
        print(f"Deposited {amount}. Current balance: {self.balance}")
my_account = BankAccount("12345", 1000)

try:
    my_account.withdraw(1500)
except BankError as e:
    print("Bank Error:", e)
try:
    my_account.deposit(-50)
except BankError as e:
    print("Bank Error:", e)
