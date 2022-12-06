# Are They Equal?

def equal_strings(a: str, b: str) -> bool:
    """returns True if both strings have the same characters and have equal length."""
    
    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(equal_strings("love", "evol"))


# Extra Challenge: Swap Values

def swap_values(l: list) -> list:
    """returns a list with swapped first element & last element."""
    
    temp = l[0]
    l[0] = l[-1]
    l[-1] = temp
    
    return l

print(swap_values([2,4,67,7]))
