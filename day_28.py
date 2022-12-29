# Return Indexes

def index_position(s: str) -> list:
    """Returns the position or indexes of all lower letters."""

    result = [s.index(char) for char in s if char.islower()]

    return result

print(index_position("LovE"))


# Extra Challenge: Largest Number
list1 = [3, 67, 87, 9, 2]

def largest_number(l: list) -> int:
    """Returns the largest number possible using individual digits from the input list."""

    new_list = []

    # convert to single digit list
    for num in l:
        if len(str(num)) == 1:
            new_list.append(num)
        else:
            for i in range(len(str(num))):
                new_list.append(int(str(num)[i]))
    
    new_list.sort(reverse=True)
    new_list = [str(num) for num in new_list]
    result = "{:,}".format(int("".join(new_list)))

    return result

print(largest_number(list1))
