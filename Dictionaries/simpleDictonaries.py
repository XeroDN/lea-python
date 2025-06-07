alien_0 = {'color': 'blue', 'points': 20 }
alien_1 = {'color': 'red', 'points': 10}
print(alien_0['color'])
print(alien_0['points'])
print("\n")
print(alien_1['color'])
print(alien_1['points'])

new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")

alien_0['x_position'] = 0
alien_0['y_position'] = 30
print(alien_0)