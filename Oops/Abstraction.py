from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, name):
        self.name = name
    
    #abstractmethod
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(step):
        pass

    #concrete method (optional)
    def show_name(self):
        print(f"Vehicle name: {self.name}")
    
class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")
    
    def stop(self):
        print("Car stops with brakes.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with kick.")
    
    def stop(self):
        print("Bike stops with hand-brake")

# --------------using classes----------------

car = Car("BMW")
bike = Bike("Royal Enfield")

car.show_name()
car.start()
car.stop()

print()

bike.show_name()
bike.start()
bike.stop()