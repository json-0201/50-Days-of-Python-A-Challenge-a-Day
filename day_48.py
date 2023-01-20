# Binary Search

def search_binary(l: list, n: int) -> int:
    """Returns the index of 'n' in list 'l' after binary search."""

    # make a copy and sort the array
    l_original = l.copy()
    l.sort()

    # iterate through the sorted array
    start, end = 0, len(l)-1
    while start <= end:
        mid = (start + end) // 2
        if l[mid] == n:
            return l_original.index(n)
        elif l[mid] < n:
            start = mid + 1
        else:
            end = mid - 1
    
    # number not found
    return -1

list1 = [12, 34, 56, 78, 98, 22, 45, 13]
print(search_binary(list1, 22))
