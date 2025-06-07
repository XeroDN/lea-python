cars=['Ford', 'Chevrolet', 'Toyota', 'Honda','bmw', 'Mercedes', 'Hyundai', 'Kia']
print(cars[0:5])
print(cars[6:3:-1])
print(cars[:6][::-1])  # This will reverse the list
print(cars[3:])
print(cars[-4:])

for car in cars[:5]:  # slicing in loop
    print(car.title())


