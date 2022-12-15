# Capitalize First Letter

def capitalize(s: str) -> str:
    """capitalizes the first letter of each word."""
    
    capitalized = []
    for word in s.split():
        capitalized.append(word.capitalize())

    return " ".join(capitalized)

print(capitalize("i like learning"))


# Extra Challenge: Reversed List
str1 = "leArning is hard, bUt if You appLy youRself\
    you can achieVe success"

def uppercase_reversed_list(s: str) -> list:
    """returns a reversed list of words containing uppercase"""
    
    new_list = []
    for word in s.split():
        if any(char.isupper() for char in word):
            new_list.append(word[::-1])
            
    return new_list

print(uppercase_reversed_list(str1))
