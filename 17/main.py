# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         """here you can seee the followers is not passed as a parameter, 
#         this means for all the users the followers count will be initialised as 0"""

# user_1 = User("001", "Nihal")

# ##### attribute

# user_1.id = "001"
# user_1.username = "Naufal"

# print(user_1.id)

# Constructor or initialise
# class Car:
#     def __init__(self):
        # initialise the atribute

# # Setting attribute 
# """ seats = 5"""
# class Car:
#     def __init__(self, seats):
#         self.seats = self.seats

  
"""Adding Methods to a Class"""
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001", "naufal")
user_2 = User("002", "Nihal")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)