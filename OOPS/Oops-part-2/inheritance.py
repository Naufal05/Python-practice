# Inheritance

# A car is a vehicle
# A BIKE IS A VEHICLE


class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehcile is starting")

    def stop(self):
        print("Vehicle is stoping")
    

class Car(Vehicle):
    def __init__(self, brand, model, year, number_of_doors, numwe_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_doors = number_of_doors
        self.numwe_of_wheels = numwe_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, number_of_wheels):
        super().__init__(brand, model, year)
        self.number_of_wheels = number_of_wheels

car = Car("Benz", "G-Wagon", 2020, 5, 4 )
bike = Bike("TVS", "Activa", 2018, 2)

print(car.__dict__)
print(bike.__dict__)