# Count the Dots

def count_dots(s: str) -> int:
    """returns the number of dots in the string."""
    
    return s.count(".")

print(count_dots("h.e.l.p."))
print(count_dots("he.lp."))


# Extra Challenge: Your Age in Minutes
import datetime

def age_in_minutes() -> int:
    """returns age in minutes"""
    
    year_current = datetime.date.today().year
    year_user = 0
    
    while len(str(year_user)) != 4 or (year_user<1900 or year_user>year_current):
        
        if len(str(year_user)) != 4:
            print("Enter 4-digit year.")
        elif year_user<1900 or year_user>year_current:
            print("Your input is invalid!")
            
        year_user = int(input("Enter your year of birth(####):"))
        min_user = "{:,}".format((year_current-year_user)*365*24*60)
    return f"You are {min_user} minutes old."

print(age_in_minutes())
