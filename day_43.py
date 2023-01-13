# Student Marks

def student_marks():
    """Records and returns the grades achieved by students on a test."""

    print("Enter \"q\" to exit.")
    result = {}    
    while True:
        name = input("Enter student's name: ")
        if name == "q":
            break
        grade = (input("Enter student's grade: "))
        if grade == "q":
            break
        try:
            float(grade)
        except ValueError as e:
            print("grade must be numeric!")
            continue

        result[name] = grade
    return result

print(student_marks())
