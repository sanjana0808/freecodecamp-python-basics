correct_guess = "Karan"
user_guess = ""
guess_count = 0
guess_limit = 4
out_of_guessess = False
while user_guess != correct_guess and not (out_of_guessess):
    if guess_count < guess_limit:
        user_guess = input("Enter correct answer: ")
        guess_count = guess_count + 1
    else:
        out_of_guessess = True
if out_of_guessess:
    print ("You are a looser")
else:
    print ("You are a champ")