def build_person(first_name,last_name):
    person = {'first':first_name,'last':last_name}
    return person
physicts = build_person('Niroj','Rana')
print(physicts)


def build_person(first_name,last_name, age=()):
    if age:
        person = {'first':first_name,'last':last_name,'aage':age}
    else:
        person = {'first':first_name, 'last':last_name}
    return person
physicts = build_person('Niroj','Rana',45)
print(physicts)

def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person
physicts = build_person('Niroj','Rana',34)
print(physicts)


def get_formatted(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print(f"\nPlease tell me your name")
    print("enter 'q' to quit")
    f_name = input("Firstname: ")
    if f_name == 'q':
        break
    L_name = input("last name: ")
    if L_name == 'q':
        break
    formatted_name = get_formatted(f_name,L_name)
    print(f"Hello {formatted_name}! ")