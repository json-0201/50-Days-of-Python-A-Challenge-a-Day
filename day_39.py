# Password Generator
def generate_pasword():
    """A simple implementation of an interactive password generator."""
    from rstr import xeger

    while True:
        level = input("Choose password strength (weak / strong / very strong): ")
        if level.lower() in ["weak", "strong", "very strong"]:
            break
        else:
            print("Password strength must be either: weak / strong / very strong!")
            print()

    if level.lower() == "weak":
        return xeger(r"[a-zA-Z0-9.,?;':()!]{5}")
    elif level.lower() == "strong":
        return xeger(r"[a-zA-Z0-9.,?;':()!]{8}")
    elif level.lower() == "very strong":
        return xeger(r"[a-zA-Z0-9.,?;':()!]{12}")

print(generate_pasword())
