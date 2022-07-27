list_of_num = [2, 10, 0, 8, 1]

def min_num():
    i = 0
    min_num = list_of_num[0]
    n = len(list_of_num)
    while i < n:
        if min_num > list_of_num[i]:
            min_num = list_of_num[i]
        i = i + 1
    return min_num

print(min_num())
