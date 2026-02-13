from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.x_move = 2
        self.y_move = 2

        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0,0)

    def speed_up(self):
        self.x_move *= 1.1
        self.y_move *= 1.1

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.speed_up()

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move

        self.goto(x, y)

    def reset_ball(self):
        self.hideturtle()
        self.goto(0,0)
        self.x_move = 2
        self.y_move = 2
        self.showturtle()
        self.bounce_x()


