from turtle import Turtle


def get_high_score():
    with open('data.txt') as file:
        return int(file.read())

def write_high_score(score):
    with open('data.txt', 'w') as file:
        file.write(str(score))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.color('white')
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.goto(0, 280)
        self.high_score = get_high_score()
        self.score = 0
        self.write_score()

    def write_score(self):
        self.write(f'Score: {self.score}. High Score {self.high_score}', False, 'center', font=('Arial', 16, 'normal'))

    def update_score(self, score=1):
        self.score += score
        self.clear()

        if self.score > self.high_score:
            write_high_score(self.score)
            self.high_score = self.score

        self.write_score()

    def game_over(self):
        self.goto(0,0)
        self.write('Game Over',False, 'center', font=('Arial', 16, 'normal'))
