from turtle import Turtle

STEP_SIZE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.snake_head = self.segments[0]

    def add_segment(self, position):
        turt = Turtle('square')
        turt.color('white')
        turt.penup()
        turt.goto(position)

        self.segments.append(turt)


    def create_snake(self):
        for n in range(3):
            self.add_segment((n * -20, 0))


    def move(self):
        for n in range(len(self.segments) - 1, 0, -1):
            prev_pos = self.segments[n - 1].pos()
            self.segments[n].goto(prev_pos)

        self.snake_head.forward(STEP_SIZE)

    def extend_snake(self):
        last_seg_pos = self.segments[-1].pos()
        self.add_segment(last_seg_pos)


    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)
    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)
    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)
    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)