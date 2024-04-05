from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    pass
# ---------------------------- UI SETUP ------------------------------- #

# window set up
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# image set up
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
# args: position (x, y) and image
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
login_input = Entry(width=35)
login_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

# buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
