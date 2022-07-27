def reverse_string(x):
    n = len(x)
    i = n - 1
    empty_string = ""
    while i >= 0:
        empty_string = empty_string + x[i]
        i = i - 1
    return empty_string


a = "karan"
b = reverse_string(a)

if a == b:
    print("It is a palindrome")
else:
    print(" It is not a panlindrome")

#palindrome function: input is string and reverse string, return true or false

def palindrome(x, y):
    if x == y:
        return True
    return False

print(palindrome(a, b))

