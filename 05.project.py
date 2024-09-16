# Function to check if a number is special
def is_special_number(num):
    original_num = num
    num_digits = 0
    temp = num

    # Find the number of digits using while loop
    while temp > 0:
        temp //= 10
        num_digits += 1

    # Recalculate the sum of the digits raised to the power of num_digits
    temp = num
    special_sum = 0
    while temp > 0:
        digit = temp % 10
        special_sum += digit ** num_digits
        temp //= 10

    # Return True if special_sum equals the original number
    return special_sum == original_num

# Get user input for the range
start = int(input("Enter Start of Range: "))
end = int(input("Enter End of Range: "))

# Print the special numbers in the range
print(f"Special Numbers between {start} and {end}")
for num in range(start, end + 1):
    if is_special_number(num):
        print(num)
