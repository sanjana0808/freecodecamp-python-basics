def check_number():
    my_list = [2, 4, 7, 10, 1]
    i = 0
    n = int(input("Enter a number: "))
    length = len(my_list)

    while i < length:
        if n == my_list[i]:
            return True
        i=i+1
    return False
print(check_number())






# def check_number():
#     my_list = [2, 4, 7, 10, 1]
#     i = 0
#     n = int(input("Enter a number: "))
#     length = len(my_list)
#
#     while i < length:
#         if n == my_list[i]:
#             return True
#             # Position 2, incorrect i = i + 1
#         # else:
#             # pass  #this will work because we are not returning anything from else
#             # return False
#             # Position 3, incorrect i = i+1
#         i=i+1# Position 1, which is correct
#     return False
# print(check_number())