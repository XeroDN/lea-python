My_favourite_games = ['football', 'cricket', 'tennis', 'badminton']
friends_favourite_games = My_favourite_games
# friends_favourite_games = My_favourite_games[:]
My_favourite_games.append('chess')
friends_favourite_games.append('hockey')

print(" My favourite games are:")
print(My_favourite_games)

print("\nMy friend's favourite games are:")
print(friends_favourite_games)


# without slicing
# This will create a reference to the same list object
# This will create a copy of the list object
friends_favourite_games = My_favourite_games[:]# Now, modifying one list will not affect the other

