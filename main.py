def welcome():
    print("Student Management System - Feature 1")

def student_details():
    print("Student Management System")

student_details()

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