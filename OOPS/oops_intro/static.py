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