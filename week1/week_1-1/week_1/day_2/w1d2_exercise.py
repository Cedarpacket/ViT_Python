# ITP Week 1 Day 2 Exercise

import time #imports time and delays
import itertools #allows the looping of characters
import sys #runtime environment

"""
We will replicate a number magic trick with Python! Below is the magic trick that we will convert! 
Below that is the python instructions, you will need to complete.

Step 1: Pick a number from 1 - 9
Step 2: Multiple by 2
Step 3: Add 10 to the total
Step 4: Divide by 2
Step 5: Subtract by the original number
Final Number: 5

"""
# assign a variable "step_1" to a number of your choice between 1 - 9
    # step_1 = 4
# below will let the user type 0 and numbers over 9 causing errors.
    # magicNumber = int(input("Enter a number between 1 and 9: ")) 
# this will be my solution for the user incorrect input errors
while True:
    try:
        magicNumber = int(input("Enter a number between 1 and 9: ")) 
        if 1 <= magicNumber <= 9:
            break
        else:
            print("Please enter a valid number between 1 and 9.")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 9.")

# assign a variable "step_2" to the product of step_1 and the number 2
    # step_2 = step_1 * 2
        #magicMaths = (((magicNumber * 2) + 10) / 2) - magicNumber // this wont work here
# assign a variable "step_3" to the sum of step_2 and the number 10
    #step_3 = step_2 + 10
# assign a variable "step_4" to the quotient of step_3 and the number 2
    #step_4 = step_3 / 2
# assign a variable "step_5" to the difference between step_4 and step_1
    #step_5 = step_4 - step_1
# print step_5 and you should see 5!
# Added a little spinner animation, I did look up how to do this online.
spinner = itertools.cycle(["|", "/", "-", "\\"])
endTime = time.time() + 2
print("Calculating magic number ", end="", flush=True)
while time.time() < endTime:
    sys.stdout.write(next(spinner))
    sys.stdout.flush()
    time.sleep(0.1)
    sys.stdout.write("\b")
print("\nCalculation complete!")
magicMaths = (((magicNumber * 2) + 10) / 2) - magicNumber
print("The final number is:", int(magicMaths)) # I also looked into why the output was a float and converted it to an integer.
input("\nPress Enter to Close...")

# BONUS 1: can you convert step_1 to prompt a user's input?
    # HINT: you need to cast step_1 to a int because user input is a type string.
    # SEE magicNumber var
# BONUS 2: can you REFACTOR using less variables?
    # SEE magicMaths var

