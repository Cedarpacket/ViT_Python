# ITP Week 1 Day 2 (In-Class) Practice

# a. assign a variable 'subtotal' to 17.75
subtotal = 17.75
# b. assign a variable 'tax_percentage' to .18
taxPercentage = 0.18
# c. assign a variable 'tax_amount' to the product of subtotal and tax_percentage 
taxAmount = subtotal * taxPercentage
# d. assign a variable 'total' to the sum of subtotal and tax_amount
total = subtotal + taxAmount
taxAmount = round(taxAmount, 2)
total = round(total, 2)
print(f"Subtotal: ${subtotal}")
print(f"Tax Percentage: {taxPercentage * 100} %")
print(f"Tax Amount: ${taxAmount}", ) # rounded to 2 decimal places for currency format
print(f"Total: ${total}", ) # rounded to 2 decimal places for currency format

input("")