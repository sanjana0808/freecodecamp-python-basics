list_of_integers = [9, 10, 11, 5, 1]
def max_number():
    i = 0
    n = 5
    max_val = list_of_integers[0]
    while i < n:
        if max_val < list_of_integers[i]:
            max_val = list_of_integers[i]
        i = i + 1
    return max_val
print(max_number())
