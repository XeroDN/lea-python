class Car:
    """A simple representation of car """
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

    def fill_gas_tank(self):
        """ electric car doesn't have any gas tank """
        print("This car does not need any gas")  # Overriding Methods from the Parent Class

class ElectricCar(Car):
    """ Representation aspect of car, specific of electric car"""
    def __init__(self, make, model, year):
        """Initilalize a attribute of parent class"""
        super().__init__(make, model, year) 
        """The super() function is a special function that allows you to call 
           a method from the parent class. This line tells Python to call the __init__() 
           method from Car, which gives an ElectricCar instance all the attributes 
           defined in that method"""
        self.battery_size = 100

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kwh of battery.")

my_byd = ElectricCar('byd', 'model', 2024)
print(my_byd.get_descriptive_name())
my_byd.describe_battery()



# Instances as attribute 
""" When modeling something from the real world in code, you may find that 
you’re adding more and more detail to a class. You’ll find that you have a 
growing list of attributes and methods and that your files are becoming 
lengthy. In these situations, you might recognize that part of one class can 
be written as a separate class. You can break your large class into smaller 
classes that work together."""

class Car:
    """A simple representation of car """
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

    def fill_gas_tank(self):
        """ electric car doesn't have any gas tank """
        print("This car does not need any gas")  # Overriding Methods from the Parent Class


class Battery():
    """A simple attempt to model for the class electric car"""
    def __init__(self, battery_size= 75):
        """ Initialize the battery size """
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has {self.battery_size}-kwh of battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

        
class ElectricCar(Car):
    """ Representation aspect of car, specific of electric car"""
    def __init__(self, make, model, year):
        """Initilalize a attribute of parent class"""
        super().__init__(make, model, year) 
        """The super() function is a special function that allows you to call 
           a method from the parent class. This line tells Python to call the __init__() 
           method from Car, which gives an ElectricCar instance all the attributes 
           defined in that method"""
        self.battery = Battery()

my_byd = ElectricCar('byd', 'model', 2024)
print(my_byd.get_descriptive_name())
my_byd.battery.describe_battery() 
my_byd.battery.get_range()
