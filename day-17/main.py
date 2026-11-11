# TODO 1: Import Question from question_model, question_data from data, and QuizBrain from quiz_brain.

# TODO 2: Start an empty question bank.

# TODO 3: Loop through question_data. From each dictionary, take the "question" text and the "correct_answer".

# TODO 4: Build a Question from that text and answer, and append it to the bank.

# TODO 5: Create a QuizBrain and hand it the question bank.

# TODO 6: While the quiz still has questions, call next_question().

# TODO 7: When the loop ends, print "You've completed the Quiz!".

# TODO 8: Print "Your final score: {score}/{question_number}" from the quiz brain.

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