# Average Calories

def average_calories():
    """Returns the average calories intake of a uesr."""
    
    cals = []
    day = 0

    print("==============================")
    print("Enter \"done\" when finished.")
    print("==============================")

    while True:

        cal = input(f"Enter the calories intake: ")
        
        if cal.lower() == "done":
            break
        
        elif cal.isnumeric():
            print(f"\tCalories intake for day-{day+1}: {cal}")
            cals.append(int(cal))
            day += 1

        else:
            continue
    
    return f"Average calories intake over {day}-days: {sum(cals)/day:.2f}" if cals\
        else "No calorie intake input!"

print(average_calories())


# Extra Challenge: Create a Nested List

def nested_lists(*l: list) -> list:
    """Creates a 2-D nested list of input lists."""

    new_list = []
    for list in l:
        new_list.append(list)
    return new_list

print(nested_lists([1,2,3,5], [1,2,3,4], [1,3,4,5]))
