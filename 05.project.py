def is_special(num):
    # Sum each digit raised to the power of itself
    temp = num
    sum_of_power = 0
    while temp > 0:
        digit = temp % 10
        sum_of_power += digit ** digit
        temp //= 10

    # Check if sum is equal to the original number
    return sum_of_power == num

# Display special numbers in a range
def find_special_numbers(start, end):
    for num in range(start, end + 1):
        if is_special(num):
            print(num)

# Input for range (should be outside the function)
start = int(input("Start of the range: "))
end = int(input("End of the range: "))

# Find and display special numbers
find_special_numbers(start, end)