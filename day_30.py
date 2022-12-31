# Most Repeated Name

def repeated_name(l: list) -> str:
    """Finds the most repeated name in the list."""

    counts = [l.count(name) for name in l]
    result = counts.index((max(counts)))
    
    return l[result]

names_1 = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
    
print(repeated_name(names_1))


# Extra Challenge: Sort by Last Name

names_2 = ["Beyonce Knowles", "Alicia Keys", "Katie Perry", "Chris Brown", "Tom Cruise"]

def sorted_name(l: list) -> list:
    """Sorts the names by last name and switches the format."""

    switched = []
    for name in l:
        fn = name.split()[0]
        ln = name.split()[1]
        switched.append(ln+" "+fn)
    switched.sort()

    return switched

print(sorted_name(names_2))
