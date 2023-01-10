# Only Words with Vowels

def words_with_vowels(s: str) -> list:
    """Returns a list of only words with vowels in them."""

    res = []

    for word in s.split():
        if [char for char in word if char.lower() in ["a","e","i","o","u"]]:
            res.append(word)

    return res

print(words_with_vowels("You have no rhythm"))


# Extra Challenge: Class of Cars

class Car:
    def __init__(self, model, color, year, transmission, electric=False):
        """Initilaize a car object."""
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric
    
    def print_cars(self):
        print(f"Model = {self.model}")
        print(f"Color = {self.color}")
        print(f"Year = {self.year}")
        print(f"Transmission = {self.transmission}")
        print(f"Electric = {self.electric}")

class BMW(Car):
    def __init__(self, model, color, year, transmisstion, electric=False):
        super().__init__(model, color, year, transmisstion, electric)

class Tesla(Car):
    def __init__(self, model, color, year, transmisstion, electric=False):
        super().__init__(model, color, year, transmisstion, electric)

class Ford(Car):
    def __init__(self, model, color, year, transmisstion, electric=False):
        super().__init__(model, color, year, transmisstion, electric)

bmw1 = BMW("X6", "Silver", 2018, "Auto", False)
bmw1.print_cars()

tesla1 = Tesla("S", "Beige", 2017, "Auto", True)
tesla1.print_cars()

ford1 = Ford("Focus", "White", 2020, "Auto", False)
ford1.print_cars()
