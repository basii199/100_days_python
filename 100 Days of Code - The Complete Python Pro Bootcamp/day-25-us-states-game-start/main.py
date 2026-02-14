from turtle import  Turtle, Screen
from state import State
import pandas as pd

screen = Screen()
turtle = Turtle()
map_image = 'blank_states_img.gif'

screen.setup(725, 490)
screen.addshape(map_image)
turtle.shape(map_image)

states = pd.read_csv('50_states.csv')

correct_guesses = []
input_title = 'US States'

while len(correct_guesses) < 50:
    user_guess = screen.textinput(f'{input_title}','Guess a state').lower()
    if user_guess == 'exit':
        missing_states = []
        for state in states.state.str.lower().to_list():
            if state not in correct_guesses:
                missing_states.append(state.title())

        pd.DataFrame(missing_states).to_csv('states_to_learn.csv')
        break

    if user_guess in states.state.str.lower().to_list():
        state_data = states[states.state.str.lower() == user_guess]

        name = state_data['state'].item()
        x = state_data['x'].item()
        y = state_data['y'].item()
        state = State(name, x, y)

        correct_guesses.append(name)
        input_title = f'{len(correct_guesses)}/50 States Correct'

# screen.exitonclick()