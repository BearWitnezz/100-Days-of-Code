# TODO 1 (question_model.py): Make a Question class with __init__ that sets text and answer. Add a docstring. (done in lesson)
# TODO 2 (main.py): Import Question and question_data. Make an empty question_bank list. Before or inside the loop? (done)
# TODO 3 (main.py): Loop through question_data. For each dict, build a Question object from its text and answer, then append it to question_bank. (done)
# TODO 4 (quiz_brain.py): Make a QuizBrain class. __init__ takes the question list and sets question_number to start at 0 (a default value). (done)
# TODO 5 (quiz_brain.py): Write next_question(self). Grab the current question, bump the number, and ask the user True/False with input. (done)
# TODO 6 (quiz_brain.py): Write still_has_questions(self). Return True or False. Compare question_number to what? (done)
# TODO 7 (main.py): Make a QuizBrain object, then use a while loop with still_has_questions to keep asking. (done)
# TODO 8 (quiz_brain.py): Add score = 0 as a default. Write check_answer(self, user_answer, correct_answer). Compare them (watch upper/lower case), add to score if right, and print the score. (done)
# TODO 9 (main.py): After the loop ends, print the final score. Run after every TODO. (done)

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