def welcome():
    print("Welcome to Student Management System")

def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

welcome()
print("Student Grade:", calculate_grade(85))