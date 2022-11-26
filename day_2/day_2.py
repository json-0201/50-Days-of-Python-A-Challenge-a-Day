# Strings to Integers

def convert_add(list_str: list):
    """converts a list of strings to integers and sums the list."""
    
    list_str = [int(list_str[i]) for i in range(len(list_str))]
    list_sum = sum(list_str)
    print(list_str, list_sum)
    return list_str, list_sum

print("convert_add function:")    
convert_add(["1","3","5"])
print()


# Extra Challenge: Duplicate Names

def check_duplicates(list_str: list):
    """returns the duplicates. if no duplicates, returns "No duplicates"."""
    
    duplicates = []
    for ele in list_str:
        if list_str.count(ele) > 1:
            duplicates.append(ele)
    
    if duplicates:
        print("duplicates:", list(set(duplicates)))
    else:
        print("No duplicates")

print("check_duplicates function:")    
check_duplicates(["a","b","c"])
check_duplicates(["a","b","c","d","e","a","c"])
print()
