# using json.dumps()
import json
numbers = [1, 2, 3, 4, 5]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)    # The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data.