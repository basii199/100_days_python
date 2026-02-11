from turtle import Screen
from scoreboard import Scoreboard
from food import Food
from snake import Snake
import time

scoreboard = Scoreboard()
screen = Screen()
snake = Snake()
food = Food()

screen.setup(600,600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.snake_head.distance(food) < 15:
        food.new_position()
        snake.extend_snake()
        scoreboard.update_score()

    x=snake.snake_head.xcor()
    y=snake.snake_head.ycor()

    if x > 280 or x < -280 or y >280 or y < -280:
        is_game = False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if snake.snake_head.distance(segment) < 10:
            is_game = False
            scoreboard.game_over()







screen.exitonclick()