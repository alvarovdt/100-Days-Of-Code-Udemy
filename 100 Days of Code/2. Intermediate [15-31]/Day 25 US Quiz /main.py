import turtle
import pandas

from turtle import Turtle
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state = Turtle()
state.hideturtle()
state.penup()
data = pandas.read_csv("50_states.csv")
states_as_list = data.state.to_list()
correct_states = []
missing_states = []
total_states = 0
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{total_states}/50 Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        game_is_on = True
        for state in states_as_list:
            if state not in correct_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in states_as_list:
        if answer_state not in correct_states:
            correct_states.append(answer_state)
            total_states += 1
            answer_data = data[data.state == answer_state]
            x_coord = int(answer_data.x)
            y_coord = int(answer_data.y)
            state.goto(x_coord, y_coord)
            state.write(answer_state)
            if total_states == 50:
                game_is_on = True
