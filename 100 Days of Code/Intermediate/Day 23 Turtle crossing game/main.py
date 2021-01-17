import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkey(player.go_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()



    #detect crossing
    if player.is_at_finish_line():
        # delete turtles after finishing level
        for car in car_manager.all_cars:
            car.hideturtle()
        car_manager.all_cars = []
        player.goto_start()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()