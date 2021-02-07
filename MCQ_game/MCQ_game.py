# for this game we will use Array,Class,def,for loop,If_else
from MCQ_Class_define import Question

# Array
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(A) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# Array & Class
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


# def & For loop
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct")


run_test(questions)
