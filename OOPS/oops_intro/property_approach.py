"""
2. PROPERTY  (python way of doing this)


"""

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
    
    # getter
    # @property
    # def email(self):
    #     print("Email accessed")
    #     return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email

user1 = User("Superman", "superman@gmail.com", "123")
print(user1.email)
