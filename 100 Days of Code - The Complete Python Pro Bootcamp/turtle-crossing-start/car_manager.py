import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.cars_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.spawn_chance = 6
        self.add_car()

    def add_car(self):
        chance = random.randint(1, int(self.spawn_chance))
        if chance == 1:
            car = Car(self.cars_speed)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.move_forward()

        self.cars = [car for car in self.cars if car.xcor() > -320]

    def level_up(self):
        # self.cars = []
        self.spawn_chance -= 0.5
        for car in self.cars:
            car.speed_up()
        self.cars_speed += MOVE_INCREMENT
        # self.add_car()



class Car(Turtle):
    def __init__(self, speed):
        super().__init__()
        self.move_speed = speed

        self.penup()
        self.hideturtle()
        self.color(random.choice(COLORS))
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(320, random.randint(-250,250))
        self.setheading(180)
        self.showturtle()

    def move_forward(self):
        self.forward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT



