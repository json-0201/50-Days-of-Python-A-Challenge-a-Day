# Simple Calculator

class Calculator:
    """A simple calculator."""
    def calculator(self):
        """User chooses an operation and inputs two numbers."""

        operation = input("Choose an operation [add/subtract/multiply/divivde]: ")
        
        if operation not in ["add", "subtract", "multiply", "divide"]:
            raise NameError ("Please choose a valid operation!")
        
        self.num1 = float(input("Enter first number: "))
        self.num2 = float(input("Enter second number: "))

        if operation == "add":
            self.add()
        elif operation == "subtract":
            self.subtract()
        elif operation == "multiply":
            self.multiply()
        elif operation == "divide":
            if self.num2 == 0:
                raise ZeroDivisionError ("Cannot divide by zero!")
            self.divide()

    
    def add(self):
        print(f"{self.num1} + {self.num2} = {self.num1+self.num2}")
    def subtract(self):
        print(f"{self.num1} - {self.num2} = {self.num1-self.num2}")
    def multiply(self):
        print(f"{self.num1} * {self.num2} = {self.num1*self.num2:.2f}")
    def divide(self):
        print(f"{self.num1} / {self.num2} = {self.num1/self.num2:.2f}")

calc = Calculator()
calc.calculator()


# Extra Challenge: Multiply Words
s1 = "love live and laugh"
s2 = "Hate war love Peace"

def multiply_words(s: str) -> int:
    """Returns the multiplied value of the lengths of lowercase words."""

    s_lower = [word for word in s.split() if not any(char.isupper() for char in word)]
    
    res = 1
    for word in s_lower:
        res *= len(word)
    
    return res

print(multiply_words(s1))
print(multiply_words(s2))
