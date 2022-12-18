# List of Tuples

def make_tuples(l1: list, l2: list) -> tuple:
    """combines two lists into a list of tuples."""
    
    ls_tp = [(i,j) for i,j in zip(l1,l2)]
    return ls_tp

a, b = [1,2,3,4], [5,6,7,8]
print(make_tuples(a,b))


# Extra Challenge: Even Number or Average

def even_or_average():
    """returns the largest even number from the inputs, or average in absence of even numbers."""
    
    nums = input("Enter five numbers, separated by commas:").split(",")
    
    if any(int(num) % 2 == 0 for num in nums):
        return max([num for num in nums if int(num) % 2 ==0])
    else:
        total = 0
        for num in nums:
            total += int(num)
        return "%.2f" %(total / len(nums))
    
print(even_or_average())
