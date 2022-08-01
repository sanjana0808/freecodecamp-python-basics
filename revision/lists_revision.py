groceries = ["egg", "meat", "butter", "oil", "rice"]

for grocery in groceries:
    print(grocery)

for index, grocery in enumerate(groceries):
    print(index, grocery)

i = 0
n = len(groceries)
while i < n:
    print(groceries[i])
    i = i+ 1