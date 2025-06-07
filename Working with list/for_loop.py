games=['volleyball', 'cricket', 'football', 'donkey', 'hockey']
for game in games:
    print(f"{game.upper().strip()}, is a great game to play")
    print(f"I can't wait to play {game.title().strip()} with my friends.\n")
print("I love playing games with my friends, don't you?")
# The for loop iterates over each element in the list 'games'
# and prints a message for each game. The 'upper' method is used to convert
# the game name to uppercase, and the 'title' method is used to capitalize
# the first letter of each word in the game name.
