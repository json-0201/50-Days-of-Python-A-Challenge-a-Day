# List Intersection

def inter_section(l1: list, l2: list) -> tuple:
    """Returns a tuple of intersections in two lists."""

    result = tuple([num for num in l1 if num in l2])

    return result

list1 = [20, 30, 60, 65, 75, 80, 85] 
list2 = [ 42, 30, 80, 65, 68, 88, 95]

print(inter_section(list1, list2))


# Extra Challenge: Set or list
import timeit

s = """\
a = range(10000000)
x = set(a)
i = 9999999
if i in x:
    pass
"""

l = """\
a = range(10000000)
y = list(a)
i = 9999999
if i in y:
    pass
"""

print(f"execution time for set: {timeit.timeit(stmt=s, number=1)}")
print(f"execution time for list: {timeit.timeit(stmt=l, number=1)}")
