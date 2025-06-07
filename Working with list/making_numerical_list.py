for value in range(0,15):
    print(value,)
#   In this example, range() prints only the numbers 0 through 14. This is 
# another result of the off-by-one behavior you’ll see often in programming 
# languages. The range() function causes Python to start counting at the first 
# value you give it, and it stops when it reaches the second value you provide. 
# Because it stops at that second value, the output never contains the end 
# value, which would have been 15 in this case.

# pass range() a single argument to start at 0 and end at the value you provide:
for value in range(5):
    print(value)

#  Mkaing a list of numbers
# You can use the range() function to create a list of numbers.
numbers = list(range(4,15))
print(numbers)

#  Skipping values in a list
num = list(range(1,20,4))
print(num)


cubes = []
for value in range(1,15):
    # cube = value**3
    cubes.append(value**3)
print(cubes)