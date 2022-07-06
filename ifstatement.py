is_male = True
is_tall = False
if is_male and is_tall:
    print("You are a tall male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
elif is_male and not(is_tall):
    print("You are a male but not tall")
else:
    print("You are not male or not tall")

def max_num(x, y, z):
    if x>=y and x>=z:
        return x
    elif y>=x and y>=z:
        return y
    else:
        return z
print(max_num(10000, 2000, 30000))
