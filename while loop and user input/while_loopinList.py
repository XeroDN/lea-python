unused_cars = ['honda','bmw', 'mercedez','suzuki']
used_cars = []
while unused_cars:
    current_cars = unused_cars.pop()
    print(f"veryfing the car: {current_cars.title()}")
    used_cars.append(current_cars)

print("The following car have in used:")
for used_car in used_cars:
    print(used_car.title())


#  removing all instances specific value from list
pets = ['cat', 'dog', 'hen', 'cat', 'dog', 'cat','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)



# Filling a Dictionary with User Input
responses = {}
polling_active = True
while polling_active:
    name = input("what is your name?: ")
    response = input("which movie do you want watch someday? ")

    responses[name] = response # store the information in dictionary
    repeat = input("would you like to respond another person?: (yes/no) ")
    if repeat == 'no':
        polling_active = False
print("\n....polling result......")
for name, response in responses.items():
    print(f"{name.title()} would like to watch {response.title()}")
