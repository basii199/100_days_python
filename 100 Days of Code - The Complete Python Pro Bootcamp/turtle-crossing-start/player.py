from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()

        self.finish = False

        self.hideturtle()
        self.penup()
        self.goto(STARTING_POSITION)
        self.showturtle()
        self.shape('turtle')
        self.setheading(90)

    def move_player(self):
        if self.ycor() + MOVE_DISTANCE > FINISH_LINE_Y:
            self.finish = True
            pass
        else:
            self.forward(MOVE_DISTANCE)

    def reset_player(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
        self.finish = False
    # def level_up(self):