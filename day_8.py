# Odd and Even

def odd_even(l: list):
    """returns the difference between:
    the largest even number and the smallest odd number."""
    
    odds=[num for num in l if num%2==1]; odds.sort()
    evens=[num for num in l if num%2==0]; evens.sort()
    
    return evens[-1]-odds[0]

print(odd_even([1,2,4,6]))


# Extra Challenge: List of Prime Numbers
from primePy import primes

def prime_numbers():
    """returns a list of all the prime numbers within its range."""
    
    n = int(input("Enter a number:"))
    p = []
    
    for i in range(n):
        if primes.check(i):
            p.append(i)
    p.remove(1)
    
    return p

print(prime_numbers())
