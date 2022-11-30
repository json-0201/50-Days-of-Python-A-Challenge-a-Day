# User Name Generator

def user_name() -> str:
    """returns username (before @)."""
    
    email = input("Enter your email:")
    username = email.split("@")[0]
    
    return username

print(user_name())


# Extra Challenge: Zero Both ends

def zeroed(l: list) -> list:
    """returns list with zeroed ends"""
    
    l[0], l[len(l)-1] = 0, 0
    
    return l

print(zeroed([2,5,7,8,9]))
