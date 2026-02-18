class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def drive(self):
        print(f"{self.brand} {self.model} is driving.")
    def stop(self):
        print(f"{self.brand} {self.model} has stopped.")
my_car=Car("Honda","Civic")
my_car1=Car("BMW","X5")
my_car.drive()
my_car.stop()
my_car1.drive()
my_car1.stop()
