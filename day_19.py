# Words and Elements
import re

def count_words(s: str) -> str:
    """counts how many words are in the string."""
    
    words = s.split(" ")
    count = len(words)
    
    return f"{count} words"


def count_elements(s: str) -> str:
    """counts how many elements are in the string."""
    
    regex = "\S" # where the string does not contain a whitespace
    elements = re.findall(regex, s)
    count = len(elements)
    
    return f"{count} elements"


sentence = "I love learning"
print(count_words(sentence))
print(count_elements(sentence))
