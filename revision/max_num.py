list_of_num = [1, 3, 10, 5, 8]

def max_num(x):
    i = 0
    max_int = x[0]
    n = len(x)
    while i < n:
        if max_int < x[i]:
            max_int = x[i]
        i = i + 1
    return max_int

print(max_num(list_of_num))