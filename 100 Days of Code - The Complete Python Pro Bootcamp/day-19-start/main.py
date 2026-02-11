import random
from collections import OrderedDict
from turtle import Turtle, Screen

# tiny = Turtle()
screen = Screen()

# Free moving arrow from user input
# def forward():
#     tiny.forward(10)
# def backward():
#     tiny.backward(10)
# def counter_clock():
#     tiny.left(10)
# def clock_wise():
#     tiny.right(10)
# def clear_screen():
#     tiny.clear()
#     tiny.penup()
#     tiny.home()
#     tiny.pendown()

# screen.listen()
# screen.onkey(forward, 'w')
# screen.onkey(backward, 's')
# screen.onkey(counter_clock, 'a')
# screen.onkey(clock_wise, 'd')
# screen.onkey(clear_screen, 'c')

# Turtle racing game

colors = ['red','orange','yellow','green','blue','indigo']

screen.setup(height=400, width=500)

while True:
    user_bet = screen.textinput(title='Pick a color to place your bet', prompt=f'{colors}')
    if user_bet in colors:
        break

screen.listen()

turtles = []
positions = {}

is_game = False

def show_scores(scores):
    ordered_scores = OrderedDict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

    top_three = []
    res_list = list(ordered_scores.items())
    for x in range(3):
        top_three.append(res_list[x][0])

    return f'First: {top_three[0].title()}, Second: {top_three[1].title()}, Third: {top_three[2].title()}'

def play():
    global is_game
    while is_game:
        for turtle in turtles:
            turtle_color = turtle.pencolor()
            if turtle.xcor()>230:
                is_game = False
                result = 'You win!' if user_bet == turtle_color else 'You lose!'
                screen.title(f'{result} The winner is {turtle_color}.')

            move = random.randint(1,10)
            turtle.forward(move)
            positions[turtle_color] = positions.get(turtle_color,0) + move

        screen.title(show_scores(positions))

def start_game():
    global is_game
    is_game = True
    play()

for n in range(len(colors)):
    new_turtle = Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[n])
    new_turtle.goto(-240, -75 + (n*30))
    turtles.append(new_turtle)

screen.title('Press \'space\' to start')
screen.onkey(start_game, 'space')


screen.exitonclick()