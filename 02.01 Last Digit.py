# Prompt the user for a number
number = int(input("Enter a number: "))

# Calculate the last digit
last_digit = number % 10

# Print the last digit using the .format method
print("Last Digit: {}".format(last_digit))