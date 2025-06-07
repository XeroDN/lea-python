website_user = {
    'username': "XeroDN",
    "first_name": 'niroj',
    'last_name': 'rana',
    'age': 21,
    'city': 'kathmandu',
    "is_admin": True,

}
for key, value in website_user.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")

for attribute, value in website_user.items():
    print(f"{attribute} = {value}")

for attribute in website_user.keys():
    print(f"{attribute}")


games = {
    'niroj': 'counter strike',
    'sanjay': 'pubg',
    'sanjeev': 'dota',
    'raju' : 'fifa',
    'sagar': 'call of duty',
    'sujan': 'fortnite',
    'suman': 'valorant',
}
friends = ['niroj', 'raju', 'hari']
for name in games:
    print(f"{name.title()}")
    if name in friends:
        game = games[name].title()
        print(f"{name.title()} favourite game is {game}")


if 'manoj' not in games.keys():
    print("\n  tell me manoj what is your favourite game? ".title().strip())
else:
    print(f"manoj's favourite game is {games['manoj']}")


for name in sorted(games.keys()):
    print(f"{name.title()} plays a  {games[name].title()}")

#  to acess the value of a key
# value() meethod
for game in sorted(games.values()):
    print(f"\n{game.capitalize().lstrip()}")

#  set()
unique_games = set(games.values())
print("\nUnique games played by friends:")
for game in unique_games:
    print(game.title())


sets= {'niroj', 'sanjay', 'sanjeev', 'raju', 'sagar', 'sujan', 'suman'}
# this is set
for name in sets:
    print(f"{name.title()} is a good friend of mine")