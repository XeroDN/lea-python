# A tuple looks just like a list except you use parentheses instead of square 
# brackets. Once you define a tuple, you can access individual elements by 
# using each item’s index, just as you would for a list.


cars = ('bmw', 'audi', 'toyota', 'honda', 'ford')
print("original tuple:")
print(cars[0:3])

cars = ('hyundi',)
print("\nmodified tuple:")
# cars[2] = 'mercedes'  # This will raise an error because tuples are immutable

#  Looping through a tuple
for car in cars:
    print(car[:])

# writing over  a tuple 

