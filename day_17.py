# User Name Generator

from random import randint

def user_name() -> str:
    """returns a username - reverse the name and attach a randomly issued number between 0-9"""

    name = input("Enter your name:")
    username = name[::-1] + str(randint(0, 9))
    return username

print(user_name())


# Extra Challenge: Sort by Length

def sort_length(l: list) -> list:
    """sorts the strings in ascending order according to their length."""

    
    for i in range(len(l)):
        for j in range(len(l) - 1):
            if len(l[j]) > len(l[j+1]):
                l[j], l[j+1] = l[j+1], l[j]
    
    return l

names = [ "Peter", "Jon", "Andrew"]
print(sort_length(names))
