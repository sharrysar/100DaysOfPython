from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

#---------------------- DATA -----------------------#
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    orig_data = pandas.read_csv("data/ukrainian_words.csv")
    data_dict = orig_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

#---------------------- FUNCTIONS ------------------#
def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(data_dict)
    canvas.itemconfig(card_label, text="Ukrainian", fill="black")
    canvas.itemconfig(word_label, text=current_card['Ukrainian'], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flip_timer = window.after(3000, func=flip_card)

def guessed():
    data_dict.remove(current_card)
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    new_card()
    


def flip_card():
    canvas.itemconfig(card_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=current_card['English'], fill="white")
    canvas.itemconfig(canvas_image, image=back_img)

#---------------------- UI SET UP ------------------#
# window set up
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# cards
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
card_label = canvas.create_text(400, 150, text="", font=("Ariel", 30, "italic"))
word_label = canvas.create_text(400,263, text="", font=("Ariel", 50, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# buttons
red_btn_img = PhotoImage(file="images/wrong.png")
red_btn = Button(image=red_btn_img, highlightthickness=0, command=new_card)
red_btn.grid(column=0, row=1)

green_btn_img = PhotoImage(file="images/right.png")
green_btn = Button(image=green_btn_img, highlightthickness=0, command=guessed)
green_btn.grid(column=1, row=1)

new_card()

window.mainloop()
