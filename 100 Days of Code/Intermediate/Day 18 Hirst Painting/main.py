###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import turtle as turtle_module
import random

dot_count = 0
t = turtle_module.Turtle()

color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

def setup():
    turtle_module.colormode(255)
    t.hideturtle()
    t.penup()
    t.setheading(225)
    t.forward(300)
    t.setheading(0)

def draw_hirst_painting(number_of_dots, size_dot, forward_dot):
    for dot_count in range(1, number_of_dots+1):
        t.pendown()
        t.dot(size_dot, random.choice(color_list))
        t.penup()
        t.forward(forward_dot)

        if dot_count % 10 == 0:
            t.setheading(90)
            t.forward(forward_dot)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)

setup()
draw_hirst_painting(100,20,50)
s = turtle_module.Screen()
s.exitonclick()

