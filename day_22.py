# Add Under_Score

def add_hash(s: str) -> str:
    """adds a hash# between the words."""

    return "#".join(s)

print(add_hash("Python"))


def add_underscore(s:str) -> str:
    """removes the hash# and replaces it with an underscore_."""
    
    return s.replace("#", "_")

print(add_underscore(add_hash("Python")))


def remove_underscore(s:str) -> str:
    """removes the underscore_ and replaces it with nothing."""

    return s.replace("_", "")

print(remove_underscore(add_underscore(add_hash("Python"))))
