from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []

for item in question_data:
    new_q = Question(item['question'], item['correct_answer'])
    question_bank.append(new_q)

# print(question_bank)

quiz = QuizBrain(question_bank)
ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")