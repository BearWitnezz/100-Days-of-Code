# TODO 1: Define a Question class. One object holds a single quiz question and the correct answer.

# TODO 2: __init__ takes the question text and the answer, after self.

# TODO 3: Save the text on self.text and the answer on self.answer.
#   Nudge: without self., those names only exist inside __init__ and the rest of the quiz cannot see them.

class Question:
    """Holds one quiz question and its correct answer."""
    def __init__(self, text, answer):
        """Set up a question with its text and correct answer."""
        self.text = text
        self.answer = answer


