import random
## Input = eg 3
## Output = [131, 431, 231]
def ran_num(x): #example x = 3
    i = 0
    l = []
    while i < x:
        a = random.randint(1, 1000) #this will give a random number bet 1 and 1000
        l.append(a)
        i = i + 1 # this will control the loop
    return l

user_ip = int(input("Enter a number: "))
print(ran_num(user_ip))
