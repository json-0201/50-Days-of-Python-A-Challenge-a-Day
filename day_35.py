# Pangram

def check_pangram(string: str) -> bool:
    """Takes a string and checks if it is a pangram."""

    chars = []

    for char in string:
        if char.isalpha() and char.lower() not in chars:
            chars.append(char)
    
    return True if len(chars)==26 else False

s = "the quick brown fox jumps over a lazy dog"
print(check_pangram(s))


# Extra Challenge: Find my Position

def find_index(l: list, i: int) -> list:
    """Returns the indexes of the integer,
    if does not exist, return a equal size list full of the integer."""

    indexes = []

    for ind, num in enumerate(l):
        if num == i:
            indexes.append(ind)

    if indexes:
        return indexes
    else:
        return list(map(lambda x: i, l))

print(find_index([1,2,4,6,7,7], 7))
print(find_index([1,2,4,6,7,7], 8))
