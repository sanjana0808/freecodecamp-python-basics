def double_letters(x):
    i = 1
    n = len(x)
    while i < n:
        if x[i - 1] == x[i]:
            return True
        i = i + 1
    else:
        return False

print(double_letters("Sanj"))