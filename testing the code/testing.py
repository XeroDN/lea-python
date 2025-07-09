from testing_the_function import get_formatted_name as gfn
print('Enter q at any time to quit.')
while True:
    first = input("\nEnter your first name:")
    if first == 'q':
        break
    last = input("\n Enter your last name:")
    if last == 'q':
        break
    formatted_name = gfn(first, last)
    print(f"\n Neatly formatted name: {formatted_name}")