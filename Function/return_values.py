def get_formatted_name(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    return full_name.title()
physicts = get_formatted_name('niroj','rana')
print(physicts)


# making an argument optional
def get_formatted_name(first_name, middle_name, last_name): # But middle names aren’t always needed, and this function as written would not work if you tried to call it with only a first name and a last name. 
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
physicts = get_formatted_name('niroj','shamser','rana')
print(physicts)


def get_formatted_name(first_name, last_name, middle_name=(),): 
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
physicts = get_formatted_name('niroj','shamser','rana')
print(physicts)
