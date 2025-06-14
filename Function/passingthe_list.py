# def greet_users(names):
#     for name in names:
#         msg = f"Hello! {name.title()}"
#         print(msg)
# usernames = ['niroj','sushil','narayan']
# greet_users(usernames)

# unrinted_dedign = ['shoes','paint','shocks']
# completed_design = []
# while unrinted_dedign:
#     current_design = unrinted_dedign.pop()
#     print(f'\n{current_design} is printed:')
#     completed_design.append(current_design)
# print("\nthe completed  design are: ")
# for complete_design in completed_design:
#     print(f"{complete_design}")


def print_models(unrinted_dedign,completed_design):
    while unrinted_dedign:
        current_design = unrinted_dedign.pop()
        print(f'\n{current_design} is printed:')
        completed_design.append(current_design)

def completed_designs(completed_design):
    print("\nthe completed  design are: ")
    for complete_design in completed_design:
        print(f"{complete_design}")
 
unrinted_dedign = ['shoes','paint','oddie','shocks']
completed_design = []

print_models(unrinted_dedign,completed_design)
completed_designs(completed_design)


# preventing function from modifying a list
# passing an arbitary argument
def making_pizza(*topping): # *asterics tells in parameter to make an empty tuples
    print(topping)
making_pizza('peporoni')
making_pizza('mushroom','slice tomato','wheat flour')


def making_pizza(*toppings):
    print("\nMaking the pizza with the following ingredients")
    for topping in toppings:
        print(f"- {topping.title()}")
making_pizza('peporani')
making_pizza('tomato', 'mushroom','wheat')
