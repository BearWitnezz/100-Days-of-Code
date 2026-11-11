# TODO 1: Define a QuizBrain class. It asks each question and keeps the score.

# TODO 2: __init__ takes the question list. Start question_number at 0, save the list, and start score at 0.

# TODO 3: still_has_questions() returns True while question_number is less than the length of the question list.
#   It returns False once the quiz is out of questions.

# TODO 4: next_question() takes the question at the current question_number, then adds 1 to question_number.

# TODO 5: Ask "Q.{number}: {question text}. (True/False): " and pass the user's answer, plus that question's
#   answer, to check_answer.

# TODO 6: check_answer(user_answer, correct_answer) compares the two in lowercase.

# TODO 7: A match prints "You got it right!" and adds 1 to the score. Anything else prints "You got it wrong!".

# TODO 8: Either way, print "The correct answer was: {answer}.", then "Your current score is:
#   {score}/{question_number}.", then a blank line.

class QuizBrain:
    """Asks each quiz question and keeps the score."""
    def __init__(self, question_list):
        """Set up the quiz with a list of questions, starting at question 0."""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """Return True if there are questions left, False if the quiz is over."""
        return self.question_number < len(self.question_list)

    def next_question(self):
        """Show the current question, move to the next number, and ask for True/False."""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """Check the answer for the current question."""
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}.")
        print("\n")


