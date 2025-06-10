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
physicts = build_person('Niroj','Rana',)
print(physicts)