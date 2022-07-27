def reverse_user_name(x):
    n = len(x)
    i = n - 1
    empty_string = ""
    while i >= 0:
        empty_string = empty_string + x[i]
        i = i - 1
    return empty_string

def reverse_user_name_2(x):
    n = len(x)
    i = n - 1
    empty_string = ""
    while i >= 0:
        empty_string = empty_string + x[i] + "\n"
        i = i - 1
    return empty_string

print(reverse_user_name_2("sanjana"))