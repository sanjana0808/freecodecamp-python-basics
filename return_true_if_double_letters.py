def double_letters(s):
    n = len(s)
    i = 1
    while i < n:
        if s[i] == s[i - 1]:
            return True
        i = i + 1

    return False
print(double_letters("karan"))