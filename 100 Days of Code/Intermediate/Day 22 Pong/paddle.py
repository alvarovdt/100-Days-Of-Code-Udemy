from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, width, height, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=width, stretch_len=height)
        self.goto(position)
        self.color("white")

    def go_up(self):
        if self.ycor() < 240:
            self.goto(self.xcor(), self.ycor()+30)

    def go_down(self):
        if self.ycor() > -240:
            self.goto(self.xcor(), self.ycor()-30)
