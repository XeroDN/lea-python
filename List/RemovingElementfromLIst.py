car=["toyota", "honda", "ford", "chevrolet"]
print(car)
# removing elements from a list using the delete statement
# del car[2]
# print(car)
# removing elements from a list using the pop() method
car.pop(2)
print(car)
popped_car = car.pop()  # removes the last element
print(car)
print(popped_car)
motorcycles = ['honda', 'yamaha', 'suzuki'] 
last_owned = motorcycles.pop() 
print(motorcycles)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

# removing elements from a list using the remove() method
car.remove("honda")
print(car)
# removing an element that does not exist will raise a ValueError
# car.remove("tesla")  # Uncommenting this line will raise an error
too_expensive = 'honda'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")
# removing all elements from a list
car.clear()
print(car)  # This will print an empty list
# removing the last element from a list using the clear() method
# car.clear() removes all elements from the list
# but does not return the removed element
# so we cannot capture it in a variable
# if you want to remove the last element and capture it, use pop()
# removing the last element from a list using the pop() method
# car.pop() removes the last element from the list
# and returns it, so we can capture it in a variable