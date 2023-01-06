# Count String

def count(string: str) -> dict:
    """Returns a dictionary of how many times each element appears in the string."""

    result = {}

    for char in string:
        if char not in result:
            result[char] = 1
        else:
            result[char] += 1

    return result

print(count("hello"))
