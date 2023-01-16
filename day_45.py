# Words & Special Characters

def analyze_string(s: str) -> dict:
    """Returns a dictionary of the input string analysis."""
    import re
    result = {
        "special_character": 0,
        "words": 0,
        "total_characters": 0,
    }

    # total characters
    result["total_characters"] = len(s)
    # words
    result["words"] = len(re.findall("\w+", s))

    # special characters
    exp = "#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
    exp = [char for char in exp]
    for char in s:
        if char in exp:
            result["special_character"] += 1
    
    return result


text = "Python has a string format operator %. This functions \
analogously to printf format strings in C, e.g. \"spam=%s \
eggs=%d\" % (\"blah\", 2) evaluates to \"spam=blah eggs=2\"."
print(analyze_string(text))
