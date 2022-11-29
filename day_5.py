# My Discount

def my_discount():
    """user inputs the price and discount,
    returns the price after the discount."""
    
    p, d = input("Enter price, discount(%):").split()
    fp = int(p) * (1-(int(d)/100))
    
    return "%.1f" % fp

print(my_discount())


# Extra Challenge: Tuple of Student Sex
sex = []
students = ['Male', 'Female', 'female', 'male', 'male', 'male', 
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
students = [ele.lower() for ele in students]

m, f = students.count("male"), students.count("female")
m_tuple, f_tuple = ("Male",m), ("Female",f)
sex.extend([m_tuple, f_tuple])

print(sex)
