"""Modift or assign the data
1. Traditional approach - make the data attribute private and use getter & setters 
    _email  // protected by prefixing underscore. It means it cannot be used outside the class

"""



class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    # def say_hi_to_user(self, user):
    #     print(f"Hi {user.username}, its {self.username} here")

    def clean_email(self):
        return self._email.lower().strip()

user1 = User("Superman", "superman@gmail.com", "123")
# user2 = User("Batman", "batman@gmail.com", "abc")

# user1.say_hi_to_user(user2)