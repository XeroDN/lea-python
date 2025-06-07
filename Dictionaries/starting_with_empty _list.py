alien_0 = {}
alien_0['color'] = 'white'
alien_0['points'] = '25' 

print(alien_0)

# Modifying the value of a key in dictonaries
alien_0['color'] = 'pink'
print(f"The color of alien is {alien_0['color']}")
# Adding a new key-value pair to the dictionary
alien_0['color'] = 'black'
print(f"\nThe color of alien now is {alien_0['color']}")


alien_0 = {}
alien_0['x_position'] = 3
alien_0['y_position'] = 25
alien_0['speed'] = 'medium'
print(f"\nOriginal x-position: {alien_0['x_position']}")
if alien_0['speed'] == 'slow':
    x_increment = 4
elif alien_0['speed'] == 'medium':
    x_increment  = 10
else:
    x_increment = 15
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New x_position: {alien_0['x_position']}")



# removing  a key value jpair from a dictionary
alien_1 = {'color': 'green', 'points': 5}
print("\n", alien_1)
del alien_1['color']
print(alien_1)