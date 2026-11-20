# TODO 1: Import turtle, make the screen, and set the title to "U.S. States Game"
# TODO 2: Store the image file name in a variable
# TODO 3: Add the image as a shape on the screen and set the turtle's shape to it
# TODO 4: Ask the user for a state with a text input popup and save the answer
# TODO 5: Print the answer
# TODO 6: Keep the screen open
# TODO 7: Import pandas and read 50_states.csv
# TODO 8: Get all the state names as a list
# TODO 9: Make an empty list for guessed states
# TODO 10: Loop while fewer than 50 states have been guessed
# TODO 11: Ask for a state, with the title showing how many are correct out of 50
# TODO 12: Make the answer title case so any casing works
# TODO 13: If the answer is a real state, add it to the guessed list
# TODO 14: Get that state's row from the data
# TODO 15: Make a hidden turtle with its pen up, go to the state's x and y, and write the name
# TODO 16: If the answer is "Exit", break out of the loop
# TODO 17: Remove the line that keeps the screen open
# TODO 18: After the loop, make an empty missing states list
# TODO 19: Loop through all the states and add each one that wasn't guessed
# TODO 20: Turn the missing states into a DataFrame
# TODO 21: Save it as states_to_learn.csv

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state]
        state_x = state_data.x.item()
        state_y = state_data.y.item()
        location = turtle.Turtle()
        location.hideturtle()
        location.penup()
        location.goto(state_x,state_y)
        location.write(answer_state)

missing_states = []
for states in all_states:
    if states not in guessed_states:
        missing_states.append(states)
print(missing_states)
missed_states = pandas.DataFrame(missing_states)
missed_states.to_csv("states_to_learn.csv")

        
