from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

Y_EDGE_LIMIT = 280
X_EDGE_LIMIT = 370
ALLOWANCE = 5

screen = Screen()
ball = Ball()
right_pad = Paddle((350,0))
left_pad = Paddle((-350,0))
scoreboard = Scoreboard()

screen.setup(800,600)
screen.bgcolor('black')
screen.title('Pong')
screen.listen()

screen.onkey(right_pad.go_up, 'Up')
screen.onkey(right_pad.go_down, 'Down')

screen.onkey(left_pad.go_up, 'w')
screen.onkey(left_pad.go_down, 's')

is_game = True
while is_game:
    ball.move()

    if ball.ycor() > Y_EDGE_LIMIT + ALLOWANCE or ball.ycor() < -Y_EDGE_LIMIT:
        ball.bounce_y()

    if (right_pad.distance(ball) < 50 and ball.xcor() > 330) or (left_pad.distance(ball) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    if ball.xcor()>X_EDGE_LIMIT:
        scoreboard.l_point()
        ball.reset_ball()

    if ball.xcor()<-X_EDGE_LIMIT:
        scoreboard.r_point()
        ball.reset_ball()














screen.exitonclick()