def rev_order(num):
    num = str(num)
    n = len(num)
    i = n-1
    new_num = ""
    while i >= 0:
        new_num = new_num + num[i]
        i = i - 1
    return int(new_num)

print(rev_order(2398))