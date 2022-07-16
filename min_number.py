my_list = [5, 8, 3, 10, 1]
def min_num():
    i = 0 #Step 1: initialize the value of i(index)
    n = len(my_list) # Step 2: Assign the value of the length of the string to a variable
    min_num = my_list[0] #Step 3: Assign the minimum number of your choice in the list to a variable
    while i < n: #Step 4: to compare the min number with other numbers in the list, make a while loop where/
                # i is less than the len of string
        if min_num > my_list[i]: #Step 5: Write a condition, where min num is greater than other integers\
                # of the list
            min_num = my_list[i] #Step 6: If the condition fulfills, assign the value of that integer to min num
        i = i + 1 #Step 7: Once the condition is checked, the value of i will be incresed by 1 to check other\
                    # numbers of the list
    return min_num
print(min_num())
