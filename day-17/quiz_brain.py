class QuizBrain:
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


