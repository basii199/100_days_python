import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()
screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move_player, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()
    car_manager.move_cars()

    for car in car_manager.cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.finish:
        player.reset_player()
        car_manager.level_up()
        scoreboard.update_score()


screen.exitonclick()