#using while loop to solve the problem
def print_string(s):
    n=len(s)
    i=n-1
    while i >= 0:
        print(s[i])
        i=i-1

x = input("Enter a name: ")
print_string(x)