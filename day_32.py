# Password Validator

def password_validator():
    """Validates a password."""

    pw = input("Enter a password: ")

    while True:
        # invalid password
        length = len(pw) < 8
        number = not any([char.isnumeric() for char in pw])
        lower = not any([char.islower() for char in pw])
        upper = not any([char.isupper() for char in pw])

        # if password does not meet all rules
        if length or number or lower or upper:
            if length:
                print("password must be at least 8 characters.")
            if number:
                print("password must include at least one number.")
            if lower:
                print("password must include at least one lowercase.")
            if upper:
                print("password must include at least one uppercase.")
            pw = input("Enter a password: ")
        
        else:
            print("valid password.")
            break

password_validator()


# Extra Challenge: Vaild Email
import re
emails = ['ben@mail.com', 'john@mail.cm', 'kenny@gmail.com', '@list.com']

def email_validator(l: list) -> list:
    """Returns valid email addresses."""
    
    exp = "^.+@.+\.com$"
    result = [email for email in emails if bool(re.search(exp, email))]

    return result

print(email_validator(emails))
