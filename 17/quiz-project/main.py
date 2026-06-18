from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

"""the data from the data.py is converted into an object which is easy and
full proof way of accessing question and answer """
queston_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    queston_bank.append(new_question)

quiz = QuizBrain(queston_bank)
# quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
# teestting