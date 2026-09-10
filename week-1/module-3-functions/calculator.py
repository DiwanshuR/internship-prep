def add(*nums):
    return sum(nums)

def subtract(a, b):
    return a - b

def multiply(*nums):
    ans = 1
    for x in nums:
        ans *= x
    return ans

def divide(a, b):
    if b == 0:
        print("Error: Division by zero not allowed.")
    return a/b

operation = input("enter your operation (add, subtract, multiply, divide): ")
if operation == "add":
    numbers = input("Enter numbers to add, separated by spaces: ")
    nums = [float(x) for x in numbers.split()]
    result = add(*nums)
    print(f"The result is: {result}")
    
elif operation == "subtract":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = subtract(a, b)
    print(f"The result is: {result}")
    
elif operation == "multiply":
    numbers = input("Enter numbers to multiply, separated by spaces: ")
    nums = [float(x) for x in numbers.split()]
    result = multiply(*nums)
    print(f"The result is: {result}")
    
elif operation == "divide":
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    result = divide(a, b)
    if b != 0:
        print(f"The result is: {result}")   
        
else:
    print("Invalid operation")