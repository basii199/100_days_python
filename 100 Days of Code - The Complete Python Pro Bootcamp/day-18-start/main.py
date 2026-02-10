import turtle
from turtle import Turtle,Screen
import random

turtle.colormode(255)
tiny = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r,g,b

# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'cyan']

# Draw a square

# tiny.forward(100)
# tiny.left(90)
# tiny.forward(100)
# tiny.left(90)
# tiny.forward(100)
# tiny.left(90)
# tiny.forward(100)

# Draw dashed lines

# for _ in range(15):
#     tiny.forward(10)
#     tiny.penup()
#     tiny.forward(10)
#     tiny.pendown()

# Draw shape with 3,4,5,6,7,8,9,10 sides

# for n in range(3,11):
#     baby_turtle = Turtle()
#
#     for _ in range(n):
#         baby_turtle.pencolor(colors[n-4])
#         baby_turtle.forward(100)
#         baby_turtle.right(360/n)

# Build random walk

# tiny.speed(8)
# tiny.pensize(10)
#
# b = random_color()
# print(b)
#
# for _ in range(100):
#     # tiny.pencolor(random.choice(colors))
#     tiny.pencolor(random_color())
#     tiny.forward(20)
#     tiny.setheading(random.choice([0,90,180,270]))

# Make a spirograph

# tiny.speed(10)
# def draw_circle(angle):
#     for _ in range(int(360/angle)):
#         tiny.pencolor(random_color())
#         tiny.circle(100)
#         tiny.right(angle)
#
# draw_circle(5)

# Hirst Painting

colorgram_colors = [(173, 71, 45), (27, 33, 65), (243, 233, 71), (56, 87, 147), (220, 139, 92), (51, 38, 30), (132, 32, 47), (126, 160, 208), (224, 80, 52), (210, 82, 124), (41, 49, 128), (139, 33, 26), (148, 55, 76), (63, 30, 39), (88, 111, 206), (125, 183, 133), (33, 48, 39), (197, 135, 158), (73, 76, 40), (70, 106, 56), (164, 187, 238), (154, 138, 68), (41, 76, 59), (241, 161, 152), (227, 171, 187), (156, 202, 220)]

def draw_hirst(size, radius, gap):
    tiny.penup()
    tiny.hideturtle()
    tiny.speed('fastest')
    tiny.goto(-250,-250)

    for _ in range(size):
        for _ in range(size):
            tiny.pencolor(random.choice(colorgram_colors))
            tiny.dot(radius)
            tiny.forward(gap)

        tiny.goto(-250, tiny.ycor() + gap)

draw_hirst(10, 20, 50)

my_screen = Screen()
my_screen.exitonclick()