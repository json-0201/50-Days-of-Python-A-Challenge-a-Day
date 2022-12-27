# Unique Numbers

def unique_numbers(l: list) -> list:
    """Return the original list if the difference between
    the sum of all the numbers in the original list and the sum of unqiue numbers in the list
    is even; if odd, return the list with unique numbers."""

    list_unique = list(set(l))

    sum_unique = sum(list_unique)
    sum_original = sum(l)
    
    if (sum_original-sum_unique) % 2 == 0:
        return l

    else:
        return list_unique

print(unique_numbers([1,2,4,5,6,7,8,8]))


# Extra Challenge: Difference of two Lists
list1 = [1, 2, 4, 5, 6]
list2 = [1, 2, 5, 7, 9]

def difference(a: list, b: list) -> list:
    """Return all the elements that are in list a but not in list b and all the elements in list b but not in list a."""

    res1 = [num for num in a if num not in b]
    res2 = [num for num in b if num not in a]
    
    res = res1 + res2
    return res

print(difference(list1, list2))
