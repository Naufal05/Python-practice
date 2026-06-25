class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 20)
person1.greet()
person2 = Person("BOB", 20)
person2.greet()