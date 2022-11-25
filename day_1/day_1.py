# Division and Square-root
from math import sqrt

def divide_or_square(num: int):
    """returns the square root if divisible by 5,
    returns remainder if not divisible by 5."""
    
    if num % 5 == 0:
        print("\treturns", "%.2f" %sqrt(num))
        return sqrt(num)
    
    else:
        print("\treturns", int(num % 5))
        return int(num % 5)

print("="*45,"\n","Testing divide_or_square function:")
divide_or_square(10)


# Extra Challenge: Longest Value
def longest_value(dict):
    "returns the first longest value of the dictionary."

    max_len = 0
    for val in dict.values():
        if len(val) > max_len:
            max_len = len(val)
            long_val = val

    print("\tThe longest value of the dictionary is", long_val)

print("="*45,"\n","Testing longest_value function:")
fruits = {'fruit': 'apple', 'color': 'green'}
longest_value(fruits)
