# car=['toyota', 'honda', 'ford', 'chevrolet']
# car.sort()  # sorts the list in ascending order
# print(car)  # Output: ['chevrolet', 'ford', 'honda', 'toyota']
# car.sort(reverse=True)  # sorts the list in descending order
# print(car)  # Output: ['toyota', 'honda', 'ford', 'chevrolet']
# # sorting a list temporarily using the sorted() function
car=['toyota', 'honda', 'ford', 'chevrolet']
sorted_car = sorted(car)  # returns a new sorted list
print(sorted_car)  # Output: ['chevrolet', 'ford', 'honda', 'toyota']
# sorting a list temporarily in descending order
sorted_car_desc = sorted(car, reverse=True)  # returns a new sorted list in descending order
print(sorted_car_desc)  # Output: ['toyota', 'honda', 'ford', 'chevrolet']
# sorting a list of numbers
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort()  # sorts the list in ascending order
print(numbers)  # Output: [1, 2, 5, 5, 6, 9]
# sorting a list of numbers in descending order
numbers.sort(reverse=True)  # sorts the list in descending order
print(numbers)  # Output: [9, 6, 5, 5, 2, 1]
cars = ['toyota', 'honda', 'ford', 'chevrolet']
cars.reverse()  # reverses the order of the list
print(cars)  # Output: ['chevrolet', 'ford', 'honda', 'toyota']
# it does not reverse the order of the list, it just returns a new reversed list
reversed_cars = list(reversed(cars))  # returns a new reversed list
print(reversed_cars)  # Output: ['toyota', 'honda', 'ford', 'chevrolet']    
cars = ['toyota', 'honda', 'ford', 'chevrolet']
len(cars)  # returns the number of items in the list
print(len(cars))  # Output: 4   
# checking if an item is in the list
# if 'toyota' in cars:
#     print('Toyota is in the list')  # Output: Toyota is in the list
# # checking if an item is not in the list
# if 'bmw' not in cars:
#     # print('BMW is not in the list')  # Output: BMW is not in the list
bikes= ['harley', 'ducati', 'yamaha', 'honda']
bikes.extend(['husqvarna', 'lamborghini'])
print(bikes)  # Output: ['harley', 'ducati', 'yamaha', 'honda', 'husqvarna', 'lamborghini']
# index error occurs when you try to access an index that is out of range
# for example, if you try to access the 5th index of a list that has only 4 items
# bikes = ['harley', 'ducati', 'yamaha', 'honda']
# print(bikes[5])  # IndexError: list index out of range