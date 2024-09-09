start = int (input("enter the starting range"))
end = int (input("enter the ending range"))
print ("prime number in range", start, "to", end)
for i in range(start, end+1):
    flag = 0
    for n in range(2, i):
        if (i % n == 0):
            flag = 1
            break
    if (flag == 0):
        print (i, end = ' ')
