import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()

        self.penup()
        self.shape('circle')
        self.shapesize(0.5,0.5)
        self.speed(0)
        self.new_position()
        self.color('red')

    def new_position(self):
        x = random.randint(-270,270)
        y = random.randint(-270,270)

        self.goto(x,y)