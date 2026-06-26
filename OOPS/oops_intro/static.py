"""
#static attribute

# Instance attribute
""" 

# class User:
#     user_count = 0

#     def __init__(self, username, email):
#         # instance attrbute
#         self.username = username
#         self.email = email
#         User.user_count += 1
    
#     def display_user(self):
#         print(f"Username: {self.username}, Email: {self.email}")

# user1 = User("Nani", "nani@gmail.com")
# user2 = User("Mahesh", "maheshbabu@gmail.com")
 
# print(User.user_count)


# ---------Static vs Instance Method Example -----------

class BankAccount:
    MIN_BALANCE = 100

    def __init__(self, owner, balance = 0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if self._is_valid_amount(amount):
            self._balance += amount
            # print(f"{self.owner}'s new balance: ${self._balance}")
            self.__log_transaction("deposit", amount)
        else:
            print("Deposit amount must be positive.")
            
    # protective method
    def _is_valid_amount(self, amount):
        return amount > 0
    
    # private methos - accessible with in internal class, cannot be overwritten 
    def __log_transaction(self, transactionType, amount):
        print(f"Logging {transactionType} of ${amount}. New balance: ${self._balance}")

    @staticmethod
    def is_valid_interest_rate(rate):
        return 0 <= rate <= 5
    

account = BankAccount("John", 500)
account.deposit(200)

print(BankAccount.is_valid_interest_rate(3))