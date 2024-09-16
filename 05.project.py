def is_special(num):

    #calculate the number of digit
    temp = num
    sum_of_power = 0
    while temp > 0:
        digits = temp % 10
        sum_of_power += digit ** digit
        temp //= 10

    #sum each digit
    temp=num
    sum_of_power=0
    while temp>0:
        digit = temp%10
        sum_of_powers += digit ** digit
        temp //= 10

    #check if sum is equal
    return sum_of_power == num

#display special numbers in a range
def find_special_numbers(start, end):
    for num in range(start, end + 1):
        if is_special(num):
            print(num)

    #input for range
    start = int(input("Start of the range: "))
    end = int(input("End of the range: "))

#find and display speacial number
find_special_numbers(start, end)