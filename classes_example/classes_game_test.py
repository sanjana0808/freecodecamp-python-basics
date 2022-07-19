from classes_test import Question

prompts = ["Color of apples:\n a- red\n b- blue\n c- green\n\n",
           "Color of bananas:\n a- red\n b- yellow, c- green\n\n",
           "Color of grapes:\n a= red\n b- green, c- blue"
           ]

questions = [
    Question(prompts[0], "a"),
    Question(prompts[1], "b"),
    Question(prompts[2], "b")
]

def play_game(mcq):
    score = 0
    total_questions= len(mcq)
    for question in mcq:
        user_answer = input(question.prompt)
        if user_answer == question.answer:
            score = score + 1
    return f"You scored {score} out of {total_questions}"

print(play_game(questions))

