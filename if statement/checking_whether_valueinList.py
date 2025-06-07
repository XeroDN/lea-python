requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings
print('mushrooms' in requested_toppings)

'pepperoni' in requested_toppings
print('pepperoni' in requested_toppings)


# checking whether  a value is not in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'kapil'
if user not in banned_users:
    print(f"\n {user.title()}, you can post a response if you wish.")
