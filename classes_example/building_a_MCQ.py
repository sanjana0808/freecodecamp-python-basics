from Question import Question

question_prompts = [
    "What color are apples?\n(a)Red\n(b)Blue\n(c)orange\n\n",
    "What color are bananas?\n(a)Red\n(b)Blue\n(c)Yellow\n\n",
    "What color are mangoes\n(a)Red\n(b)Yellow\n(c)orange\n\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
    ]

def run_test(multiple_questions):
    score = 0
    total_questions = len(multiple_questions)
    for question in multiple_questions:
        user_answer = input(question.prompt)
        if user_answer == question.answer:
            score = score + 1
    return f"You scored {score} out of {total_questions}"

print(run_test(questions))









### program
# Step 1, add two number # function 1 addition
# Step 2, multiply result of step 1 with 54 # function2 multiply_with_54
# Step 3, check if result from step 2 is divisble by 4 # function3 check_divisibility_by_4
#  x = addition(3, 5)
#  x = multiply_with_54(x)