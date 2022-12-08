# Flatten the List

def flat_list(l: list) -> list:
    """returns a one-dimension list from a nested list."""

    while (type(l)==list and type(l[0])==list):
        l = l[0]
    
    return l
    
print(flat_list([[2,4,5,6]]))


# Extra Challenge: Teacher's Salary

def your_salary():
    """returns the teacher's name, periods taught, and gross salary."""

    name = input("Enter the name:")
    periods = int(input("Enter the number of periods:"))
    rate = int(input("Enter the monthly rate:"))
    
    if periods < 100:
        salary = periods*rate
    else:
        salary = 100*rate + (periods-100)*(rate*1.25)
    
    return name, periods, "%.2f" %salary

name, periods, salary = your_salary()
print(f"Teacher: {name}\nPeriods: {periods}\nMonthly salary: ${salary}")
