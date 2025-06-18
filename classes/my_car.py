from Importing_class import Car # Importing single class from module
from Importing_class import ElectricCar
from Importing_class import Car, ElectricCar, Battery # Importing multiple class from module
import Importing_class  # Importing entire module 
from Importing_class import * # Importing all class from module --- it is also not recommended, it can mislead to error 
from electric_car_module import Battery # this one is example of importing model into module 
import electric_car_module
from Importing_class import ElectricCar as EC # using alias for better understanding
import Importing_class as IC # using alias


my_new_car = Car('BMW', 'Bmw', 2003)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 45
my_new_car.read_odometer()

my_new_car = ElectricCar('tesla', 'telsaX', 2025)
print(my_new_car.get_descriptive_name())
my_new_car.battery.describe_battery()
my_new_car.battery.get_range()

my_new_car = Importing_class.Car('honda','hondax', 2003)  # Importing entire module instances line 4 example 
print(my_new_car.get_descriptive_name())

my_new_car = electric_car_module.ElectricCar('BYD','SUV',2000) # line 7 example 
print(my_new_car.get_descriptive_name())

my_new_car = EC('tessla', 'modelx',2005) # line 8 example 
print(my_new_car.get_descriptive_name())

my_car = IC.Car('jagur','rangerover', 1990) # line 9 example
print(my_car.get_descriptive_name())