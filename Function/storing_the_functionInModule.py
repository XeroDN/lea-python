def make_pizza(size , *toppings):
    print(f"Making {size} inches of pizza which have following topping:")
    for topping in toppings:
        print(topping)