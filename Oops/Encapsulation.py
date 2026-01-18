class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.__pin = 1234
    
    def owner_name(self):
        print("Account holder: ",self.owner)
    
    #getter
    @property
    def balance(self):
        return self._balance
    
    #setter
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            print("Invalid amount.")
        else:
            self._balance = amount
    
    #private method
    def __verify_pin(self, pin):
        return self.__pin == pin
    
    #public method to use private method
    def withdrawal(self, amount, pin):
        if not self.__verify_pin(pin):
            print("Incorrect pin.")
            return
        
        if amount > self._balance:
            print("Insufficient balance.")
        else:
            self._balance -= amount
            print("Remaing balance: ", self._balance)

# ----------- USING THE CLASS -------------

b1 = BankAccount("Mohit", 50000)
b1.owner_name()
#getting balance
print("Account balance: ", b1.balance)
#setting balance
b1.balance = -200
b1.balance = 60000
print("Updated balance", b1.balance)
#withdrawing
b1.withdrawal(2000, 2222)
b1.withdrawal(1000000, 1234)
b1.withdrawal(5000, 1234)

# Name mangling access (NOT recommended)
print("Accessing private via mangling:", b1._BankAccount__pin)