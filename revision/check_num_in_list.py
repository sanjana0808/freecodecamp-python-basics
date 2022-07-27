list_of_num = [1, 4, 10, 3, 4]

#METHOD 1:

# def check_num(x):
#     i = 0
#     n = len(x)
#     user_input = int(input("Enter a number: "))
#     while i < n:
#         if user_input == x[i]:
#             return True
#         i = i + 1
#     return False
#
#
# print(check_num(list_of_num))

#METHOD 2: Using "in" operator

def check_num(x):
    user_input = int(input("Enter a num: "))
    if user_input in list_of_num:
        return True
    return False

print(check_num(list_of_num))