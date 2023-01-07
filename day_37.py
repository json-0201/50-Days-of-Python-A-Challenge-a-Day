# Count the Vowels

def count_the_vowels(string: str) -> int:
    """Returns the number of unique vowels in the string."""

    vowels = [char for char in string if char.lower() in ["a","e","i","o","u"]]
    counts = len(set(vowels))

    return counts

print(count_the_vowels("hello"))
print(count_the_vowels("saas"))
