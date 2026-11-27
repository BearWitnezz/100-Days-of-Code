# TODO 1: Import tkinter and set up the "Password Manager" window with 20px padding on all sides (keep it open at the bottom).
# TODO 2: Create a 200x200 Canvas and load logo.png with PhotoImage.
# TODO 3: Put the logo right in the center of the canvas, then pack the canvas onto the window.
# TODO 4: Switch the canvas from pack() to grid() in the top row, middle column.
# TODO 5: Add the three Labels down column 0 (Website:, Email/Username:, Password:).
# TODO 6: Add the three Entry boxes beside them. Which two need columnspan?
# TODO 7: Add the "Generate Password" button next to the password box, and the "Add" button on the bottom row spanning 2 columns.
# TODO 8: Put the cursor in the website box on launch, and pre-fill the email box with a default email.
# TODO 9: Write save() in SAVE PASSWORD to grab the text from all three entries, and hook it up to the Add button.
# TODO 10: Open data.txt in append mode and write "website | email | password" on its own new line.
# TODO 11: Clear the website and password boxes after saving (leave the email box alone).
# TODO 12: Import messagebox from tkinter (why doesn't * bring it in?).
# TODO 13: Before saving, check if the website or password is empty — if either is, show an info popup ("Oops") and stop there.
# TODO 14: Otherwise, ask OK/Cancel showing the email and password, and only save + clear the boxes if they click OK.
# TODO 15: Drop the starter password generator into PASSWORD GENERATOR and rewrite the three for-loops as list comprehensions (using choice and randint).
# TODO 16: Combine the three lists, shuffle them, and turn the list into one string with "".join(...).
# TODO 17: Wrap it in generate_password(), hook it to the Generate Password button, and insert the new password into the password box.
# TODO 18: Install pyperclip (in VS Code terminal: python -m pip install pyperclip), import it, and copy the generated password to your clipboard.

from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    nr_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    nr_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = nr_letters + nr_symbols + nr_numbers
    random.shuffle(password_list)
    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website_save = website_input.get()
    email_username_save = email_username_input.get()
    password_save = password_input.get()

    if len(website_save) == 0 or len(password_save) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_save, message=f"These are the details entered: \nEmail: {email_username_save} "
                                                                f"\nPassword: {password_save} \nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as new_file:
                new_file.write(f"{website_save} | {email_username_save} | {password_save}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
mypass_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=mypass_img)
canvas.grid(column=1, row=0)

#Labels

website = Label(text="Website:")
website.grid(column=0, row=1)

email_username = Label(text="Email/Username:")
email_username.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

#Entries

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "john@gmail.com")

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

#Buttons

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add = Button(text="Add", width=36, command=save)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()