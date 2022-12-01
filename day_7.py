# A String Range

def string_range(n):
    """returns a string of its range."""
    
    strings = [str(i) for i in range(n)]
    return ".".join(strings)

print(string_range(6))


# Extra Challenge: Dictionary of names
names = ["Joseph","Nathan","Sasha","Kelly",
         "Muhammad","Jabulani","Sera","Patel","Sera"]

def s(l):
    """return a dictionary of names starting with S: count"""
    
    result = {}
    items = [item for item in l if item[0].lower()=="s"]    
    for item in items:
        result[item] = items.count(item)
    
    return result

print(s(names))
