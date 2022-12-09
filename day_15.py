# Same in Reverse

def same_in_reverse(s: str):
    """returns True if palindrome"""
    
    counter = 0
    for i in range(int(len(s)/2)):
        if s[i] != s[-1-i]:
            counter += 1
    
    return True if counter == 0 else False

print(same_in_reverse("dad"))


# Extra Challenge: What's My Age?
names_age = {
    "jane": 23,
    "kerry": 45,
    "tim": 34,
    "peter": 27}

def your_age():
    """returns the age of a student"""
    
    name = input("Enter your name:").lower()
    if name in names_age:
        return f"Hi, {name}, you are {names_age[name]} years old."
    
    else:
        print("You are not registered.")
        age = int(input("Enter your age:"))
        names_age[name] = age
        return f"Hi, {name}, you are {names_age[name]} years old."

print(your_age())
