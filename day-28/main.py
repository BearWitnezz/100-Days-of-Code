# TODO 1: Switch the canvas from pack() to grid(). Middle column, second row. (done)
# TODO 2: Title label "Timer" on the top row, middle column. Which keyword colors the text green? (done)
# TODO 3: Make the title big (FONT_NAME, 50) and blend it into the window. What does bg do? (done)
# TODO 4: Start button, left column, the row under the canvas. (done)
# TODO 5: Reset button, right column, same row as Start. (done)
# TODO 6: Get rid of the white border around the buttons. Same trick as the canvas. (done)
# TODO 7: Check mark label on the bottom row, middle column. Paste a ✔ as its text, green on yellow. (done)
# TODO 8: Save the canvas text in a variable so you can change it later. (done)
# TODO 9: count_down(count) in COUNTDOWN MECHANISM. Update the canvas text to count. Label uses config... what does a canvas use? (done)
# TODO 10: Make it loop with window.after. Wait 1 second, then call itself with one less. (done)
# TODO 11: Stop it at 0 so it doesn't go negative. (done)
# TODO 12: start_timer() in TIMER MECHANISM that kicks off count_down. Hook it to the Start button (parentheses or not?). (done)
# TODO 13: Count down minutes instead of seconds. How many seconds in a minute? (done)
# TODO 14: Show it as minutes:seconds. Which math function chops off decimals, and which operator gives the leftover seconds? (done)
# TODO 15: Make the seconds always show two digits (5:00, 4:09, 0:07). When is a number "too short", and how can an f-string add a 0 in front? (done)
# TODO 16: Make a global reps = 0. Bump it by 1 every time start_timer runs. What keyword lets a function change it? (done)
# TODO 17: Work out the work, short break, and long break seconds from your constants. (done)
# TODO 18: Pick which one to count down. Rep 8 = long break, even reps = short break, everything else = work. Which check has to go first? (done)
# TODO 19: When the countdown hits 0, start the next session on its own. (done)
# TODO 20: Change the title text and color for each session: Work green, short Break pink, long Break red. (done)
# TODO 21: Make the check mark label start out empty. (done)
# TODO 22: When a countdown hits 0, add one ✔ for every finished work session. How many reps make one work session? (done)
# TODO 23: reset_timer() in TIMER RESET, hooked to the Reset button (parentheses or not?). (done)
# TODO 24: Stop the running timer. Save what window.after gives back in a variable, then cancel it. Where does that variable need to live? (done)
# TODO 25: Put the timer text, title, and check marks back to how they started. (done)
# TODO 26: Hit Reset mid-timer, then Start. Does it start on Work? If not, what didn't reset? (done)
# TODO 27: Put your real minutes back (25, 5, 20). (done)

from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    #timer_text 00:00
    canvas.itemconfig(timer_text, text="00:00")
    #title_label "Timer"
    title_label.config(text="Timer")
    #reset check_marks
    global marks
    marks = ""
    check_marks.config(text=marks) 
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    #If it's the 8th rep:
    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    #If it's the 2nd/4th/6th rep:
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    #If it's the 1st/3rd/5th/7th rep:
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            global marks
            marks += "✔"
            check_marks.config(text=marks) 
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()