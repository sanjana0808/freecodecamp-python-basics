# # METHOD 1: While Loop
#
# def exponent(base, power): #2 , 3
#     i = 0
#     output = 1
#     while i < power:
#         output = output*base
#         i = i + 1
#     return output
#
# print(exponent(2, 3))
#
# # METHOD 2:
# print(2**3)

#METHOD 3: For loop

def exponent(base_num, power_num):
    output = 1
    for i in range(power_num):
        output = output*base_num
    return output

print(exponent(2, 3))
