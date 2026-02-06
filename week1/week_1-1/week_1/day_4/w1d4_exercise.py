# # ITP Week 1 Day 4 Exercise
# # EASY
# lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
lowercase = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
# # 1. loop through the lowercase and print each element
for letter in lowercase:
    print(letter)
# # 2. loop through the lowercase and print the capitalization of each element
for letter in lowercase:
    print(letter.upper())
# # MEDIUM
# # 1. create a new variable called uppercase with an empty list
uppercase = []
# # 2. loop through the lowercase list
#     # 2a. append the capitalization of each element to the uppercase list
for letter in lowercase:
    uppercase.append(letter.upper())
# # HARD
# # A safe password has a minimum of (1) uppercase, (1) lowercase, (1) number, (1) special character.
# # password = "MySuperSafePassword!@34"
specialChar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
# # 1. create the following variables and assign them Booleans as False
while True:
    password = input("Enter a password: ")
    hasUppercase = False
    hasLowercase = False
    hasNumber = False
    hasSpecialChar = False
    hasTenChars = False
# # 2. loop through the string password (same as a list)
# # OR you can create a new list variable of the string password
# # using list(string) NOTE: assign it a new variable as such:
# # password_list = list(password) prior to looping.
    for char in password:
        if char in uppercase:
            hasUppercase = True
        elif char in lowercase:
            hasLowercase = True
        elif char in numbers:
            hasNumber = True
        elif char in specialChar:
            hasSpecialChar = True
# # 3. For each iteration of the loop, create a if statement
# # check to see if it exists in any of the list by using IN
# # if it does exist, update the appropriate variable and CONTINUE
# # not break.
#
# # NOTE: to see if it has a number, use range from 0 - 10!
# # 4. do a final check to see if all of your variables are TRUE
# # by using the AND operator for all 4 conditions. (This is done for you, uncomment below)
# final_result = hasUppercase == True and hasLowercase == True and hasNumber == True and hasSpecialChar == True
# # NOTE: we can shorthand this by just checking if the variable exists (returns True)
# #final_result_shorthand = has_uppercase and has_lowercase and has_number and has_special_char
# # this will fail the same if any one of them is False
# # If the final_result is true, print "SAFE STRONG PASSWORD"
# # else, print "Update password: too weak"
# # NOTE: this must be done outside of the loop

    if len(password) >= 10: # I added a password length to the program.
        hasTenChars = True

    if hasUppercase and hasLowercase and hasNumber and hasSpecialChar and hasTenChars:
        savedPassword = password
        print("Password accepted and saved.")
        break
    else:
        print("Password too weak. Issues:")

        if not hasUppercase:
            print("- Missing uppercase letter")
        if not hasLowercase:
            print("- Missing lowercase letter")
        if not hasNumber:
            print("- Missing number")
        if not hasSpecialChar:
            print("- Missing special character")
        if not hasTenChars:
            print("- Must be at least 10 characters long")
        print("Try again.\n")
# # BONUS: update the password variable to take in an user input!
# # NIGHTMARE: in the final check, use another if statement to list why it isn't a strong password!