""" Importing a module into module """

from Importing_class import Car
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
        self.battery = Battery()