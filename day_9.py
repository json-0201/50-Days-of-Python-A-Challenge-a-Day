# Biggest Odd Number

def biggest_odd(s: str) -> int:
    """returns the biggest old number in the list."""
    
    odds = [int(n) for n in s if int(n)%2==1]
    
    return max(odds)

print(biggest_odd("23569"))


# Extra Challenge: Zeros to the End

def zeros_last(l:list) -> list:
    """move zeros to the end of the list and maintain the order,
    return the sorted original list if no zeros."""
    
    if 0 in l:
        for i, n in enumerate(l):
            if n == 0:
                z = l.pop(i)
                l.append(z)
        return l
    
    else:
        return sorted(l)

print(zeros_last([1,4,6,0,7,0,9]))
print(zeros_last([2,1,4,7,6]))
