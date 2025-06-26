file_path = 'C:/Users/xero__t94rj10/OneDrive/Desktop/learn/python/pyth/files and exception/pi.txt'
with open(file_path) as file_object:
    """To do any work with a file, even just printing its contents, you first need to open the file to access it. The open() function needs 
       one argument: the name of the file you want to open."""
    content = file_object.read() # read function read the content from the pi.txt file
print(content.lstrip())

# reading line by line 
file_path = 'pi.txt'
with open(file_path) as file_object:
    for line in file_object: # read function read the content from the pi.txt file
        print(line.strip())

# making list of line from file
file_path = 'C:/Users/xero__t94rj10/OneDrive/Desktop/learn/python/pyth/files and exception/pi.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip())


# working with file content
file_path = 'C:/Users/xero__t94rj10/OneDrive/Desktop/learn/python/pyth/files and exception/pi.txt'
with open(file_path) as file_object:
    lines = file_object.readlines()

pi = ''
for line in lines:
    pi += line.rstrip()

print(pi)
print(len(pi))

# reading larger file 
filename = 'C:/Users/xero__t94rj10/OneDrive/Desktop/learn/python/pyth/files and exception/pi.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
print( f"{pi_string[:40]}....")
print(len(pi_string))
