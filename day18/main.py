from turtle import Turtle, Screen, colormode
import random

screen = Screen()
colormode(255)

color_list = [(184, 148, 95), (151, 104, 46), (179, 150, 22), (83, 34, 27), (12, 56, 72), (32, 100, 120), (101, 41, 47), (57, 136, 121), (107, 40, 30), (23, 65, 50), (40, 80, 7)]

turt = Turtle()
turt.speed(0)
turt.shape("arrow")
# turt.pensize(10)

turt.setheading(225)
turt.penup()
turt.hideturtle()
turt.forward(300)
turt.setheading(0)
size = 0

while size < 10:
    for i in range(10):
        turt.dot(20, random.choice(color_list))
        # print(turt.position())
        
        turt.penup()
        turt.forward(100)
        turt.pendown()
        
    turt.left(90)
    turt.penup()
    turt.forward(100)
    turt.left(90)
    turt.forward(1000)
    turt.setheading(0)
    size += 1




screen.exitonclick()