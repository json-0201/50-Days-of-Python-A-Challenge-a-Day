# Any Number of Arguments

def any_number(*nums):
    """return the average of input numbers."""
    
    total = 0
    for num in nums:
        total += num
    
    return total/len(nums)

print(any_number(12, 90, 12, 34))
print(any_number(12, 90))


# Extra Challenge: Any Number of Arguments

def add_reverse(l1: list, l2: list) -> list:
    """adds each corresponding number and reverses the outcome."""

    if len(l1) != len(l2):
        print("Lists must have same length!")
        quit()
        
    result = []
    for i in range(len(l1)):
        result.append(l1[i]+l2[i])
        result.reverse()
        
    return result

print(add_reverse([10,12,34], [12,56,78]))
