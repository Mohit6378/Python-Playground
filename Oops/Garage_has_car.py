class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def display_car_info(self):
        return f"Brand: {self.brand} and Model: {self.model}"

class Garage:
    def __init__(self):
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
        print(f"New car bought: {car.display_car_info()}")
    
    def show_my_garage(self):
        print("You have these cars in your garage.")
        for car in self.cars:
            print(car.display_car_info())

car1 = Car("Lamborghini", "Gallardo")
car2 = Car("BMW", "M3GT")

my_garage = Garage()
my_garage.add_car(car1)
my_garage.add_car(car2)
my_garage.show_my_garage()