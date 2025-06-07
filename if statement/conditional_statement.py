#  Checking for equality
bike = 'Honda'
bike == "honda"
bike.lower() == 'honda'
print(bike.lower() == 'honda') 

# checking for inequality

requested_food = 'pizza'
if requested_food != 'rice':
    print(f"sorry, we don't have {requested_food}:")

# Numerical comparisons
age = 17
if age != 21:
    print(f"you are not 21, you are {age} years old")

## Using multiple conditions
age = 18
if age >= 18 and age <21:
    print(f"\nyou are {age} years old, you can vote but not drink alcohol")

# age = 20
# age_1 = 23
# age <= 18 or age_1 > 21
# print(f"\n {age}")

age_0 = 22
age_1 = 18
age_0 >= 21 or age_1 >= 21