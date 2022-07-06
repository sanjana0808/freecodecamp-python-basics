def addition(x, y):
    z = x + y
    return z
def multiplication(x, y):
    z = x*y
    return z
def division(x, y):
    z = x/y
    return z
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operation: ")
if operation == "+":
    y= addition(num1, num2)
    print(y)
elif operation == "*":
    z= multiplication(num1, num2)
    print(z)
elif operation == "/":
    a= division(num1, num2)
    print(a)
else: print("not a valid choice")
