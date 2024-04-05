from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_input.get()
    login = login_input.get()
    password = password_input.get()

    with open("data.txt", "a") as data:
        data.write(f"{website} | {login} | {password}\n")
        
    website_input.delete(0, END)
    password_input.delete(0, END)
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
website_label.grid(column=0, row=1, sticky="W")
login_label = Label(text="Email/Username:")
login_label.grid(column=0, row=2, sticky="W")
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3, sticky="W")

# inputs
website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()
login_input = Entry(width=35)
login_input.grid(column=1, row=2, columnspan=2, sticky="EW")
login_input.insert(0, "myemail@gmail.com")
password_input = Entry(width=23)
password_input.grid(column=1, row=3, sticky="EW")

# buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3, sticky="EW")
add_button = Button(text="Add", width=32, command=save_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")




window.mainloop()
