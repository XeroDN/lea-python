# zero division error 
# print(2/0)  # exception 

# using try-except blocks
try:
    print(3/0)
except ZeroDivisionError:
    print("You can't divide the number")

# using exception to prevent crashes
print("Enter the number for division:")
print("Enter q to exit:")
while True:
    first_number = input("enter the first number:")
    if first_number == "q":
        break
    second_number = input("enter the second number:")
    if second_number == "q":
        break
    # the else block
    try:
        answer = int(first_number)/ int(second_number)
    except:
        print("You can't divide by zero!")
    else:
        print(answer)

# Handling the file not found error
filename = 'progrramming.txt'
try:
    with open(filename, encoding = 'utf-8') as f:
      contents = f.read()
except FileNotFoundError:
    print(f"the file {filename} doesn't exist!")