def factorial(x):
    y = 1
    while x >= 1:
        y = y*x
        x = x - 1
    return y

print(factorial(3))

# using for loop

def factorial(y):#4*3*2*1
    i = y
    x = 1
    for j in range(y):
        x= x*i
        i = i -1
    return x
print(factorial(4))