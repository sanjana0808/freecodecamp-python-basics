def division(x):
    x = x/2
    return x

def multiplication(x):
    x = x*2
    return x

num = int(input("Enter a number: "))

if num < 10:
    print(division(num))

if num > 10:
    print(multiplication(num))
