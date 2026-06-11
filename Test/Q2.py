# Create Abstract class Vehicle with: (4 Marks)
# • Abstract methods: start(), stop(), fuel_type()
# Create 3 child classes:
# • Car fi 'Car started' / 'Petrol'
# • Bike fi 'Bike started' / 'Petrol'
# • Tesla fi 'Tesla started' / 'Electric'
# Create objects and call all methods


from abc import ABC,abstractmethod

class Vehicle(ABC):
    def start(self):
        pass

    def stop(self):
        pass

    def fuel_type(self):
        pass

class Car(Vehicle):
    def start(self):
        print("car Start")

    def stop(self):
        print("car stop")

    def fuel_type(self):
        
        print("petrol ")

class  Bike(Vehicle):
    def start(self):
        print("Vehicle Start")

    def stop(self):
        print("Vehicle stop")

    def fuel_type(self):
        
        print("petrol")
class  Tesla(Vehicle):
    def start(self):
        print("Vehicle Start")

    def stop(self):
        print("Vehicle stop")

    def fuel_type(self):
        
        print("Electric")

car = Car()
car.start() 
car.stop()
car.fuel_type()

bike = Bike()
bike.start() 
bike.stop()
bike.fuel_type()

tesla = Tesla()
tesla.start() 
tesla.stop()
tesla.fuel_type()
