from turtle import Turtle, Screen

screen = Screen()
turt = Turtle()

def move_forward():
    turt.forward(15)

def move_backwards():
    turt.backward(15)

def turn_left():
    turt.left(10)

def turn_right():
    turt.right(10)

def clear_screen():
    turt.clear()
    turt.penup()
    turt.home()
    turt.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(clear_screen, "c")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")

screen.exitonclick()
