# Pay Your Tax

def your_vat() -> int:
    """return the price of the item plus VAT."""
    
    while True:
        try:
            price, vat = map(int, input("Enter price and VAT of the item(price, vat):").split(","))
            break
        except ValueError:
            print("Enter valid numbers!")
    
    return round(price*(1+(vat/100)))

print(your_vat())


# Extra Challenge: Pyramid of Snakes
from emoji import emojize

def Python_snakes(n: int):
    """creates a pyramid of snakes"""
    
    for i in range(n):
        
        # left hand side
        print(" "*(n-i), end="")
        print(emojize(":snake:")*(1+(2*i)), end="")
        print(" "*(n-i), end="")
        print()

Python_snakes(7)
