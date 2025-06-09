def describe_type(animal_type, pet_name):
    """ displaying a pet type"""
    print(f"\nI have a reptile {animal_type.title()}")    
    print(f"My {animal_type} name is {pet_name.title()}")  
describe_type(animal_type='snake', pet_name='hola')
describe_type(pet_name='hola', animal_type='snake')  # same result The order of keyword arguments doesn’t matter because Python knows where each value should go.

# Default value 
def describe_pet(pet_name, animal_type = 'cat'):
    print(f"\nI have a pet {animal_type.title()}")    
    print(f"My {animal_type} name is {pet_name.title()}")  
describe_pet(pet_name='harrry')
describe_pet(pet_name='solo',animal_type='dog')
# When you use default values, any parameter with a default value needs to be listed 
# after all the parameters that don’t have default values. This allows Python to con
# tinue interpreting positional arguments correctly


# Avoiding argument error
def describe_pet(pet_name, animal_type = 'cat'):
    print(f"\nI have a pet {animal_type.title()}")    
    print(f"My {animal_type} name is {pet_name.title()}")  
describe_pet()