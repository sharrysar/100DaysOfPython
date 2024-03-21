from turtle import Turtle, Screen, colormode
import random

screen = Screen()
screen.setup(width=700, height=500)

user_bet = screen.textinput("Make your bet", "Enter a color: ")
y_positions = [100, 50, 0, -50, -100]
colors = ["red", "orange", "blue", "green", "brown"]
race_on = False
all_turts = []

for i in range(5):
    turt = Turtle(shape="turtle")
    turt.penup()
    turt.goto(x=-330, y=y_positions[i])
    turt.color(colors[i])
    all_turts.append(turt)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turts:
        if turtle.xcor() > 330:
            race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner.")
            else:
                print(f"You've lost. The {winner} turtle is the winner.")

        ran_distance = random.randint(0, 10)
        turtle.forward(ran_distance)

screen.exitonclick()