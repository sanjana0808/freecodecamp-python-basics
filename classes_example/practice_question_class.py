class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_prompts = [
    "What color are apples?\n(a)Red\n(b)Blue\n(c)orange\n\n",
    "What color are bananas?\n(a)Red\n(b)Blue\n(c)Yellow\n\n",
    "What color are mangoes\n(a)Red\n(b)Yellow\n(c)orange\n\n"
]

my_questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "a")
]

def run_game(mcq):
    score = 0
    total_questions = len(mcq)
    for question in mcq:  # a = [10,20,13] for i in a:
        user_answer = input(question.prompt)
        if user_answer == question.answer:
            score = score + 1
    return f"You have scored {score} out of {total_questions}"

print(run_game(my_questions))