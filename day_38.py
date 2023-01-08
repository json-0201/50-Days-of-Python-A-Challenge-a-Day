# Guess a Number
import random

def guess_a_number():
    """Plays a guessing game. Maximum of three tries."""

    number = random.randint(1,20)
    flag = False
    i = 3

    while i > 0:
        try:
            guess = int(input("Guess a number between 1 and 20: "))
        except ValueError:
            print("Input must be a number!")
            continue

        if guess < number:
            print("Guess too low!")
        elif guess > number:
            print("Guess too high!")
        else:
            flag = True
            break
        i -= 1
    
    return f"You won! The number was {number}" if flag else f"You lost! The number was {number}"

print(guess_a_number())


# Extra Challenge: Find Missing Numbers
numbers = [1, 2, 3, 5, 6, 7, 9, 11, 12, 23, 14, 15, 17,
        18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 31]

def missing_numbers(lst: list) -> list:
    """Returns the missing numbers in the sequence."""

    sequence = list(range(min(lst), max(lst) + 1))
    missing = [num for num in sequence if num not in lst]

    return missing

print(missing_numbers(numbers))
