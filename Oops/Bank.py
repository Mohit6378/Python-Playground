class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Your balance after deposit: {self.balance}")
    
    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            print(f"Your amount after withdrawal: {self.balance}")
        else:
            print("Insufficient balance.")
    
    def display(self):
        print(f"Account holder name: {self.account_holder} with Bank balance: {self.balance}")

b1 = BankAccount("Mohit", 50000)
b2 = BankAccount("Rohit", 100000)

b2.withdraw(20000)
b1.deposit(20000)

b1.display()
b2.display()