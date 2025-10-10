class Car:
    def __init__(self,brand,engine_power):
        self.brand = brand
        self.engine = self.Engine(engine_power)
    
    def show_info(self):
        print(f"car brand: {self.brand}")
        print(f"Engine power: {self.engine.power} HP")
    
    class Engine:
        def __init__(self,power):
            self.power = power 

my_car = Car("Toyota",150)
my_car.show_info()
