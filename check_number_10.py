def division(x):
    print("running division")
    x = x/2
    return x

def multiplication(x):
    print("running multiplication")
    y = x*2
    return y

num = int(input("Enter a number: "))

if num > 10:
    y = division(num)
else:
    y = multiplication(num)

print(y)