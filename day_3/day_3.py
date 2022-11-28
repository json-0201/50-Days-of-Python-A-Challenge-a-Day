# Register Check

def register_check(d: dict):
    """return the number of students in school"""
    
    count = 0
    for val in d.values():
        if val == "yes":
            count += 1

    return count

register = {'Michael':'yes','John': 'no',  
            'Peter':'yes', 'Mary': 'yes'}
print(register_check(register))


# Extra Challenge: Lowercase Names
names = ["kerry", "dickson", "John", "Mary",  
         "carol", "Rose", "adam"]

lc_names = tuple([name \
    for name in names if name.islower()])
print(lc_names)
