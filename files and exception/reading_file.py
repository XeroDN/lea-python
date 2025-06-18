file_path = 'C:/Users/xero__t94rj10/OneDrive/Desktop/learn/python/pyth/files and exception/pi.txt'
with open(file_path) as file_object:
    """To do any work with a file, even just printing its contents, you first need to open the file to access it. The open() function needs 
       one argument: the name of the file you want to open."""
    content = file_object.read() # read function read the content from the pi.txt file
print(content.lstrip())