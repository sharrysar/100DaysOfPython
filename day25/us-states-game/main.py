import turtle
import pandas

screen = turtle.Screen()
image = "blank_states_img.gif"
data = pandas.read_csv("50_states.csv")

screen.title("Guess US States Game")
screen.addshape(image)
turtle.shape(image)

states = data['state']

def return_y_coor(state):
    y_coor = (data[data.state == state.title()].y)
    return y_coor

def return_x_coor(state):
    x_coor = (data[data.state == state.title()].x)
    return x_coor

score = 0
guesses = []

while score < 50:
    user_answer = screen.textinput(title=f"{score}/50 Guess the State", prompt="Name a state:").title()

    if user_answer in states.values:
        turtle.penup()
        x_coor = float(return_x_coor(user_answer))
        y_coor = float(return_y_coor(user_answer))
        turtle.goto(x_coor, y_coor)
        turtle.write(user_answer)
        score += 1
        guesses.append(user_answer)
        
    else:
        print(False)

turtle.mainloop()