ages = [2,3,4,5,14,15,18,1,21,26,46,78,96,54,47,33]
ages.sort()
for age in ages:
    if age <= 4 or age >= 60:
        price = "free"
    elif age <= 16:
        price = "half"
    elif age < 25:              # multiple elif statements
        price = "25% off"
    else:
        price = "full"
    print(f"\nyour ticket is {price} price")




allien_color = ["green","yellow","red"]
for color in allien_color:
    if color == "green":
        point=5
    elif color == "yellow":
        point = 10
    elif color == "red":
        point = 15
    print(f"\n you have earned {point} points:")



requested_toppings = []
if requested_toppings:
 for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print("\nFinished making your pizza!")
else:
    print("\nAre you sure you want a plain pizza?")


#  workng with mltiple lists
available_toppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"\nAdding {requested_topping}.")
    else:
        print(f"\nSorry, we don't have {requested_topping}.")