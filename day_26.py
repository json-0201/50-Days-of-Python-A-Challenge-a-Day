# Sort Words

def sort_words(s: str) -> list:
    """Returns a list of letters sorted in alphabetical order, separated by commas."""

    res = list(set([char for char in s if char.isalpha()]))
    res.sort()
    res = ",".join(res)

    return [res]

print(sort_words("love life"))


# Extra Challenge: Length of Words
s = 'Hi my name is Richard'

def string_length(s: str) -> dict:
    """Returns the length of all the words in a form of a dictionary."""

    res = {}
    words = s.split()
    for word in words:
        res[word] = len(word)
    
    return res

print(string_length(s))
