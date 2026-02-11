from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(0, 280)

        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}', False, 'center', font=('Arial', 16, 'normal'))

    def update_score(self, score=1):
        self.score += score
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over',False, 'center', font=('Arial', 16, 'normal'))
