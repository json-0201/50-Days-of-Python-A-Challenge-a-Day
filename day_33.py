# Just Digits

def just_digits(file):
    """Returns only digit elements from the file."""

    digits = []

    with open(file, "r") as f:
        content = f.read()
        for word in content.split():
            if word.isdigit():
                digits.append(word)
    
    return digits

print(just_digits("python.csv"))
