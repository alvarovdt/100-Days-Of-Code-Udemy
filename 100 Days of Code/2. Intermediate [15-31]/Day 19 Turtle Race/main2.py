from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a name Leonardo, "
                                                          "Michelangelo, Donatello, Raphael, Splinter: ")
colors = ["blue", "orange", "purple", "red", "brown"]
names = ["Leonardo", "Michelangelo", "Donatello", "Raphael", "Splinter"]
turtles = []
is_race_on = False
players = len(names)
for i in range(players):
    turtles.append(Turtle(shape="turtle"))
    turtles[i].color(colors[i])
    turtles[i].penup()
    turtles[i].goto(x=-230, y=(-50+i*30))

turtles[4].shape("circle")
if user_bet:
    is_race_on = True
while is_race_on:
    for index in range(players):
        if turtles[index].xcor() > 230:
            is_race_on = False
            winning_turtle = names[index]
            if winning_turtle == user_bet:
                print(f"You've won! The {names[index]} turtle is the winner")
            else:
                print(f"You've lost! The {names[index]} turtle is the winner")
        rand_dist = random.randint(0, 10)
        turtles[index].forward(rand_dist)

screen.exitonclick()