import time
from turtle import Screen

import scoreboard
from paddle import Paddle
from ball import Ball
from scoreboard import  Scoreboard

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)
right_paddle = Paddle(5, 1, (350, 0))
left_paddle = Paddle(5, 1, (-350, 0))
ball = Ball((0, 0))
scoreboard = Scoreboard()
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
game_is_on = True
while game_is_on:

    time.sleep(ball.move_speed)
    ball.move()
    screen.update()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.left_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.right_point()
screen.exitonclick()