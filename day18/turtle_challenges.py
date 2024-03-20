from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
screen = Screen()
tim.shape("arrow")
# tim.pensize(10)
tim.speed(0)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

## drawing a square
# for i in range(0,4):
#     tim.forward(100)
#     tim.right(90)

## drawing a dashed line
# for i in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

## drawing multiple shapes
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "cyan"]

# def draw_shape(num_of_sides):
#     angle = 360 / num_of_sides
#     for i in range(num_of_sides):
#         tim.forward(100)
#         tim.right(angle)

# for i in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(i)

## drawing random walk
# directions = [0, 90, 180, 270]
# angles = [tim.right(90), tim.left(90)]



# for i in range(60):
    # color = random_color()
    # tim.forward(30)
    # tim.setheading(random.choice(directions))
    # tim.color(color)

## drawing a spirograph
for i in range (40):
    color = random_color()
    tim.color(color)
    tim.circle(100)
    tim.setheading(tim.heading() + 10)



screen.exitonclick()