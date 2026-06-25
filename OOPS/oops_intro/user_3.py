"""Modift or assign the data
1. Traditional approach - make the data attribute private and use getter & setters 
    _email  // protected by prefixing underscore. It means it cannot be used outside the class
    - Potected
# The Conseding Adults Phillosophy
The developer responsiblity for not accessing the underscored items

* user double undercore to protect the attrbite. you can in the below tested. 
    = private
    It throws an error: 
            AttributeError: 'User' object has no attribute '__email'

    # Name Manled - private variable      
# GETTER AND SETTER METHOD 

2. REcommended Approach using Properties

"""


from datetime import datetime

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.__email = email
        self.password = password

    # def say_hi_to_user(self, user):
    #     print(f"Hi {user.username}, its {self.username} here")

    # def clean_email(self):
    #     return self.__email.lower().strip()

    # Getter
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return  self.__email

    # setter
    def set_email(self, new_email):
        if "@" in new_email:
            self.__email = new_email

user1 = User("Superman", "superman@gmail.com", "123")
# user2 = User("Batman", "batman@gmail.com", "abc")
# print(user1.__email)
# print(user1.clean_email())

user1.set_email("superman@outlook.com")
print(user1.get_email())

# user1.say_hi_to_user(user2)