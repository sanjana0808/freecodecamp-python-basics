def factorial(x):
    y = 1
    while x >= 1:
        y = y*x
        x = x - 1
    return y

print(factorial(3))