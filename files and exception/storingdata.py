# using json.dumps()
import json
numbers = [1, 2, 3, 4, 5]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)  # The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data.

# using json.load()
filename = 'numbers.json'
with open(filename) as h:
    numbers = json.load(h)
print(numbers)

# saving and reading usergenerated input data
username = input('what is your name?')
filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
print(f'we will remember you when you come back, {username.title()}!')
 
# name is already stored
filename = 'username.json'
with open(filename) as h:
    username = json.load(h)
    print(f'Welcome back, {username.title()}!')

# load the username with exception handling
filename = 'username.json'
try:
    with open(filename) as h:
        username = json.load(h)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f'We will remember you when you come back, {username.title()}!')
else:
    print(f'Welcome back, {username.title()}!')


# refactoring the code
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as h:
            return json.load(h)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print(f'Welcome back, {username.title()}!')
    else:
        username = get_new_username()
        print(f'We will remember you when you come back, {username.title()}!')
greet_user()