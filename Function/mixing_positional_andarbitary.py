
def making_pizza(size,*toppings):
    print(f"\nMaking {size} inches pizza with the following ingredients:")
    for topping in toppings:
        print(f"- {topping.title()}")
making_pizza(12,'peporani')
making_pizza(16,'tomato', 'mushroom','wheat')

# keyword argument
def build_profile(first, last, **user_profile):
    user_profile['first'] = first
    user_profile['last'] = last
    return user_profile
user_info = build_profile('niroj','rana',
                           location = 'california',
                           field = 'scientist')
print(user_info)