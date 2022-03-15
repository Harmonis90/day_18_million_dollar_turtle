
import turtle
import random


turt = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
dot_size = 20
spacing = 50

rgb_colors = [(37, 94, 184), (235, 165, 81), (244, 223, 89), (249, 51, 22), (97, 196, 234), (215, 69, 104),
              (202, 70, 21), (240, 105, 142), (250, 138, 167), (187, 47, 91), (142, 234, 216), (166, 175, 232),
              (67, 46, 12), (73, 206, 172), (83, 189, 100), (253, 220, 0), (20, 158, 51), (249, 147, 3), (24, 37, 88),
              (104, 39, 44), (154, 30, 9)]

def draw_dots():
    for x in range(10):

        for i in range(10):
            turt.dot(dot_size, random.choice(rgb_colors))
            turt.fd(spacing)
            if i == 9:
                if x % 2 == 0:
                    turt.dot(dot_size, random.choice(rgb_colors))
                    turt.seth(90)
                    turt.fd(spacing)
                    turt.seth(180)
                else:
                    turt.dot(dot_size, random.choice(rgb_colors))
                    turt.seth(90)
                    turt.fd(spacing)
                    turt.seth(0)


width = screen.window_width()
height = screen.window_height()
x_start = (width / 2) * 0.5
y_start = (height / 2) * 0.5


turt.penup()
turt.goto(-x_start, -y_start)
draw_dots()
turtle.exitonclick()