# text ="hello my name is niroj rana"
# text.split()
filename = 'C:/Users/xero__t94rj10/OneDrive/Desktop/learn/python/pyth/files and exception/pi.txt'
try:
    with open(filename, encoding = 'utf-8') as f:
      contents = f.read()
except FileNotFoundError:
    print(f"the file {filename} doesn't exist!")
else:
   # count the number of words in the file
   words = contents.split()
   num_words = len(words)
   print(f"the file {filename} has about {num_words} words.")
   

# working with multiple file
def count_words(filename):
    try:
        with open(filename, encoding = 'utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"the file {filename} doesn't exist!")
    else:
   # count the number of words in the file
       words = contents.split()
       num_words = len(words)
       print(f"the file {filename} has about {num_words} words.")
filenames = ['C:/Users/xero__t94rj10/OneDrive/Desktop/learn/python/pyth/files and exception/pi.txt', 'programming.txt', 'hrllo']
for filename in filenames:
    count_words(filename)