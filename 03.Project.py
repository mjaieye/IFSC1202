#enter the operator
operator = input("enter the operator (+ - * /): ")
#enter number
num1 = float(input("enter the 1th number"))
num2 = float(input("enter the 2ed number"))
#enter the operation
if operator == "+":
    result = num1 + num2
    print(result)
elif operator =="-":
    print(result)
    result = num1 - num2
    print(result)
elif operator == "*":
    result = num1 * num2
    print(result)
elif operator == "/":
    result = num1 / num2
    print(result)
else:
    print(f"{operator} is not a valid operator")
