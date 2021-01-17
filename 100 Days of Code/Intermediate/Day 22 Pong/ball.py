from turtle import Turtle


class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.goto(position)
        self.shape("circle")
        self.penup()
        self.pensize(0.5)
        self.color("white")
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.1


    def move(self):
        self.goto(self.xcor()+self.x_move, self.ycor()+self.y_move)

    def y_bounce(self):
        self.y_move *= -1

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()