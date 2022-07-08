def exponent_power(base_num, power_num):
    Result = 1
    for index in range(power_num):
        Result = Result * base_num
    return Result
print(exponent_power(2, 2))



