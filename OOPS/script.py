# name = "danny"
# age = 29

# print(type(name.capitalize))
# print(type(age))


class Dog:
    # init is created once only
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    # function
    def bark(self):
        print("whof whof")


class Owner:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone

#object
owner1 = Owner("Raju","Palakkad", "01233456")
dog1 = Dog("branc", "Chokli", owner1)
# dog1.bark()
print(dog1.owner.name)

owner2 = Owner("Damu","Kozhukode", "98756445")
dog2 = Dog("Jenny", "Rajapalayam", owner2)
# dog2.bark()
print(dog2.owner.name)


"""
#### SUMMARY

Class - blueprint for creating object
Object - instance of a class
Attrbitues - stores info about an object
Methods: actions or functions that can perform
self - referes to the specfiic object of the class

"""