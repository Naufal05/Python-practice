# Encapculation



# bad example
# class BadBankAcccount:
#     def __init__(self, balance):
#         self.balance = balance


# account = BadBankAcccount(0.0)
# account.balance = -1
# print(account.balance)

# Good example

class BankAccount:
    def __init__(self):
        self._balance = 0.0
    
    # getter property mthod called balance
    @property
    def balance(self):
        return self._balance
    
    def  deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount be positive")
        self._balance += amount
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount be positive")
        if amount >= self._balance:
            raise ValueError("Insufficient Funds")

        self._balance -= amount


account = BankAccount()
# initial balance
print(account.balance)
# deposit method
account.deposit(199)
print(account.balance)
# Withdraw methof
account.withdraw(5)
print(account.balance)
