game_1 = {'size':5, 'player': 11, 'post_size': '9 feet'}
game_2 = {'size': 2, 'player': 11, 'field_size': '100 sq feet'}
game_3 = {'size': 4, 'player': 5, 'field_size': '40 sq feet'}
games = [game_1, game_2, game_3]
for game in games:
    print(game)

games = []
for game_number in range(10):
    game_number = {'football_size': 5, 'field_size' : '60 sq feet', 'player_size' : 22 }
    games.append(game_number)

for game_number in games[:3]:
    if game_number['football_size'] == 5:
        game_number['football_size'] = 6
        game_number['field_size'] = '120 sq feet'
        game_number['player_size'] = 24

for game in games[:6]:
    print(game)
print(".....")

print(f"\nTotal numbe of games is {len(games)}")