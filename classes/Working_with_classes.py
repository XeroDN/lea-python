class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}."
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} mileage.")

my_new_car = Car('toyota','jagur', 2025)
print(f"my new car is {my_new_car.model} and manufactured by {my_new_car.make} in {my_new_car.year}.".capitalize())
my_new_car.read_odometer()


# Modifying attributes values
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}."
        return long_name.title()
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} mileage.")

my_new_car = Car('toyota','jagur', 2025)
print(f"my new car is {my_new_car.model} and manufactured by {my_new_car.make} in {my_new_car.year}.".capitalize())
my_new_car.odometer_reading =  30  # Modifying an Attribute’s Value Directly
my_new_car.read_odometer()


# Modifying an Attribute’s Value Through a Method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}."
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} mileage.")

    def update_odometer(self, mileage):   #Modifying an Attribute’s Value Through a Method
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back odo meter")
        

my_new_car = Car('toyota','jagur', 2025)
print(f"\nmy new car is {my_new_car.model} and manufactured by {my_new_car.make} in {my_new_car.year}.".capitalize())
my_new_car.update_odometer(50)
my_new_car.read_odometer()


# Incrementing an Attribute’s Value Through a Method
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}."
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} mileage.")

    def update_odometer(self, mileage):   #Modifying an Attribute’s Value Through a Method
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print(f"You can't roll back odo meter")
        
    def increment_odometer(self, miles):
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()