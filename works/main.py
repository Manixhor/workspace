
balance = 0.0
transactions = []

def deposit(amount):
    global balance

    balance += amount
    transactions.append(f"Deposited {amount}/-")
    print(f'₹{amount} deposited successfully\n')

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance\n")
    else:
        balance -= amount
        transactions.append(f"withdrawn {amount}/-")
        print(f"₹{amount} withdrawn successfully\n")
        print(f"your balance is {balance}\n")
def checkbalance():
    print(f"Current Balance: ₹{balance}/-\n")

def tranactionhistory():
    if not transactions:
        print("NO Transaction's occurred.")
    else:
        print("-----Transactions history-----")
        for t in transactions:
            print("-",t)
        deposits = sum(1 for t in transactions if 'Deposited' in t)
        withdraws = sum(1 for t in transactions if 'withdrawn' in t)
        print(f'\n Total Deposits: {deposits}')
        print(f"\n Total withdraws: {withdraws}")



def menu():
    while True:
        print("-----Welcome to PYVault----")
        print("-----PYVault Menu----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. View Transaction History")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter your deposit amount: "))
            deposit(amount)
        elif choice == "2":
            amount = float(input("Enter your withdraw amount:"))
            withdraw(amount)
        elif choice == "3":
            checkbalance()
        elif choice == "4":
            tranactionhistory()
        elif choice == "5":
            print("Thank you for choosing PYVault and visit again")
            break
        else:
            print("Invalid Choice")

menu()

