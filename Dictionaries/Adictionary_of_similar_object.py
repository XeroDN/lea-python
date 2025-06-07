favourite_games = {
    'john': 'cricket',
    'niroj': 'football',
    'rihan': 'basketball',
    'philip': 'tennis',
}
games = favourite_games['john'].title()
print(f"{'john'.title()} favourite game is {games}.")
print(f"Niroj favourite game is {favourite_games['niroj'].title()}.")

#Using to get() access to the dictionary
# you can use the get() method to set a default value that will be returned if the requested key doesn’t exist.
name= favourite_games.get('nirall', 'Unknown')
print(name)

# get() method
# get()
