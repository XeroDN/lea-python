car=["toyota", "honda", "ford", "chevrolet"]
print(car)
# Modifying elements in a list
car[0]="nissan"
print(car)
# Modifying elements in a list is easy, just assign a new value to the index of the element you want to change


# Adding elements to a list
car.append("kawasaki")
print(car)
# The append() method adds a new element to the end of the list
# You can also add elements to a specific position in the list using the insert() method
# Adding elements to a specific position in the list
car.insert(2, "bmw")
print(car)
# The insert() method takes two arguments: the index where you want to insert the new element and the element itself
car.insert(4,"mercedes benz")
print(car)
# You can also add multiple elements to a list using the extend() method
# The extend() method takes an iterable (like a list or a tuple) and adds its elements to the end of the list
# Adding multiple elements to a list
car.extend(['suzuki', 'hyundai'])
print(car)
# The extend() method is useful when you want to add multiple elements to a list at once