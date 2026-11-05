# Day 17 transcript notes (cards/quiz built ONLY from these)

## Lesson 1 - Creating your own classes
- Class = blueprint for creating objects; now we make our own.
- Project: day-17-start, file main.py.
- Syntax: `class User:` then indented body (transcript says "semicolon" but means colon `:`).
- Example: User class to model website users (what they have / can do).
- Create object: `user_1 = User()` (parentheses initialize). PyCharm shows "C" symbol for classes.
- Empty class/function -> "Indent Expected" error. Fix with `pass` keyword (just continue to next line).
- Naming: PascalCase for classes (every word capitalized, like a person's name - Blaise Pascal).
  camelCase = first word lowercase, later words capitalized (rare in Python).
  snake_case = all lowercase with underscores; used for pretty much everything else.

## Lesson 2 - Attributes, constructor (__init__), self, defaults
- Add attribute via dot notation: `user_1.id = "001"`. Attribute = variable associated with an object.
- Adding attributes one by one for each object is repetitive and typo-prone.
- Constructor = part of blueprint that says what happens when object is constructed (aka initializing).
- Python constructor: special `__init__` function (two underscores each side = special method the interpreter knows).
- `__init__` is called every time a new object is created from the class (e.g. a print inside it runs per object).
- `self` = the actual object being created/initialized. Add extra parameters after self; data passed in at construction sets attributes.
- Car example: `my_car = Car(5)` -> my_car.seats == 5, same as `my_car.seats = 5` after creating.
- `def __init__(self, user_id, username): self.id = user_id; self.username = username`
- Parameter and attribute names can differ (user_id -> self.id); convention is often same name.
- `user_1 = User("001", "angela")` -> 1 line instead of 3.
- Once __init__ has parameters, creating object without them errors: missing 2 required positional arguments.
- Default value: `self.followers = 0` (Instagram example) - not a parameter; every object starts at 0.

## Lesson 3 - Methods
- Attributes = what object has; methods = what object does. Function attached to object = method.
- Car race mode: `def enter_race_mode(self): self.seats = 2`; call `my_car.enter_race_mode()`.
- A method always needs `self` as the first parameter so it knows which object called it.
- Instagram: default attrs `self.followers = 0`, `self.following = 0`.
- `def follow(self, user): user.followers += 1; self.following += 1`
- self refers to the object inside the class blueprint; you never see self when *using* objects.
- `user_1.follow(user_2)` -> user_1: followers 0, following 1; user_2: followers 1, following 0.

## Lesson 4 - Quiz Game: Question model
- Quiz Game = True/False game; ask question, user picks True/False, tell right/wrong, give score.
- Download quiz-game-start zip from course resources, open in PyCharm.
- 4 files: data, main, question_model, quiz_brain.
- Task 1: question_model.py -> class Question with __init__ initializing text and answer.
- Example: `new_q = Question("2 + 3 = 5", "True")` -> constructor sets text and answer.
- Use PyCharm autofill: type def + init, hit Enter.
- `def __init__(self, q_text, q_answer): self.text = q_text; self.answer = q_answer`
- Attributes greyed/yellowed out "no effect" until they receive values from parameters.
- Access later with `new_q.text`.

## Lesson 5 - Question bank
- data.py: `question_data` = list of 12 dictionaries, each with "text" and "answer" keys.
- Warnings: Code > Auto-Indent Lines; lines >120 chars split with Enter (PyCharm adds quotes); newline at end of file; save unknown word ("Backrub") to project-level dictionary -> green check.
- List indentation doesn't change functionality (unlike methods/for loops).
- main.py: `from question_model import Question`, `from data import question_data`.
- Make empty `question_bank = []`, loop `for question in question_data:` -> question_text = question["text"], question_answer = question["answer"]; `new_question = Question(question_text, question_answer)`; `question_bank.append(new_question)`.
- Prints list of 12 Question objects.
- Why: converting string-key dicts (typo-prone) into objects with easy, foolproof attribute access + autocomplete; data from the internet often looks like this.

## Lesson 6 - QuizBrain & next_question
- QuizBrain class manages quizzing: asking next question, checking answer, checking end of quiz.
- Attributes: `self.question_number = 0` (default, tracks current question) and `self.question_list = q_list` (passed in = question bank).
- next_question: `current_question = self.question_list[self.question_number]`; increase `self.question_number += 1`; `input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")`.
- Each list item is a Question object -> use `.text` / `.answer`.
- main.py: `from quiz_brain import QuizBrain`; `quiz = QuizBrain(question_bank)`; `quiz.next_question()`.
- Number showed Q.0 at first because index starts at 0 for the first list item; fix by increasing question_number by 1 after grabbing the current question (same effect as +1, and it needs to increase every call anyway).
- Program exits after one question for now; next lesson keeps asking.

## Lesson 7 - still_has_questions + while loop
- Need to continue to next question after input. Method `still_has_questions` returns a boolean.
- main.py: `while quiz.still_has_questions(): quiz.next_question()` - loops until out of questions.
- Hint: relate question number and length of question list. `len(self.question_list)` = 12.
- Long version: if self.question_number < len(self.question_list): return True else: return False.
- question_number starts 0, goes to 1 inside next_question before the while check.
- Simplify: `return self.question_number < len(self.question_list)` - the comparison itself evaluates to True/False (e.g. return 5 > 3 -> True).
- Next lesson: checking the user's answer.

## Lesson 9 (?) - Open Trivia DB + modularity
- Swap question data: write your own, or use Open Trivia Database (opentdb) - free, user-contributed, 3000+ verified questions.
- Use its API: choose amount (10), category (computers), difficulty (easy), type (True/False) -> Generate API URL -> open URL.
- Data comes as JSON (JavaScript Object Notation) - looks pretty much like a Python dictionary.
- Paste into data.py; Code > Reformat Code to read it.
- Outer dict has "response_code" and "results" (list of 10 dicts). Remove the enclosing dict so question_data is a list of dicts.
- Each dict keys: category, type, difficulty, question, correct_answer, incorrect_answers.
- main.py change: question_text = question["question"], question_answer = question["correct_answer"].
- OOP advantage / modularity: only main.py knows about the data; QuizBrain untouched. QuizBrain only cares about tracking question number, next question, checking answer - unconcerned with where data comes from or its format.
- Teams: colleague can work on QuizBrain without knowing data structure; more complex than simple procedural code.
