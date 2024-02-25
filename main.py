bikes = ['Honda', 'Harley', 'Ducati']
trucks = ['Ford', 'Hyundai', 'Chevy']


class Vehicle:
    vehicles_to_compare = []
    def __init__(self, make, miles, price, engine_on=False):
        self.make = make
        self.miles = miles
        self.price = price
        self.engine_on = False
        pass
    def start_engine(self):
        print("Starting engine...")
        #  Sets engine_on to True
        pass
    def make_noise(self):
        print("Beep beep!")
        pass

class Truck(Vehicle):
    def __init__(self, make, miles, price, cargo=False):
        super().__init__(make, miles, price)
        self.cargo = False
        pass
    def load_cargo(self):
        print("Loading the truck bed...")
        #  Sets cargo to True
class Motorcycle(Vehicle):
    def __init__(self, make, miles, price, top_speed):
        super().__init__(make, miles, price)
        self.top_speed = top_speed
    def make_noise(self):
        print("Vroom vroom!")
        pass


# motor = Motorcycle()
# motor.make_noise()


while True:
    pass
