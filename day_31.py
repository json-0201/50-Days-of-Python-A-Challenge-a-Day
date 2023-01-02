# Longest Word

def longest_word(l: list) -> tuple:
    """Returns the longest word and its number of characters."""

    word = max(l, key=len)
    length = len(word)

    return (word, length)

print(longest_word(["Java", "JavaScript", "Python"]))


# Extra Challenge: Create User

def create_user():
    """Saves user info per input and simulates a log-in."""

    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    password = input("Enter your password: ")
    
    user = {
        "name": name,
        "age": age,
        "password": password,
    }

    flag = False
    while not flag:
        n = input("Enter your name: ")
        p = input("Enter your password: ")
        
        if n == user["name"] and p == user["password"]:
            print("Logged in successfully.")
            flag = True
        else:
            print("Wrong password or username. Please try again!")

create_user()
