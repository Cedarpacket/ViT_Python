# ITP Week 1 Day 3 (In-Class) Practice

# Take an user's input and assign it to a variable named "student_grade_string"
studentGradeString = input("What was your student's grade? ")
# The user input comes in as a string so we have to cast it to a Int to a variable named "student_grade_int"
studentGradeInt = int(studentGradeString)

# Create an If statement with the appropriate Elif and Else statement for the following grading system.

"""
A : 90 - 100
B : 80 - 89
C : 70 - 79
D : 60 - 69
F : 0 - 59
"""

# Within each "block" print out the appropriate letter grade.
if studentGradeInt >= 90:
    print("Letter Grade: A")
elif studentGradeInt >= 80:
    print("Letter Grade: B")
elif studentGradeInt >= 70:
    print("Letter Grade: C")
elif studentGradeInt >= 60:
    print("Letter Grade: D")
else:
    print("Letter Grade: F")