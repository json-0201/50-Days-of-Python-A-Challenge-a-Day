# Pig Latin

def translate(s: str) -> str:
    """Translates the input text into Pig Latin."""

    result = []

    for word in s.split():
        if word[0] in ["a","e","i","o","u"]:
            result.append((word+"yay").lower())
        else:
            word += word[0]
            word = word[1:]
            result.append((word+"ay").lower())

    result[0] = result[0].title()
    return " ".join(result)

a = "i love python"
print(translate(a))
