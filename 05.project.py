#function to check if number is special
def is_special_number(num)
    original_num = num
    num_digit = 0
    temp = num

    #find the number of digit using while loop
    while temp > 0:
        temp //= 10
        num_digits += 1

    #recalculate the sum of the digits raised to the power
    temp = num
    special_sum = 0
    while temp > 0:
        digit = temp % 10
        special_sum += digit ** num_digits
        temp //= 10

    #return true if special sum is equal to original number
    return special_sum == original_num

#get user input for range
start = int(input("enter number for starting range"))
end = int(input("input number ending range"))

#print the special number
print(f"special number between {start} and {end}")
for num in range(start, end +1):
    if is_special_number(num):
        print(num)