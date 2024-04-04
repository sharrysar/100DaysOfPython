from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# window set up
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# tomato pic set up
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=img)
canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

# label set up
timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)
timer_label.config(font=(FONT_NAME, 35))

# start button
start_btn = Button(text="Start")
start_btn.grid(column=0, row=2)

# reset button
reset_btn = Button(text="Reset")
reset_btn.grid(column=2, row=2)

# fire emoji
fire_emoji = Label(text="✔", fg=GREEN, bg=YELLOW)
fire_emoji.grid(column=1, row=3)
fire_emoji.config(font=(FONT_NAME, 35))

window.mainloop()