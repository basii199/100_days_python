from turtle import  Turtle

MOVE_DISTANCE = 20
EDGE_LIMIT = 240

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()

        self.hideturtle()
        self.shape('square')
        self.color('white')
        self.penup()
        self.speed(0)
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.showturtle()

    def go_up(self):
        x = self.xcor()
        y = self.ycor()

        if y + MOVE_DISTANCE > EDGE_LIMIT:
            pass
        else:
            self.goto(x, y + MOVE_DISTANCE)

    def go_down(self):
        x = self.xcor()
        y = self.ycor()

        if y - MOVE_DISTANCE < -EDGE_LIMIT:
            pass
        else:
            self.goto(x, y - MOVE_DISTANCE)
