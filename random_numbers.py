import random
def generate_random_numbers(n):
    random_integers = []
    i = 0
    while i < n:
        a = random.randint(1, 1000)
        random_integers.append(a)
        i = i + 1
    return random_integers
print(generate_random_numbers(5))

