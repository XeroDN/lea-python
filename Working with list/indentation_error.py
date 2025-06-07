games=['volleyball', 'cricket', 'football', 'donkey', 'hockey']
for game in games:
# print(f"{game.upper().strip()}, is a great game to play")   # IndentationError: expected an indented block  

# The above code will raise an IndentationError because the print statement is not indented properly.
# To fix the error, we need to indent the print statement properly.
    print(f"I can't wait to play {game.title().strip()} with my friends.\n")

# forgetting to indent the print statement
print(f"{game.title().strip()} is a fun game to play.")
# Theabove code will not raise an IndentationError because the print statement is not inside the for loop.
# The print statement is outside the for loop, so it will not be executed for each game in the list.
# To fix the error, we need to indent the print statement properly.

#  LOGICAL ERROR EROOOOOOOOOOOOOOOOOOR NOT SYNTAX ERROR

# IdentationError: expected an indented block
cars = ['audi', 'bmw', 'toyota', 'honda']
#    print("Cars I like:")

