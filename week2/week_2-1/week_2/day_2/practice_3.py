# ITP Week 2 Day 2 (In-Class) Practice 3

# Functions Parameters and Arguments

# Lets take those functions we built in practice_2 
# and make them more dynamic:

# Rewrite the functions from practice_2 using parameters:
def add_num(x, y):
    sum = int(x) + int(y)
    print(sum)

def subtract_num(x, y):
    difference = int(x) - int(y)
    print(difference)

def multiply_num(x, y):
    product = int(x) * int(y)
    print(product)

def divide_num(x, y):
    quotient = int(x) / int(y)
    print(round(quotient))

# Don't forget to call your functions to make sure they work 
# Uncomment to call your functions:
print("I should see the number 7 below from add_num: ")
add_num(3, 4)

print("I should see the number -2 below from subtract_num: ")
subtract_num(6, 8)

print("I should see the number 18 below from multiply_num: ")
multiply_num(2, 9)

print("I should see the number 2 below from divide_num: ")
divide_num(10, 5)

# Extra Time?
# Now take in 2 users inputs and pass them in as arguments when calling the functions
print("I should see the sum of the two numbers I input below: ")
add_num(input("Enter a whole number: "), input("Enter another whole number: "))
print("I should see the difference of the two numbers I input below: ")
subtract_num(input("Enter a whole number: "), input("Enter another whole number: "))
print("I should see the difference of the two numbers I input below: ")
multiply_num(input("Enter a whole number: "), input("Enter another whole number: "))
print("I should see the quotient of the two numbers I input below: ")
divide_num(input("Enter a whole number: "), input("Enter another whole number: "))
