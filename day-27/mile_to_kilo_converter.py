# TODO 1: Set up the Tkinter window (title, padding, and mainloop at the bottom).

# TODO 2: Create the miles Entry and the four Labels ("Miles", "is equal to", "0", "Km").

# TODO 3: Create the Calculate Button.

# TODO 4: Place every widget on a 3x3 grid using column and row numbers.

# TODO 5: Write the miles_to_km function to read the Entry, convert to km, and update the result Label.

# TODO 6: Wire the Calculate Button to miles_to_km and test with 20 miles.

from tkinter import *


def button_clicked():
    miles_to_km = round(float(miles_input.get()) * 1.609)
    result_label.config(text=miles_to_km)


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=7)
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles", font=("Arial", 24, "bold"))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 24, "bold"))
equal_label.grid(column=0, row=1)

result_label = Label(text="0", font=("Arial", 24, "bold"))
result_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 24, "bold"))
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
