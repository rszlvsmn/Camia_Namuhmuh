# Activity Title: Sum and Difference Calculator
# ---------------------------------------------



# Variables
sum = 0
difference = 0

# Get User Input
num1 = int(input("Enter a number:  "))
num2 = int(input("Enter another number:  "))

# Calculate Sum
def calculate_sum():
    global sum
    sum = num1 + num2
    return sum

# Calculate Difference
def calculate_difference():
    global difference
    difference = num1 - num2
    return difference

# Print Results
print("Sum:", calculate_sum())
print("difference:", calculate_difference())