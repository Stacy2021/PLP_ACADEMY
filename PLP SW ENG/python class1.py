# Prompt the user to enter the first number and convert it to float
num1 = float(input("Enter first number: ")) 

# Prompt the user to enter the second number and convert it to float
num2 = float(input("Enter second number: "))

# Calculate the sum of the two numbers
sum_result = num1 + num2

# Calculate the difference between the two numbers
difference_result = num1 - num2

# Calculate the product of the two numbers
product_result = num1 * num2

# Calculate the quotient, handling division by zero
quotient_result = num1 / num2 if num2 != 0 else "undefined (division by zero)"

# Display the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Quotient: {quotient_result}")

# This script performs basic arithmetic operations on two numbers provided by the user.
# It calculates the sum, difference, product, and quotient of the two numbers.
# It handles division by zero gracefully.