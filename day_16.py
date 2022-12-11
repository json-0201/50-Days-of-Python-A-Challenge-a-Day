# Sum the List

def sum_list(l: list) -> int:
    """returns the sum of the integers."""
    
    n = len(l)
    total = 0
    
    for i in range(n):
        total += sum(l[i])
        
    return total

print(sum_list([[2,4,5,6],[2,3,5,6]]))


# Extra Challenge: Unpack A Nest
Nested_list = [[12, 34, 56, 67], [34, 68, 78]]

new_list = []
for array in Nested_list:
    for num in array:
        if num in [34, 67,78]:
            new_list.append(num)

new_list = list(set(new_list))

print(new_list)
