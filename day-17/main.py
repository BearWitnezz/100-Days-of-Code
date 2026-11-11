# TODO 1: Turn each item in the question data into a Question and store them in a list.
# TODO 2: Hand that list to a QuizBrain and keep asking while questions remain.
# TODO 3: When the quiz ends, print the score out of the number of questions asked.

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the Quiz!")
print(f"Your final score: {quiz.score}/{quiz.question_number}")