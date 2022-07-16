def factorial(num):
    i = num
    x = 1
    while i >= 1:
        x = x*i
        i = i - 1
    return x
print(factorial(4))
y = factorial(5)
print(y)