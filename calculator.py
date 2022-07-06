# num1 = input("Enter a number: ")
# num2 = input("Enter 2nd number: ")
# Result = float(num1) + float(num2)
# print(Result)

x = float(input("Enter a number: "))
op = input("Enter an operator: ")
y = float(input("Enter another number: "))
if op == "+":
    print(x+y)
elif op == "-":
    print(x-y)
else: print("invalid operator")
