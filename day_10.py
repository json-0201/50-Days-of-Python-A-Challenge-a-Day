# Hide my Password

def hide_password():
    """returns a hidden password."""
    
    pw = input("Enter the password:")
    pw = len(pw) * "*"
    
    print(pw)
    print(f"Your password is {len(pw)} characters long.")
    
hide_password()


# Extra Challenge: A Thousand Separator

def convert_numbers(l: list) -> list:
    """returns a list of vlaues with applied thousand separators."""

    l = [str("{:,}".format(num)) for num in l]
        
    return l

print(convert_numbers([1000000, 2356989, 2354672, 9878098]))
