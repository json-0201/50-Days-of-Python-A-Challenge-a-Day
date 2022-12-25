# All the Same

def all_the_same(item: str or list or tuple) -> bool:
    """Checks if all the elements are the same -> returns True."""

    flag = True
    for i in range(len(item)-1):
        if item[i] != item[i+1]:
            flag = False
    
    return flag

print(all_the_same(["Mary", "Mary", "Mary"]))


# Extra Challenge: Reverse a String
str1 = "the love is real"

def read_backwards(s: str) -> str:
    """Takes a string as an argument and reverses it."""

    reversed = s.split()
    reversed.reverse()

    return " ".join(reversed)

print(read_backwards(str1))
