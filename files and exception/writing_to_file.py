""" wirting to empty file """
filename = 'programming.txt' #  The open() function automatically creates the file you’re writing to if it doesn’t already exist.
with open(filename, 'w') as file_object:  # 'w' for write and 'r ' for read and 'a' for append mode
    file_object.write("I love programming:\n ")
    file_object.write(' i love python programming as well as playing with python.\n')
    file_object.write(' i love creating a new game\n')

# appending  to a file 
filename = 'programming.txt' #  The open() function automatically creates the file you’re writing to if it doesn’t already exist.
with open(filename, 'a') as file_object:  # 'w' for write and 'r ' for read and 'a' for append mode
    file_object.write("I love doing new thing :\n ")
    file_object.write(' i love  to create a game to satisfy my personal believe.\n')  # append does not overwrite the file, it just adds to the end of the file